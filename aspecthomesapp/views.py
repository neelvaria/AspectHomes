from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def loader(request):
    return render(request,"loader.html")

def indexpage(request):
    return render(request,"index.html")

def newsletters(request):
    if request.method == "POST":
        nname = request.POST.get("name")
        nemail = request.POST.get("email")
        
        query = newsletter(name=nname,email=nemail)
        query.save()
    
    return render(request,"index.html")

def signuppage(request):   
    return render(request,"signup.html")

def signupinsert(request):
    if request.method == "POST":    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        role = request.POST['role']
        
        if not username or not email or not password or not confirm_password or not role:
            messages.error(request, "Please fill in all the required fields.")
            return render(request, "signup.html")

        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match.")
            return render(request, "signup.html")
        
        query=user(username=username,email=email,password=password,confirmpassword=confirm_password,role=role)
        query.username = username
        query.email = email
        query.password = password
        query.save() 
        
        messages.success(request, f"Registration successful for {username}. You can now log in.")
        
        subject = "AspectHomes Aapka Swagat hee!!"
        message = render_to_string("emailconfirmation.html", {'username': query.email,'password': query.password})
        from_email = settings.EMAIL_HOST_USER
        to_list = [query.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        
    return render(request, "login.html")

def loginpage(request):
    return render(request,"login.html")

def logincheckup(request):
    if request.method == "POST":
        email = request.POST['log_email']
        password = request.POST['password']

        try:
            query = user.objects.get(email=email, password=password)
            request.session['log_username'] = query.username  # Store username in session
            request.session['log_id'] = query.id
            request.session.save()

            lid = request.session['log_id']
            data = user.objects.get(id=lid)

            designer = None
            if data.role == "Designer":
                designer = True
                return redirect('/designerindex')
            else:
                return redirect('/')

        except user.DoesNotExist:
            messages.error(request, "Incorrect email or password. Please try again.")

    return render(request, "login.html")
    
def logout(request):
    try:
        del request.session["log_username"]
    except:
        pass
    return render(request,"login.html")
    
def profile(request):
    return render(request,"profile.html")

def aboutpage(request):
    return render(request,"about.html")

def servicespage(request):
    return render(request,"services.html")

def talkdesigners(request):
    if request.method == "POST":
        tname = request.POST.get("name")
        temail = request.POST.get("email")
        tphone = request.POST.get("phone")
        tsubject = request.POST.get("subject")
        
        if not temail:
            messages.error(request, "Please provide an email address.")
            return redirect("service")
        
        query = talkdesigner(name=tname, email=temail, subject=tsubject, phone=tphone)
        try:
            query.save()
            messages.success(request,"Thank you! Our Team reach you soon!!")
        except:
            messages.error(request,"Opps An Error Occured!!")
        return redirect("service")        
    return render(request,"service.html")

def email(request):
    return render(request,"emailconfirmation.html")

def bid(request):
    return render(request,"bid.html")

def biddata(request):
    if request.method == "POST":
        lid = request.session.get('log_id')
        if not lid:
            messages.error(request, 'User not logged in')
            return redirect('login')
            
        bimage = request.FILES.get("preferredstyle")
        desc = request.POST.get("description")
        budget = request.POST.get("budget")
        virtual = request.FILES.get("virtual")
        
        if not bimage or not desc or not budget or not virtual:
            messages.error(request, 'All fields are required')
            return render(request, "bid.html")
        
        user_instance = user.objects.get(id=lid)
        insertdata = requirement(u_id=user_instance,preferredstyle=bimage,description=desc,budget=budget,virtual=virtual)  
        insertdata.save()  
              
        messages.success(request, 'Your details have been submitted successfully!')
        return redirect('bid')

    return render(request,"bid.html")

def viewbidding(request):
    userid = request.session['log_id']
    data = requirement.objects.filter(u_id=userid).values('id')
    
    biddata=bidding.objects.filter(requirementid__in=data)

    context = {
        "reqdata":biddata
    }    
    return render(request,"viewbid.html",context)

def bookings(request,id):
    userid = request.session['log_id']
    data =bidding.objects.get(id=id)
    
    
    context = {
        "reqid":id,
        "data":data
    }
    
    return render(request,"book.html",context)

def payatdoorstep(request):
    offline=request.POST.get('offline')
    online=request.POST.get('online')
    
    if offline:
        if request.method == "POST":
            uid = request.session['log_id']
            bids = request.POST.get("requirementid")
            
            user_instance = user.objects.get(id=uid)
            bid = bidding.objects.get(id=bids)
            
            query = booking(u_id=user_instance,bid=bid,totalamount=bid.bidamount)
            query.save()
            
            name = request.POST.get("name")
            email = request.POST.get("email")
            address = request.POST.get("address")
            city = request.POST.get("city")
            state = request.POST.get("state")
            zipcode = request.POST.get("zipcode")

            booking_id = query.id
            insert = billing(u_id=user_instance,cname=name,book_id=booking(booking_id),cemail=email,caddress=address,city=city,state=state,zipcode=zipcode)
        
        
            insertpay = payment(u_id=user_instance, mode="Cash", status="Paid", b_id=booking(booking_id))
            insertpay.save()
            insert.save()
            messages.success(request,"Booked SucessFully!!")
            
        return redirect('success')
                     
    elif online:
        if request.method == "POST":
            uid = request.session['log_id']
            bids = request.POST.get("requirementid")
            
            user_instance = user.objects.get(id=uid)
            bid = bidding.objects.get(id=bids)
            
            query = booking(u_id=user_instance,bid=bid,totalamount=bid.bidamount)
            
            name = request.POST.get("name")
            email = request.POST.get("email")
            address = request.POST.get("address")
            city = request.POST.get("city")
            state = request.POST.get("state")
            zipcode = request.POST.get("zipcode")
            
            cardname = request.POST.get("cardname")
            cardnumber = request.POST.get("cardnum")
            expiry = request.POST.get("expiry")
            cvv = request.POST.get("cvv")
            
            carddata = card.objects.first()
            num = carddata.card_number
            exp = carddata.expirydate
            cvv = carddata.cvv
                        
            if cardnumber == num and expiry == exp and cvv == cvv:
                booking_id = query.id
                insert = billing(u_id=user_instance,cname=name,book_id=booking(booking_id),cemail=email,caddress=address,city=city,state=state,zipcode=zipcode)
                insertpay = payment(u_id=user_instance, mode="Card", status="Paid", b_id=booking(booking_id))
                insertpay.save()
                insert.save()
                messages.success(request,"Booked SucessFully!!")
            return redirect('success') 

    return render(request,"index.html")

def success(request):
    return render(request,"success.html")

def bookedservice(request):
    userid = request.session['log_id']
    data = booking.objects.filter(u_id=userid).values('id')
    biddata=payment.objects.filter(b_id__in=data)
    context = {
        "udata":data,
        "bdata":biddata
    }
    return render(request,"bookedbids.html",context)

def contact(request):
    return render(request,"contact.html")

def contactformdata(request):
    if request.method == "POST":
        cname = request.POST.get("name")
        cemail = request.POST.get("email")
        csubject = request.POST.get("subject")
        cmessage = request.POST.get("message")
        
        if not cemail:
            messages.error(request, "Please provide an email address.")
            return redirect("contact")
        
        query = contactus(name=cname, email=cemail, subject=csubject, message=cmessage)
        try:
            query.save()
            messages.success(request,"Form submitted successfully. Thank you!")
        except:
            messages.error(request,"Opps An Error Occured!!")
        return redirect("contact")
    return render(request, "contact.html")

def blogpage(request):
    return render(request,"blog.html")

def residential(request):
    return render(request,"residantial.html")

def office(request):
    return render(request,"office.html")

def commercial(request):
    return render(request,"commercial.html")

def portfolio(request):
    return render(request,"portfolio.html")

def blogsingle(request):
    return render(request, "blog-single.html")

def commingsoon(request):
    return render(request,"coming-soon.html")

def ecommerce(request):
    return render(request,"ecommerce.html")

def faq(request):
    return render(request,"faq.html")

def gallery(request):
    return render(request,"gallery.html")

def termsservice(request):
    return render(request,"terms-service.html")

#designerside 
def designerindex(request):
    return render(request,"designer/index.html")

def designerabout(request):
    return render(request,"designer/about.html")

def designerservice(request):
    return render(request,"designer/services.html")
    
def designerbidding(request,id):
    context = {
        "reqid":id
    }
    return render(request,"designer/bidding.html",context)

def designermanagebid(request):
    alldata = requirement.objects.all()
    context = {
        "data":alldata
    }
    return render(request,"designer/managebid.html",context)

def designersubmitbid(request):
    if request.method == "POST":
        uid = request.session['log_id']
        reqid = request.POST.get("id")
        bidamt = request.POST.get("bidAmount")
        desc = request.POST.get("desc")
    
        user_instance = user.objects.get(id=uid)
        reqi_instance = requirement.objects.get(id=reqid)

    
        query = bidding(u_id=user_instance,requirementid=reqi_instance,bidamount=bidamt,desc=desc)
        query.save()
      
    return render(request,"designer/bidding.html")

def designerfaq(request):
    return render(request,"designer/designerfaq.html")

def termsservicedesigner(request):
    return render(request,"designer/terms.html")

def portfoliodesigner(request):
    return render(request,"designer/portfolio.html")

def descontact(request):
    return render(request,"designer/contact.html")

def contactformdata(request):
    if request.method == "POST":
        cname = request.POST.get("name")
        cemail = request.POST.get("email")
        csubject = request.POST.get("subject")
        cmessage = request.POST.get("message")
        
        if not cemail:
            messages.error(request, "Please provide an email address.")
            return redirect("descontact")
        
        query = contactus(name=cname, email=cemail, subject=csubject, message=cmessage)
        try:
            query.save()
            messages.success(request,"Form submitted successfully. Thank you!")
        except:
            messages.error(request,"Opps An Error Occured!!")
        return redirect("descontact")
    return render(request, "designer/contact.html")

# def designerbookedbid(request):
#     # userid = request.session['log_id']
#     # # data = booking.objects.filter(bid=userid).values_list('id','bid')
#     # # biddata=payment.objects.filter(b_id__in=data)
#     # data = payment.objects.filter(u_id=userid).values('b_id')
#     # context = {
#     #     "udata":data,
#     #     # "bdata":biddata
#     # }
    
#     userid = request.session.get('log_id')
#     getdata = bidding.objects.filter(u_id=userid).values('id')
#     getbookingdata = booking.objects.filter(bid__in=getdata)
#     context = {
#         "data": getbookingdata,
#     }
    
#     return render(request,"designer/bookedbids.html",context)


def designerbookedbid(request):
    userid = request.session.get('log_id')
    getdata = bidding.objects.filter(u_id=userid).values('id')
    getbookingdata = booking.objects.filter(bid__in=getdata)

    data_with_payment_modes = []
    for booking_instance in getbookingdata:
        payment_modes = payment.objects.filter(b_id=booking_instance).values('mode')
        data_with_payment_modes.append((booking_instance, payment_modes))

    context = {
        "data_with_payment_modes": data_with_payment_modes,
    }

    return render(request, "designer/bookedbids.html", context)

def checkout():
    pass
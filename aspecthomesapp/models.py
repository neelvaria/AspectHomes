from django.db import models
from django.utils.safestring import mark_safe
# # Create your models here.
role = [
    ('User','User'),
    ('Designer','Designer')
]
status_choice = [
    ('Inactive','Inactive'),
    ('Active','Active')
]

modepay = [
    ('Card','Card'),
    ('Cash','Cash')
]

paymentstatus = [
    ('Paid','Paid'),
    ('Unpaid','Unpaid')
]

class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)
    role = models.CharField(max_length=30,choices=role)
    
    class Meta:
        verbose_name='user'
        verbose_name_plural = 'User'
    
    def __str__(self):
        return self.username
    
    
class detail(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE)
    phoneno = models.BigIntegerField()
    profile_pic = models.ImageField(upload_to='Profilepic')
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    work_exp = models.IntegerField()
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.profile_pic.url))
    
    admin_photo.allows_tags = True
    
    class Meta:
        verbose_name='detail'
        verbose_name_plural = 'Detail'
    
class requirement(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE)
    preferredstyle = models.ImageField(upload_to='userstyleimage')
    description = models.TextField()
    submittime = models.TimeField(auto_now=True)
    budget = models.FloatField()
    virtual = models.ImageField(upload_to='360userimages',null=True)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.preferredstyle.url))
    
    admin_photo.allows_tags = True
    
    def admin_virtual(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.virtual.url))
    
    admin_virtual.allows_tags = True

    
    class Meta:
        verbose_name='requirement'
        verbose_name_plural = 'Requirement'
        
    def __str__(self):
       return str(self.u_id)

class virtual(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE)
    imageupload = models.ImageField(upload_to='360')
    description = models.CharField(max_length=100)
    experience = models.IntegerField()
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.imageupload.url))
    
    admin_photo.allows_tags = True
    
    class Meta:
        verbose_name = 'virtual'
        verbose_name_plural = 'Virtual'
    
    def __str__(self):
        return str(self.u_id)

class bidding(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE)
    requirementid = models.ForeignKey(requirement,on_delete=models.CASCADE,null=True)
    bidamount = models.BigIntegerField()
    desc = models.TextField()
    date = models.TimeField(auto_now=True)
    def __str__(self):
        return self.u_id.username
    
    
    class Meta:
        verbose_name = 'bidding'
        verbose_name_plural = 'Bidding'
         
class booking(models.Model):
    u_id = models.ForeignKey(user, on_delete=models.CASCADE)
    bid = models.ForeignKey(bidding, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, editable=False)
    totalamount = models.BigIntegerField()

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'Booking'
        
    def __str__(self):
        return str(self.bid)
    
class payment(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE,related_name='pay_user_type',db_column='ut_id',default=1)
    b_id = models.ForeignKey(booking,on_delete=models.CASCADE)
    paymentdate = models.DateField(auto_now=True,editable=False)
    mode = models.CharField(max_length=20,choices=modepay)
    status = models.CharField(max_length=20,choices=paymentstatus)
    
    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'Payment'
        
    def __str__(self):
        return self.mode
    
class card(models.Model):
   cname = models.CharField(max_length=30,null=True)
   card_number = models.BigIntegerField()
   expirydate = models.CharField(max_length=20, null=True)
   cvv = models.IntegerField(null=True)
   balance = models.IntegerField(null=True)
   transaction_id = models.CharField(max_length=100,null=True,default="")
   datetime = models.DateField(auto_now=True)
   
   class Meta:
       verbose_name = 'card'
       verbose_name_plural = 'Card'

class billing(models.Model):
   u_id = models.ForeignKey(user,on_delete=models.CASCADE)
   dname = models.ForeignKey(requirement,on_delete=models.CASCADE,null=True)
   book_id = models.ForeignKey(booking,on_delete=models.CASCADE,related_name='pay')
   cname = models.CharField(max_length=50,null=True)
   cemail = models.EmailField()
   caddress = models.CharField(max_length=100)
   city = models.CharField(max_length=50)
   state = models.CharField(max_length=100)
   zipcode = models.IntegerField()
   
   class Meta:
       verbose_name = 'billing'
       verbose_name_plural = 'Billing'
   
class project(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE,related_name = 'project_user',default=2)
    project =  models.ImageField(upload_to='project')
    description = models.CharField(max_length=100)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.project.url))
    
    admin_photo.allows_tags = True
    
    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'Project'

class feedback(models.Model):
    u_id = models.ForeignKey(user,on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    submissiondate = models.DateField(auto_now=True,editable=False)
    
    class Meta:
     verbose_name = 'feedback'
     verbose_name_plural = "Feedback"

class newsletter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
     verbose_name = 'newsletter'
     verbose_name_plural = "Newsletter"

class talkdesigner(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    subject = models.TextField()

    class Meta:
     verbose_name = 'talkdesigner'
     verbose_name_plural = "TalkDesigner"
     
class contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    
    class Meta:
        verbose_name = 'contactus'
        verbose_name_plural = "ContactUs"


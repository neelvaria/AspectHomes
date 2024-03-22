from django.contrib import admin
from .models import *
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


# Register your models here.

class signup(admin.ModelAdmin):
    list_display = ("id","username","email","password","confirmpassword","role")
admin.site.register(user,signup)

class detailpage(admin.ModelAdmin):
    list_display = ("id","u_id","phoneno","address","city","state","country","work_exp","profile_pic","admin_photo")
admin.site.register(detail,detailpage)

class requi(admin.ModelAdmin):
    list_display = ("id","u_id","preferredstyle","submittime","budget","admin_photo","virtual","admin_virtual")
admin.site.register(requirement,requi)

class biddingtable(admin.ModelAdmin):
    list_display = ("id","u_id","requirementid","bidamount","desc","date")
    
admin.site.register(bidding,biddingtable)


class paymenttable(admin.ModelAdmin):
    list_display = ("id","u_id","b_id","paymentdate","mode","status")
admin.site.register(payment,paymenttable)

class cardtable(admin.ModelAdmin):
    list_display = ("id","cname","card_number","expirydate","transaction_id","datetime","balance","cvv")
admin.site.register(card,cardtable)

class addbilling(admin.ModelAdmin):
    list_display = ("id","u_id","book_id","dname","cname","cemail","caddress","city","state","zipcode")
admin.site.register(billing,addbilling)

class virtualtable(admin.ModelAdmin):
    list_display = ("id","u_id","imageupload","description","experience","admin_photo")
admin.site.register(virtual,virtualtable)

class projectable(admin.ModelAdmin):
    list_display = ("id","u_id","project","description")
admin.site.register(project,projectable)

class feedbacktable(admin.ModelAdmin):
    list_display = ("id","u_id","description","submissiondate")
admin.site.register(feedback,feedbacktable)

class newsletteradmin(admin.ModelAdmin):
    list_display = ("id","name","email")
admin.site.register(newsletter,newsletteradmin)

class designertalk(admin.ModelAdmin):
    list_display = ("name","email","phone","subject")
admin.site.register(talkdesigner,designertalk)

class contactusadmin(admin.ModelAdmin):
    list_display = ("id","name","email","subject","message")
admin.site.register(contactus,contactusadmin)


def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []
   custom_color_1 = colors.HexColor("#1B4242")  # Example hex code for a custom color
   custom_color_2 = colors.HexColor("#FFFFFF")  # Another example hex code for a custom color

   # Define the style for the table
   style = TableStyle([
    # Header row
    ('BACKGROUND', (0, 0), (-1, 0), custom_color_1),  # Use custom color for header background
    ('TEXTCOLOR', (0, 0), (-1, 0), custom_color_2),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('LINEABOVE', (0, 0), (-1, 0), 1, colors.black),
    # Data rows
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
    ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 12),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    # Grid
    ('GRID', (0, 0), (-1, -1), 1, colors.lightgrey),
])


   # Create the table headers
   headers = ['u_id', 'bid', 'date','totalamount']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.u_id.username, obj.bid, obj.date,obj.totalamount])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"

class showorder(admin.ModelAdmin):
   list_display = ['u_id','bid','date','totalamount']
   list_filter = ['datetime']
   actions = [export_to_pdf]

class userbooking(admin.ModelAdmin):
    def display_username(self, obj):
        return obj.bid.u_id.username
    list_display = ("id","u_id","display_username","date","totalamount")
    list_display = ['u_id','bid','date','totalamount']
    list_filter = ['date']
    actions = [export_to_pdf]
    
admin.site.register(booking,userbooking)

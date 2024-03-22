from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.loader,name="loader"),
    path('index/',views.indexpage,name="index"),
    path('newsletters/',views.newsletters,name="newsletters"),
    
    #signup
    path('signup/',views.signuppage,name="signup"),
    path('sigupinsert/',views.signupinsert,name="signupinsert"),
    
    #login
    path('login/',views.loginpage,name="login"),
    path('logincheckup/',views.logincheckup,name="logincheckup"),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    
    path('service/',views.servicespage,name="service"),
    path('talkdesigners/',views.talkdesigners,name="talkdesigners"),
    path('about/',views.aboutpage,name="about"),
    path('contact/',views.contact,name="contact"),
    path('contactformdata/',views.contactformdata,name="contactformdata"),
    
    #blogpage
    path('blog/',views.blogpage,name="blogpage"),
    path('blogsingle/',views.blogsingle,name="blogsingle"),
    
    #detail
    path('portfolio/',views.portfolio,name="portfolio"),
    path('gallery/',views.gallery,name="gallery"),
   
    #categories
    path('residential/',views.residential,name="residential"),
    path('office/',views.office,name="office"),
    path('commerical/',views.commercial,name="commercial"),
    
    #ecommerce
    path('ecommerce/',views.ecommerce,name="ecommerce"),
    path('commingsoon/',views.commingsoon,name="commingsoon"),
    
    #faq & T&C
    path('faq/',views.faq,name="faq"),
    path('termsservice/',views.termsservice,name="termsservice"),
       
    #bid
    path('bid/',views.bid,name="bid"),
    path('biddata/',views.biddata,name="biddata"),
    path('viewbidding/',views.viewbidding,name="viewbidding"),
    path('booking/<int:id>/',views.bookings,name="booking"),
    path('email/',views.email,name="email"),
    path('success/',views.success,name="success"),
    path('payatdoorstep',views.payatdoorstep,name="payatdoorstep"),
    
    #designer side
    
    #index
    path('designerindex/',views.designerindex,name="designerindex"),
    
    #about & service
    path('designerabout/',views.designerabout,name="designerabout"),
    path('designerservice/',views.designerservice,name="designerservice"),
    path('designerfaq/',views.designerfaq,name="designerfaq"),
    path('termsservicedesigner/',views.termsservicedesigner,name="termsservice"),
    path('portfoliodesigner/',views.portfoliodesigner,name="portfoliodesigner"),
    path('descontact/',views.descontact,name="descontact"),
    path('bookedservice/',views.bookedservice,name="bookedservice"),
    
    #bidding
    path('designerbidding/<int:id>',views.designerbidding,name="designerbidding"),
    path('designermanagebid/',views.designermanagebid,name="designermanagebid"),
    path('designersubmitbid/',views.designersubmitbid,name="designersubmitbid"),
    path('designerbookedbid/',views.designerbookedbid,name="designerbookedbid"),
    
    
]
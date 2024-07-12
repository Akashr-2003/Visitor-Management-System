"""
URL configuration for VisitorMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",home,name="home"),
    path("admin_approval/",admin_approval, name="admin_approval"),
    path("admin_approve/<int:id>/",admin_approve, name="admin_approve"),
    path("admin_reject/<int:id>/",admin_reject, name="admin_reject"),
    path("registration/", registration, name="registration"),
    path("userlogin/",userlogin,name="userlogin"),
    path("userlogout/",userlogout,name="userlogout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("index/",index,name="index"),
    path("NavBar/",NavBar,name="NavBar"), 
    path("employeedetailsview/",employeedetailsview,name="employeedetailsview"),
    path("employeedetailsview/<int:employee_id>", employeedetailsview, name="employeedetailsview_update"),
    path("employeedetailsdelete/<id>",employeedetailsdelete,name="employeedetailsdelete"),
    path("visitordetailsview/",visitordetailsview,name="visitordetailsview"),
    path("visitordetailsview/<int:visitor_id>", visitordetailsview, name="visitordetailsview_update"),
    path("visitordetailsdelete/<id>",visitordetailsdelete,name="visitordetailsdelete"),

]

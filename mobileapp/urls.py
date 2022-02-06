from django.urls import path
from . import views

urlpatterns=[ 
    path('home/',views.fnhome,name="home"),
    path('signup/',views.fnsignup,name="signup")
]
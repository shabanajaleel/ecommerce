from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnaddrole,name="add_role")
]
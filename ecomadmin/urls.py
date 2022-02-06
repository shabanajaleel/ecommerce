from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnroles,name="admin_role"),
    path('add_role/',views.fnaddroles,name="add_role"),
    path('delete_role/<role_id>',views.fndeleteroles,name="delete_role"),

    path('add_admin/',views.fnaddadmin,name="add_admin"),
    path('view_admin/',views.fnviewadmin,name="view_admin"),

    path('login/',views.fnlogin,name="login")
]

from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class RoleForm(forms.ModelForm):
    class Meta:
        model=Role
        fields="__all__"
        widgets={
            'role_name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Role Name'}),
            'status' : forms.Select(attrs={'class':'form-control','placeholder':'Select status'})
        }

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','password1','password2','email','role','phone')
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'role' : forms.Select(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'phone' : forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile No'})
        }

        def save(self,commit=True):
            user=super(CustomUserForm,self).save(commit=False)
            user.role=self.cleaned_data['role']
            user.phone=self.cleaned_data['phone']
            if commit:
                user.save()
                return user
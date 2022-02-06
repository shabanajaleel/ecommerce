from django.shortcuts import render

# Create your views here.
def fnhome(request):
    return render(request,'home.html')

def fnsignup(request):
    return render(request,'signup.html')


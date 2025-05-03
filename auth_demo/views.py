from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 
from django.shortcuts import redirect

@login_required
def home(request):
    return render(request, 'home.html') 

def login_page(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

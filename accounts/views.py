from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse
from .models import Register
# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('index')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request,'accounts/login-register.html',{
        'form' :form 
    })


# @login_required
# def profile_page(request, username):
#     user = get_object_or_404(Register, username=username)
#     return render(request, 'accounts/dashboard.html', {'profile_user': user})


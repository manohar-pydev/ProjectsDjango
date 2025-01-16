from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created.')
            form.save()
            return redirect('login')
    else:    
        form = RegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .emailer import sendOTPToEmail
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
user = get_user_model()
# Create your views here.
def login_page(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        user_obj = User.objects.filter(phone_number=phone_number)
        if not user_obj.exists():
            return redirect('/login/')
        email = user_obj[0].email
        otp = random.randint(1000,9999)
        user_obj.update(otp=otp)
        subject = "OTP for Login"
        message = f"Your otp is {otp}"
        sendOTPToEmail(
            email,
            subject,
            message,
        )
        return redirect('/check-otp/{user_obj.id}/')
    
    return render(request, 'login.html')

def check_otp(request, user_id):
    if request.method == "POST":
        otp = request.POST.get('otp')
        user_obj = User.objects.get(id=user_id)
        if otp == user_obj.otp:
            login(request)
            return redirect("/dashboard/")
        messages.error(request,"Invalid OTP")
        return redirect('/check-otp/{user_obj[0].id}/')
    return render(request, 'check_otp.html')
    
@login_required(login_url = '/')
def dashboard(request):
    return HttpResponse("You are logged in")
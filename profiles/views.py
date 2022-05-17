from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, logout, login
from profiles.models import UserProfile
def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        form_object = User.objects.filter(username = email)
        if form_object.exists():
            messages.warning(request, 'Try resetting your password, we found an account with this credientials')
            return HttpResponseRedirect(request.path_info) 
        form_object = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = email)       
        form_object.set_password(password)
        form_object.save() 
        messages.success(request, 'Please verify your email')
    return render (request, 'profiles/register.html')
def login_page(request):  # sourcery skip: last-if-guard, use-named-expression
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)
        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)
        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)
        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')
        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)
    return render(request ,'accounts/login.html')
def activate_email(request , email_token):
    try:
        user = UserProfile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')


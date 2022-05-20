from base64 import urlsafe_b64decode, urlsafe_b64encode
from email import message_from_binary_file
from email.errors import MessageError
from email.message import EmailMessage
from http.client import REQUEST_ENTITY_TOO_LARGE
from math import prod
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm,UserForm,UserProfileForm,UserLoginForm
from .models import Account, UserProfile
from django.contrib import messages , auth
 

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
import requests
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username,password=password)
            user.phone_number = phone_number
            user.save()
            # messages.success(request, 'Submitted successfully, Please check your mailbox to verify your Email!')

            # user activation  
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), #hiding pK smiles
                'token' : default_token_generator.make_token(user)  
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect ('/accounts/login/?command=verification&email='+email)

    else:
        form = RegistrationForm()
    context = {
        'form'  :   form
    }
    return render(request, 'accounts/register.html',context)

def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'accounts/login.html', context)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)  
            messages.success(request,'You are now logged in.')
            url = request.META.get('HTTP_REFERER')
            try:
                query  = requests.utils.urlparse(url).query
                # next url confirm before login
                params =  dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
                    
                
            except:
                return redirect ('home')
            
        else:
            messages.error(request,'invalid login credentials')
            return redirect ('login')

    return render(request, 'accounts/login.html',context)

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You have been logged out.')
    return redirect('login')

# email activations
def activate(request,uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request,'Yaay! your account is now activated. Happy Shopping!')
        return redirect('login')
    else:
        messages.error(request,'Invalid activation link')
        return redirect('register')

@login_required(login_url = 'login')
def dashboard(request):
    # userprofile = UserProfile.objects.get(id=request.user.id)
    # # userprofile = get_object_or_404(UserProfile, user=request.user)
    # # orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered = True)
    # # orders_count = orders.count()
   
    # context = {
    #     # 'orders_count':orders_count,
    #     'userprofile' : userprofile,
    # }
    return render (request, 'accounts/dashboard.html')
    # return render (request, 'accounts/dashboard.html',context)

def forgotPassword(request):
    if request.method =='POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            # reset password  
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html',{
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)), #hiding pK smiles
                'token' : default_token_generator.make_token(user)  
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Password reset email has been sent to your email address')
            return  redirect('login')
        else:
            messages.error(request,'Account does not exist!')
            return redirect ('forgotPassword')
    return render(request,'accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid 
        messages.success(request,'Please Reset Your Password')
        return redirect('resetPassword')
    else:
        messages.error(request,'You are using Expired Link')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password  = request.POST['password']
        confirm_password  = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)

            user.set_password(password)
            user.save()
            messages.success(request,'Password reset was successful')
            return redirect('login')

        else:
            messages.error(request,'passwords do not match!')
            return redirect('resetPassword')
    else:
        return render(request,'accounts/resetPassword.html')

# @login_required(login_url='login')
# my invoices
# def my_orders(request):
#     orders = Order.objects.filter(user=request.user,is_ordered=True).order_by('-created_at')
#     context = {
#         'orders':orders,
#     }
#     return render (request,'accounts/my_orders.html',context)

@login_required(login_url='login')
def edit_profile(request):
    userprofile = get_object_or_404(UserProfile, id=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        # profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Your Profile has been updated.")
            return redirect('edit_profile')
    else:
        user_form  = UserForm(instance=request.user)
        # profile_form = UserProfileForm(instance=userprofile)
        profile_form = UserProfileForm(instance=request.user)
        
    # userprofile = UserProfile.objects.all()  
    context = {
        'user_form' :   user_form,
        'profile_form' : profile_form,
        'userprofile':  userprofile,
        
    }       
    return render(request,'accounts/edit_profile.html',context)

@login_required(login_url='login')
def change_password(request):
    # check if request method is Post and receive data from the form
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

    # collect specific user data
        user = Account.objects.get(username__exact=request.user.username)
        # validate user data
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password updated successfully.')
                return redirect ('change_password')
            else:
                messages.error(request,'Enter Valid current password')
                return redirect ('change_password')
        else:
            messages.error(request,'Password does not match')
            return redirect ('change_password')
    return render(request,'accounts/change_password.html')

# @login_required(login_url='login')
# # invoice detail
# def order_detail(request, order_id):
#     order_detail = OrderProduct.objects.filter(order__order_number = order_id)
#     order = Order.objects.get(order_number = order_id)
#     subtotal = 0
#     for i in order_detail:
#         subtotal += i.product_price * i.quantity
#     context = {
#         'order_detail' : order_detail,
#         'order'         : order,
#         'subtotal'      : subtotal,
#     }
#     return render(request,'accounts/order_detail.html',context)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth import views as auth_views

from accounts.forms import (
    CustomPasswordResetForm, 
    CustomSetPasswordForm, 
    CustomUserCreationForm,
    CustomAuthenticationForm)
from accounts.confirm_email import send_email, activate



class SignupView(View):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    initial = {'key': 'value'}

    def get(self,request):
        if not request.user.is_authenticated:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        
        return redirect("profile")


    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            email_sent = send_email(request,user)
            if email_sent:
                
                messages.success(request,
                "Your account has been successfully Created. A confirmation" \
" mail has been sent to your account please follow the necessary precautions in order to"\
" activate your account")
            
            else:
                messages.warning(request,"Something Went Wrong Please Try Again.")

            return redirect("signin")

        return render(request, self.template_name, {'form': form})


class SigninView(View):
    form_class = CustomAuthenticationForm
    template_name = "signin.html"

    initial = {"key":"value"}

    def get(self, request):
        if not request.user.is_authenticated:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form})
        return redirect("index")
    
    def post(self, request):
        if not request.user.is_authenticated:
            if request.method =="POST":
                fm = self.form_class(request=request,data=request.POST)
                if fm.is_valid():
                    user = authenticate(username=fm.cleaned_data['username'],password=fm.cleaned_data['password'])
                    if user is not None:
                        login(request,user)
                        return redirect("index")
            else:      
                fm = self.form_class()
            return render(request,self.template_name,{"form":fm})
        else:
            return redirect("index")


def signout(request):
    logout(request)
    return redirect("signin")


def activate_account(request, uidb64, token):
    activated = activate(uidb64, token)
    if activated:
        messages.success(request,"Your Account Has been Successfully Activated! Login To Continue")
        return redirect("signin")
    
    return render(request, "email/activation_failed.html")


class PasswordResetView(auth_views.PasswordResetView):
    template_name = "password/password_reset.html"
    form_class = CustomPasswordResetForm
    email_template_name = "password/password_reset_email.html"
    html_email_template_name = "password/password_reset_email.html"


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "password/reset_mail_sent.html"
    

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "password/password_reset_confirm.html"
    form_class = CustomSetPasswordForm


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "password/password_reset_complete.html"



def random_email_sender(request):

    from django.conf import settings
    from django.core.mail import send_mail
    from django.template.loader import render_to_string
    from django.utils.html import strip_tags
    from django.contrib.sites.shortcuts import get_current_site

    sender = settings.EMAIL_HOST_USER
    receiver = ["sagar.neupane419@gmail.com"]

    email_subject = "Welcome Email From NepSpeech"

    use_https = request.is_secure()
    current_site = get_current_site(request)
    
    protocol="http"

    if use_https:
        protocol="https"

    email_message = render_to_string("email/congrats_email.html",{
        "domain":current_site,
        "protocol":protocol
        })



    # email_message = render_to_string("email/congrats_email.html",{""})
    message = strip_tags(email_message)
    send_mail(email_subject, message, sender, receiver, html_message=email_message)
    return HttpResponse("<h1>Your Email Has been successfully Sent</h1>")



def dummy_response(request):
    return render(request, "dummy.html")



class ProfileView(View):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name)

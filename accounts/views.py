from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from accounts.models import MyUser
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
                "Your account has been successfully Created.A confirmation" \
"mail has been sent to your account Please follow the precautions in order to"\
"Activate your account")
            
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
        return redirect("profile")
    
    def post(self, request):
        if not request.user.is_authenticated:
            if request.method =="POST":
                fm = self.form_class(request=request,data=request.POST)
                if fm.is_valid():
                    user = authenticate(username=fm.cleaned_data['username'],password=fm.cleaned_data['password'])
                    if user is not None:
                        login(request,user)
                        return redirect("profile")
            else:      
                fm = self.form_class()
            return render(request,self.template_name,{"form":fm})
        else:
            return redirect("profile")


class ProfileView(View):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name)


def signout(request):
    logout(request)
    return redirect("signin")


def activate_account(request, uidb64, token):
    activated = activate(uidb64, token)
    if activated:
        messages.success(request,"Your Account Has been Successfully Activated! Login To Continue")
        return redirect("signin")
    
    return render(request, "activation_failed.html")
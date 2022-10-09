from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage, send_mail

from django.conf import settings

from accounts.tokens import generate_token
from  accounts.models import MyUser


def send_email(request,user):

    # Sending Mail To User
    # Welcome Mail
    subject = "Welcome to NepSpeech!!"
    message = "Hello "+ user.first_name + "!!!\n " \
    + "Welcome to NepSpeech Site\n\n" + \
    "Thank you for visting our site \n "+ \
    "We have sent you a confirmation email.\n"+ \
    "Please verify it in order to activate your account!!\n\n"+ \
    "Thanking you!!! NepSpeech team"

    from_email = settings.EMAIL_HOST_USER
    to_list = [user.email]
    send_mail(subject,message,from_email,to_list,fail_silently=True)

    # # End of Welcome Mail
    # if send_mail(subject,message,from_email,to_list,fail_silently=True):
    #     print("Yes Mail is sent")
    # else:
    #     print("Not Working")

    # Start of Email Confirmation 
    current_site = get_current_site(request)
    email_subject = "Confirmation Email From Auction Bidding!!"
    confirm_message = render_to_string("email_confirmation.html",{
        'name':user.first_name,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user),
    })
    email = EmailMessage(
        email_subject,
        confirm_message,
        from_email,
        to_list,
    )
    email.fail_silently = True
    email_to_sent = email.send()
    
    if email_to_sent:
        return True
    return False


def activate(uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = MyUser.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,MyUser.DoesnotExists):
        user=None 
    
    if user is not None and generate_token.check_token(user,token):
        user.is_active=True 
        user.save()
        return True
    
    return False

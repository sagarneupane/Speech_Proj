from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage, send_mail
from django.utils.html import strip_tags

from django.conf import settings

from accounts.tokens import generate_token
from  accounts.models import MyUser


def send_email(request,user):

    subject = "Welcome From Nepspeech"
    from_email = settings.EMAIL_HOST_USER
    to_list = [user.email]
    html_message = render_to_string("email/congrats_email.html")
    message = strip_tags(html_message)
    send_mail(subject,message,from_email,to_list,html_message=html_message,fail_silently=True)

    current_site = get_current_site(request)
    email_subject = "Confirmation Email From NepSpeech"
    confirm_message = render_to_string("email/emailtemplate.html",{
        'name':user.first_name,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':generate_token.make_token(user),
    })
    message = strip_tags(confirm_message)

    email_to_sent = send_mail(email_subject, message, from_email, to_list, html_message=confirm_message)
    
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

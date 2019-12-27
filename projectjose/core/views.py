import threading
from django.shortcuts import resolve_url
from django.contrib.auth.views import (
    LoginView as LegacyLoginView,
    LogoutView as LegacyLogoutView)
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages
from .mails import Mail
from projectjose.posts.models  import Post


def index(request):
    posts = Post.objects.all()
    return render(request,'core/index.html',{
        'posts':posts
    })

def send_email(name,email,text):
    email = EmailMessage(
        "White House:Nuevo mensaje de contacto",
        "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,text),
        email,
        [settings.EMAIL_HOST_USER],
        reply_to=[email]
    )
    try:
        email.send()
    except:
        messages.error(request,'ocurrio un error, intenta de nuevo.')
        return redirect('core:contact')


def contact(request):
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    text = request.POST.get('text','')
    if request.method == 'POST':
        thread = threading.Thread(target=send_email,args=(name,email,text))
        thread.start()
        messages.success(request,'El mensaje se ha enviado exitosamente.')
        return redirect('core:contact')

    return render(request,'core/contact.html',{})

from django.shortcuts import render


def index(request):
    return render(request,'core/index.html',{})

def contact(request):
    return render(request,'core/contact.html',{})

def post(request):
    return render(request,'core/post.html',{})

def nosotros(request):
    return render(request,'core/nosotros.html',{})

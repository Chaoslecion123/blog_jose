from django.shortcuts import render
from projectjose.services.models import Service

def nosotros(request):
    services = Service.objects.all()
    return render(request,'core/nosotros.html',{
        'services': services
    })

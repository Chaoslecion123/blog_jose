from django.urls import path
from .views import index,contact

urlpatterns = [
    path('',index,name='index'),
    path('contacto/',contact,name='contact'),
]

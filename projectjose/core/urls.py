from django.urls import path
from .views import index,contact,post,nosotros

urlpatterns = [
    path('',index,name='index'),
    path('contacto/',contact,name='contact'),
    path('post/',post,name='post'),
    path('nosotros/',nosotros,name='nosotros'),
]

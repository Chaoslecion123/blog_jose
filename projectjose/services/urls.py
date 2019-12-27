from django.urls import path
from .views import nosotros

urlpatterns = [
    path('',nosotros,name='nosotros'),
]

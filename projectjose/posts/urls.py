from django.urls import path
from .views import PostDetailView

urlpatterns = [
    path('<slug:the_slug>/',PostDetailView.as_view(),name='post-detail')
]

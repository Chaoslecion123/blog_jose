from django.urls import path
from .views import LinkListView,LinkAddView,LinkEditView,LinkDetailView

urlpatterns = [
    path('link/list/',LinkListView.as_view(),name="link-list"),
    path('link/add/',LinkAddView.as_view(),name="link-add"),
    path('link/<int:pk>/edit/',LinkEditView.as_view(),name="link-edit"),
    path('link/<int:pk>/detail/',LinkDetailView.as_view(),name="link-detail")
]

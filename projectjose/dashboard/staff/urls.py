from django.urls import path
from .views import (StaffListView,StaffAddView,StaffEditView,StaffDetailView,StaffDeleteView,
    StaffChangePasswordView)

urlpatterns = [
    path('list/',StaffListView.as_view(),name="staff-list"),
    path('add/',StaffAddView.as_view(),name="staff-add"),
    path('edit/<int:pk>/',StaffEditView.as_view(),name="staff-edit"),
    path('detail/<int:pk>/',StaffDetailView.as_view(),name="staff-detail"),
    path('delete/<int:pk>/',StaffDeleteView.as_view(),name="staff-delete"),
    path(
        'staff/<int:pk>/change-password/',
        StaffChangePasswordView.as_view(),
        name='staff-change-password'
    ),
]

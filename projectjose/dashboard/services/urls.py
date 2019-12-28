from django.urls import path
from .views import (ServieViewList,ServiceAddView,ServiceEditView,ServiceDetailView,
        AttributeServiceAddView,AttributeServiceEditView,AttributeServiceDeleteView,
        ServiceDeleteView)

urlpatterns = [
    path('list/',ServieViewList.as_view(),name='service-list'),
    path('add/',ServiceAddView.as_view(),name='service-add'),
    path('edit/<int:pk>/',ServiceEditView.as_view(),name='service-edit'),
    path('detail/<int:pk>/',ServiceDetailView.as_view(),name='service-detail'),
    path('delete/<int:pk>/',ServiceDeleteView.as_view(),name='service-delete'),

    path('<int:pk>/attribute/add/',AttributeServiceAddView.as_view(),name='service-attribute-add'),
    path(
        '<int:pk>/attribute/<int:attribute_pk>/edit/',
        AttributeServiceEditView.as_view(),
        name='service-attribute-edit'
    ),
    path(
        '<int:pk>/attribute/<int:attribute_pk>/delete/',
        AttributeServiceDeleteView.as_view(),
        name='service-attribute-delete'
    ),
]

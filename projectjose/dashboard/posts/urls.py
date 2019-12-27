from django.urls import path
from .views import (PostListView,PostDetailView,PostAddView,PostEditView,PostDeleteView,
    PostImageAddView,PostImageEditView,PostImageEditView,PostImageDeleteView)

urlpatterns = [
    path('list/',PostListView.as_view(),name='post-list'),
    path('add/',PostAddView.as_view(),name='post-add'),
    path('edit/<int:pk>/',PostEditView.as_view(),name='post-edit'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name='post-delete'),

    path('<int:pk>/image/add/',PostImageAddView.as_view(),name='post-image-add'),
    path(
        '<int:pk>/image/<int:image_pk>/edit/',
        PostImageEditView.as_view(),
        name='post-image-edit'
    ),
    path(
        '<int:pk>/image/<int:image_pk>/delete/',
        PostImageDeleteView.as_view(),
        name='post-image-delete'
    ),
]

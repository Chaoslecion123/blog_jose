"""Main URLs module."""

from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib import admin
from core.urls import urlpatterns as core_urls
from posts.urls import urlpatterns as post_urls
from services.urls import urlpatterns as service_urls
from dashboard.urls import urlpatterns as dashboard_urls

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        '',
        include(
            (
                core_urls,
                'core'
            ),
            namespace='core'
        )

    ),
    path(
        'dashboard/',
        include(
            (
                dashboard_urls,
                'dashboard'
            ),
            namespace='dashboard'
        )
    ),
    path(
        'nosotros/',
        include(
            (
                service_urls,
                'services'
            ),
            namespace='services'
        )

    ),
    path(
        'post/',
        include(
            (
                post_urls,
                'posts'
            ),
            namespace='posts'
        )

    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf.urls import include
from projectjose.dashboard.posts.urls import urlpatterns as posts_url
from projectjose.dashboard.services.urls import urlpatterns as services_url
from projectjose.dashboard.staff.urls import urlpatterns as staff_url
from projectjose.dashboard.social.urls import urlpatterns as social_url
from projectjose.dashboard.core.urls import urlpatterns as core_url


urlpatterns = [
    path(r'posts/',include(posts_url),name='posts'),
    path(r'services/',include(services_url),name='services'),
    path(r'staff/',include(staff_url),name='staff'),
    path(r'social/',include(social_url),name='social'),
    path(r'',include(core_url),name='core'),
]

from django.shortcuts import resolve_url
from django.contrib.auth.views import (
    LoginView as LegacyLoginView,
    LogoutView as LegacyLogoutView)
from django.shortcuts import render, redirect
from django.conf import settings


class LoginView(LegacyLoginView):
    template_name = 'storefront/auth/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        if not self.request.user.is_staff:
            url = resolve_url('dashboard:staff-list')
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)


class LogoutView(LegacyLogoutView):
    next_page = 'core:index'

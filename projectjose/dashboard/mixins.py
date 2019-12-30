from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from projectjose.core.mixins import (
    SearchEnabledViewMixin,
    FilterEnabledViewMixin
)


# class LoginRequiredMixin(AccessMixin):
#     """Verify that the current user is authenticated and is staff or super user."""
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()

#         if request.user.is_authenticated and not (request.user.is_staff or request.user.is_superuser):
#             return self.handle_no_permission()

#         return super().dispatch(request, *args, **kwargs)

#     def handle_no_permission(self):
#         if self.raise_exception or self.request.user.is_authenticated:
#             logout(self.request)
#             raise PermissionDenied(self.get_permission_denied_message())
#         return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


class DashboardMixin(LoginRequiredMixin, SuccessMessageMixin):
    login_url = 'dashboard:login'
    paginate_by = 20
    permission_denied_message = 'No tienes permisos suficientes para ver este contenido'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['google_maps_api_key'] = settings.GEOPOSITION_GOOGLE_MAPS_API_KEY
    #     return context


class DashboardListMixin(DashboardMixin, FilterEnabledViewMixin, SearchEnabledViewMixin):
    pass


class DashboardDeleteMixin(DashboardMixin):
    def get_success_message(self, cleaned_data):
        object_dict = model_to_dict(self.get_object())

        return self.success_message % dict(
            **cleaned_data,
            **object_dict,
        )

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.get_success_message({}))
        return super().delete(request, *args, **kwargs)

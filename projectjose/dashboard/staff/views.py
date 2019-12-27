from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


from projectjose.staff.models import Staff
from .forms import StaffForm,StaffEditForm,StaffChangePasswordForm

class StaffListView(LoginRequiredMixin,SuccessMessageMixin,ListView):
    login_url = 'dashboard:login'
    model = Staff
    template_name = 'dashboard/staff/list.html'
    paginate_by = 20
    search_fileds = [
        'first_name',
        'last_name',
        'is_staff'
        'is_active',
        'is_superuser',
    ]
    return_403 = True
    accept_global_perms = True

class StaffAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'dashboard:login'
    model = Staff
    template_name = 'dashboard/staff/add.html'
    form_class = StaffForm
    success_message = 'El personal "%(username)s" fue creado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:staff-list',
        )

class StaffEditView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'dashboard:login'
    model = Staff
    template_name = 'dashboard/staff/edit.html'
    form_class = StaffEditForm
    success_message = 'El personal "%(username)s" fue modificado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:staff-list',
        )

class StaffDetailView(LoginRequiredMixin,SuccessMessageMixin,DetailView):
    login_url = 'dashboard:login'
    model = Staff
    template_name = 'dashboard/staff/detail.html'

class StaffDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = 'dashboard:login'
    model = Staff
    # template_name = 'dashboard/posts/post_.html'
    success_url = reverse_lazy('dashboard:staff-list')
    success_message = 'El personal "%(username)s" fue eliminado exitosamente.'
    http_method_names = ['post', 'delete']

class StaffChangePasswordView(StaffEditView):
    login_url = 'dashboard:login'
    model = Staff
    template_name = 'dashboard/staff/change-password.html'
    form_class = StaffChangePasswordForm
    success_message = 'La contraseña del usuario fue actualizado exitosamente.'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.get_object()
        })
        return kwargs

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:staff-detail',
            kwargs={
                'pk': self.object.pk
            }
        )

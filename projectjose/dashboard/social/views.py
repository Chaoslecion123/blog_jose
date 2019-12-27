from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404

from projectjose.social.models import Link
from .forms import LinkForm

class LinkListView(SuccessMessageMixin,ListView):
    model = Link
    template_name = 'dashboard/social/link/list.html'

class LinkAddView(SuccessMessageMixin,CreateView):
    model = Link
    template_name = 'dashboard/social/link/add.html'
    form_class = LinkForm
    success_message = 'la Red social "%(name)s" fue creado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:link-list',
        )

class LinkEditView(SuccessMessageMixin,UpdateView):
    model = Link
    template_name = 'dashboard/social/link/edit.html'
    form_class = LinkForm
    success_message = 'La red social "%(name)s" fue actualizado exitosamente.'
    success_url = reverse_lazy('dashboard:link-list')

class LinkDetailView(SuccessMessageMixin,DetailView):
    model = Link
    template_name = 'dashboard/social/link/detail.html'
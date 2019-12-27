from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404


from projectjose.services.models import Service,AttributeService
from .forms import ServiceForm,AttributeServiceForm

class ServieViewList(ListView):
    model = Service
    template_name = 'dashboard/services/list.html'

class ServiceAddView(CreateView):
    model = Service
    template_name = 'dashboard/services/add.html'
    form_class = ServiceForm
    success_message = 'El servicio "%(title)s" fue creado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:service-detail',
            kwargs={
                'pk': self.object.pk
            }
        )

class ServiceEditView(UpdateView):
    model = Service
    template_name = 'dashboard/services/edit.html'
    form_class = ServiceForm
    success_message = 'El servicio "%(title)s" fue actualizado exitosamente.'
    success_url = reverse_lazy('dashboard:service-list')

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'dashboard/services/detail.html'

# ---------------------------------------------------------------------------- #
# Service Attributes Views                                                        #
# ---------------------------------------------------------------------------- #
class AttributeServiceAddView(CreateView):
    model = AttributeService
    template_name = 'dashboard/services/attribute/add.html'
    form_class = AttributeServiceForm
    success_message = 'el atributo del  servicio "%(name)s" ha sido creada exitosamente.'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = get_object_or_404(Service, pk=self.kwargs['pk'])
        context['form'].initial.update({'service': service})
        context['service'] = service
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard:service-detail', args=[self.kwargs['pk']])

class AttributeServiceEditView(UpdateView):
    model = AttributeService
    template_name = 'dashboard/services/attribute/edit.html'
    form_class = AttributeServiceForm
    pk_url_kwarg = 'attribute_pk'
    success_message = 'el atributo del  servicio "%(name)s" ha sido creada exitosamente.'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = get_object_or_404(Service, pk=self.kwargs['pk'])
        context['form'].initial.update({'service': service})
        context['service'] = service
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard:service-detail', args=[self.kwargs['pk']])

class AttributeServiceDeleteView(DeleteView):
    model = AttributeService
    form_class = AttributeServiceForm
    pk_url_kwarg = 'attribute_pk'
    success_message = 'el atributo del  servicio "%(name)s" ha sido creada exitosamente.'
    http_method_names = ['post', 'delete']

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
        )


    def get_success_url(self):
        return reverse_lazy('dashboard:service-detail', args=[self.kwargs['pk']])

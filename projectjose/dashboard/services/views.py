from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.db import transaction
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


from projectjose.services.models import Service,AttributeService
from .forms import ServiceForm,AttributeServiceForm

class ServieViewList(LoginRequiredMixin,SuccessMessageMixin,ListView):
    login_url = 'dashboard:login'
    model = Service
    template_name = 'dashboard/services/list.html'

class ServiceAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'dashboard:login'
    model = Service
    form_class = ServiceForm
    template_name = 'dashboard/services/add.html'
    success_message = 'El servicio "%(title)s" fue creado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:service-detail',
            kwargs={
                'pk': self.object.pk
            }
        )

    # def get_context_data(self, **kwargs):
    #     self.object = None
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ServiceForm(
    #         self.request.POST or None, self.request.FILES or None
    #     )

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     form = context['form']

    #     with transaction.atomic():
    #         form.instance = form.instance
    #         if form.is_valid():
    #             self.object = form.save()
    #         else:
    #             return self.render_to_response(context)

    #     return HttpResponseRedirect(self.get_success_url())

class ServiceEditView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'dashboard:login'
    model = Service
    template_name = 'dashboard/services/edit.html'
    form_class = ServiceForm
    success_message = 'El servicio "%(title)s" fue actualizado exitosamente.'
    success_url = reverse_lazy('dashboard:service-list')

class ServiceDetailView(LoginRequiredMixin,SuccessMessageMixin,DetailView):
    login_url = 'dashboard:login'
    model = Service
    template_name = 'dashboard/services/detail.html'

class ServiceDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = 'dashboard:login'
    model = Service
    # template_name = 'dashboard/posts/post_.html'
    success_url = reverse_lazy('dashboard:service-list')
    success_message = 'El servicio "%(title)s" fue eliminado exitosamente.'
    http_method_names = ['post', 'delete']

# ---------------------------------------------------------------------------- #
# Service Attributes Views                                                        #
# ---------------------------------------------------------------------------- #
class AttributeServiceAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'dashboard:login'
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

class AttributeServiceEditView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'dashboard:login'
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

class AttributeServiceDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = 'dashboard:login'
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

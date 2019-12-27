from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin



from projectjose.posts.models  import Post,PostImage
from .forms import PostForm,PostImageForm


class PostListView(LoginRequiredMixin,SuccessMessageMixin,ListView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/posts/list.html'

class PostAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/posts/add.html'
    form_class = PostForm
    success_message = 'El proyecto "%(title)s" fue creado exitosamente.'

    def get_success_url(self):
        return reverse_lazy(
            'dashboard:post-detail',
            kwargs={
                'pk': self.object.pk
            }
        )

class PostEditView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/posts/edit.html'
    form_class = PostForm
    success_message = 'El proyecto "%(title)s" fue actualizado exitosamente.'
    success_url = reverse_lazy('dashboard:post-list')

class PostDetailView(LoginRequiredMixin,SuccessMessageMixin,DetailView):
    login_url = 'dashboard:login'
    model = Post
    template_name = 'dashboard/posts/detail.html'

class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = 'dashboard:login'
    model = Post
    # template_name = 'dashboard/posts/post_.html'
    success_url = reverse_lazy('dashboard:post-list')
    success_message = 'El proyecto "%(title)s" fue eliminado exitosamente.'
    http_method_names = ['post', 'delete']


# ---------------------------------------------------------------------------- #
# Post Images Views                                                            #
# ---------------------------------------------------------------------------- #
class PostImageAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = 'dashboard:login'
    model = PostImage
    template_name = 'dashboard/posts/image/add.html'
    form_class = PostImageForm
    success_message = 'La imagen para el proyecto "%(post_title)s" ha sido creada exitosamente.'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            post_title=self.object.post.title,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['form'].initial.update({'post': post})
        context['post'] = post
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard:post-detail', args=[self.kwargs['pk']])

class PostImageEditView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = 'dashboard:login'
    model = PostImage
    template_name = 'dashboard/posts/image/edit.html'
    form_class = PostImageForm
    pk_url_kwarg = 'image_pk'
    success_message = 'La imagen del proyecto "%(post_title)s" ha sido actualizada exitosamente.'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            post_title=self.object.post.title,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['post'] = post
        return context

    def get_success_url(self):
        return reverse_lazy('dashboard:post-detail', args=[self.kwargs['pk']])

class PostImageDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = 'dashboard:login'
    model = PostImage
    form_class = PostImageForm
    pk_url_kwarg = 'image_pk'
    success_message = 'La imagen del proyecto "%(post_title)s" ha sido eliminada exitosamente.'
    http_method_names = ['post', 'delete']

    def get_success_message(self, cleaned_data):
        post = Post.objects.filter(pk=self.kwargs['pk']).first()

        return self.success_message % dict(
            cleaned_data,
            post_title=post.title,
        )

    def get_success_url(self):
        return reverse_lazy('dashboard:post-detail', args=[self.kwargs['pk']])

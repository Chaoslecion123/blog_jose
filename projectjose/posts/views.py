from django.shortcuts import render
from django.views.generic.detail import DetailView
from projectjose.posts.models  import Post


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'the_slug'
    template_name = 'core/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

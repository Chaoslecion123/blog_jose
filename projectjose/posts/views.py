from django.shortcuts import render
from django.views.generic.detail import DetailView
from projectjose.posts.models  import Post


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'the_slug'
    template_name = 'core/post.html'

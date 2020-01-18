from django.shortcuts import render
from django.views.generic import DetailView

# Models
from posts.models import Post

class PostDetail(DetailView):
    """Detail post."""
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'
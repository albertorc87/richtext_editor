"""Posts models."""

# Django
import os
from django.db import models


from django.utils.text import slugify
from django.contrib.auth.models import User


# django-ckeditor
from ckeditor.fields import RichTextField


class Post(models.Model):
    """Post model."""
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    url = models.SlugField(max_length=255, unique=True)


    class Meta:
        ordering = ('title',)


    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
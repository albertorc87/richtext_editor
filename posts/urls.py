"""Posts URLs."""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='posts/<slug:url>/',
        view=views.PostDetail.as_view(),
        name='detail'
    ),
]

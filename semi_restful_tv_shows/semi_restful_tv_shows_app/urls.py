from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>', views.view)
]

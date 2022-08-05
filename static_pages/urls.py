# static_pages URLS

from django.urls import path
from . import views

app_name = 'static_pages'

urlpatterns = [
    path('', views.home_view, name='home'),
]
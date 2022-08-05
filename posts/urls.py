from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.post_create_view, name='create'),
    path('detail/<int:pk>/', views.post_detail_view, name='detail'),
    path('list/', views.post_list_view, name='list'),
    path('update/<int:pk>/', views.post_update_view, name='update'),
    path('delete/<int:pk>/', views.post_delete_view, name='delete'),
]
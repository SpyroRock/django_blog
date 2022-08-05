from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.user_create_view, name="create"),
    path('login/', views.user_login_view, name="login"),
    path('logout/', views.user_logout_view, name="logout"),
    path('<str:username>/', views.user_profile_view, name="profile"), 
]
from django.urls import path
from .views import login_page, register_page, RegisterView, LoginView

urlpatterns = [
    path('login/', login_page, name='login'),  # Render login page
    path('register/', register_page, name='register'),  # Render register page
    path('api/users/register/', RegisterView.as_view(), name='api_register'),  # API for registration
    path('api/users/login/', LoginView.as_view(), name='api_login'),  # API for login
]   


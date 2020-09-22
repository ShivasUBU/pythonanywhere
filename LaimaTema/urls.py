from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='LaimaTema/loginbox.html'), name='home'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]

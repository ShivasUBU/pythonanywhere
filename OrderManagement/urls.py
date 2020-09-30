from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('Profile', views.profile, name='Profile'),
    path('add', views.addorder, name='AddOrder'),
    path('search', views.searchorder, name='SearchOrder'),
    path('waitsend', views.waitsendorder, name='WaitSendOrder'),
    path('AllOrder', views.allorder, name='AllOrder'),
    path('Order/<int:id>/', views.orderdetail, name='OrderDetail'),
]

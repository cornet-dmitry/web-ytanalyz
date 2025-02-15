from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_list, name='clients_list'),  # Основной URL для списка клиентов
    path('add/', views.add_client, name='add_client'),  # URL для добавления клиента
    path('<int:client_id>/', views.client_detail, name='client_detail'),  # Подробнее о клиенте
]
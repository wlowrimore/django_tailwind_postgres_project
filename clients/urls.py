from django.urls import path
from .views import view_clients, create_client

urlpatterns = [
    path('', view_clients, name='view_clients'),
    path('create_client', create_client, name='create_client')
]
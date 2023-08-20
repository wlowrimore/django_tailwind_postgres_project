from django.urls import path
from .views import view_clients

urlpatterns = [
    path('', view_clients, name='view_clients'),
]
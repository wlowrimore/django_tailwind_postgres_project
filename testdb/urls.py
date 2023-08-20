from django.urls import path
from .views import index, logout_user, register_user

urlpatterns = [
    path("", index, name="home"),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register')
]

from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "address1", "address2", "city", "state", "zipcode", "email", "phone", "notes"]


admin.site.register(Client)

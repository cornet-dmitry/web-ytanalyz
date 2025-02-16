from django.contrib import admin
from .models import Clients, ClientsStatus, UsersClients, FullVideos


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'project_name', 'city', 'contact', 'start_date', 'status')
    list_filter = ('status', 'city')
    search_fields = ('client_name', 'project_name', 'contact')


@admin.register(ClientsStatus)
class ClientsStatusAdmin(admin.ModelAdmin):
    list_display = ('status_name',)


@admin.register(UsersClients)
class UsersClientsAdmin(admin.ModelAdmin):
    list_display = ('users', 'clients')
    list_filter = ('users', 'clients')
    search_fields = ('users__username', 'clients__project_name')
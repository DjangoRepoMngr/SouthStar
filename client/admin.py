from django.contrib import admin
from .models import client, route, client_buy, SupervisorVisitorRelationship

admin.site.register(client)
admin.site.register(route)
admin.site.register(client_buy)
admin.site.register(SupervisorVisitorRelationship)

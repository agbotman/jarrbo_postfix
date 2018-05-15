from django.contrib import admin
from .models import *

class VirtualAliasAdmin(admin.ModelAdmin):
	list_display = ('domain', 'source', 'destination', 'description')
	list_editable = ('description',)

admin.site.register(VirtualDomain)
admin.site.register(VirtualUser)
admin.site.register(VirtualAlias, VirtualAliasAdmin)

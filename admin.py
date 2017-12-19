from django.contrib import admin
from .models import *

admin.site.register(VirtualDomain)
admin.site.register(VirtualUser)
admin.site.register(VirtualAlias)

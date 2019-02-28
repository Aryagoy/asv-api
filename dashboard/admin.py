from django.contrib import admin

# Register your models here.
from .models import Horizon, Scan


admin.site.register(Horizon)
admin.site.register(Scan)

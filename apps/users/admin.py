from django.contrib import admin
from .models import Location, Profile, CustomServices, ServiceProvider

# Register your models here.
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(CustomServices)
admin.site.register(ServiceProvider)
from django.contrib import admin
from .models import Profile, Location

# # Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','address_name','user', 'country','city']
    
# register profile for User
admin.site.register(Profile)

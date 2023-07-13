from django.contrib import admin
from .models import Location, Profile, CustomServices, ServiceProvider, ChangeEmail

# Register your models here.
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'country','city']
    
    
@admin.register(CustomServices)
class CustomServicesAdmin(admin.ModelAdmin):
    list_display = ['id','request_by', 'name','category','request_date', 'location']
    
    
admin.site.register(Profile)

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['name','location','phone_number', 'category','year_experience','summary_experience']
    
    
admin.site.register(ChangeEmail)
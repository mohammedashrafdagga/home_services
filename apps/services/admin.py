from django.contrib import admin

from .models import Category, Services, IncludeServices, NotIncludeServices

class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        slug = str(obj.name).replace(' ', '-')
        obj.slug = f'قسم-{slug}'
        super().save_model(request, obj, form, change)


# register into admin
admin.site.register(Category, CategoryAdmin)


class IncludeServicesAdmin(admin.TabularInline):
    model =  IncludeServices
    extra = 2
    
    
class NotIncludeServicesAdmin(admin.TabularInline):
    model =  NotIncludeServices
    extra = 2
    

# Services Admin
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'slug']
    inlines = [IncludeServicesAdmin, NotIncludeServicesAdmin]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        slug = str(obj.name).replace(' ', '-')
        obj.slug = f'خدمة-{slug}'
        super().save_model(request, obj, form, change)


# register into admin
admin.site.register(Services, ServicesAdmin)


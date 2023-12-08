from django.contrib import admin
from .models import RecentProjects, ClientFeedback, interiorProjects, designProjects, residentialProjects, commercialProjects, Properties, ClientForm

class AutoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug') # adding columns 
    # list_filter = ('', ) # Adding filters
    prepopulated_fields = {'slug': ('title', )}
    
class clientsAdmin(admin.ModelAdmin):
    list_display = ('clientName', 'clientDesignation', 'slide') # adding columns 
    list_filter = ('rating', ) # Adding filters

class formAdmin(admin.ModelAdmin):
    list_display = ('name', 'email') # adding columns 
    
class propertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug') # adding columns 
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('category', ) # Adding filters

# Register your models here.
admin.site.register(RecentProjects, AutoAdmin)
admin.site.register(ClientFeedback, clientsAdmin)
admin.site.register(interiorProjects, AutoAdmin)
admin.site.register(designProjects, AutoAdmin)
admin.site.register(residentialProjects, AutoAdmin)
admin.site.register(commercialProjects, AutoAdmin)
admin.site.register(Properties, propertyAdmin)
admin.site.register(ClientForm, formAdmin)


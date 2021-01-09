from django.contrib import admin
from .models import Bepcar2020, Bepcar2019, Bepcar2018, Bepcar2017, Bepcar2016, Bepcar2015
# Register your models here.
admin.site.register(Bepcar2020)
admin.site.register(Bepcar2019)
admin.site.register(Bepcar2018)
admin.site.register(Bepcar2017)
admin.site.register(Bepcar2016)
admin.site.register(Bepcar2015)
# class ProfileAdmin(admin.ModelAdmin):
# 	list_display = ('user', 'title', 'image', 'bio', 'location', 'phone_number')

# admin.site.register(Profile, ProfileAdmin)
from import_export.admin import ImportExportModelAdmin
    # from django.contrib import admin
    # from .models import Blog
    
    # class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #     ...
        
    # admin.site.register(Blog, BlogAdmin)  
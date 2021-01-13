from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Bepcar2020, Bepcar2019, Bepcar2018, Bepcar2017, Bepcar2016, Bepcar2015
# Register your models here.

# from django_summernote.admin import SummernoteModelAdmin
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('text',)

# admin.site.register(Post, PostAdmin)

class ArAdmin(admin.ModelAdmin):
	list_display = ('title', 'status','brevet')
admin.site.register(Bepcar2020, ArAdmin)
admin.site.register(Bepcar2019, ArAdmin)
admin.site.register(Bepcar2018, ArAdmin)
admin.site.register(Bepcar2017, ArAdmin)
admin.site.register(Bepcar2016, ArAdmin)
admin.site.register(Bepcar2015, ArAdmin)
# admin.site.register(Profile, ProfileAdmin)

    # from django.contrib import admin
    # from .models import Blog
    
    # class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #     ...
        
    # admin.site.register(Blog, BlogAdmin)  
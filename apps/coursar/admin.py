from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Brevet_Ar
from .models import Cours_Ar
from .models import Cours_Ar_T
# Register your models here.

# from django_summernote.admin import SummernoteModelAdmin
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('text',)

# admin.site.register(Post, PostAdmin)

class ArAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('title', 'status','create')
admin.site.register(Brevet_Ar, ArAdmin)
admin.site.register(Cours_Ar, ArAdmin)
admin.site.register(Cours_Ar_T)
# admin.site.register(Profile, ProfileAdmin)

    # from django.contrib import admin
    # from .models import Blog
    
    # class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #     ...
        
    # admin.site.register(Blog, BlogAdmin)  
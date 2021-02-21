from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_summernote.admin import SummernoteModelAdmin
from .models import Brevet_Fr
from .models import Cours_Fr
from .models import Cours_Fr_T
# Register your models here.
# admin_site_header ='welcom'
class FrAdmin(ImportExportModelAdmin,SummernoteModelAdmin,admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title','status','create')
    
admin.site.register(Brevet_Fr, FrAdmin)
admin.site.register(Cours_Fr, FrAdmin)
admin.site.register(Cours_Fr_T)
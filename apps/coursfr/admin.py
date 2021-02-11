from django.contrib import admin
from .models import Brevet_Fr
from .models import Cours_Fr
from .models import Cours_Fr_T
# Register your models here.
class FrAdmin(admin.ModelAdmin):
    list_display = ('title','status','create')

admin.site.register(Brevet_Fr, FrAdmin)
admin.site.register(Cours_Fr, FrAdmin)
admin.site.register(Cours_Fr_T)
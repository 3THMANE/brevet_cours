from django.contrib import admin
from .models import Bepcfr2020, Bepcfr2019, Bepcfr2018, Bepcfr2017, Bepcfr2016, Bepcfr2015
# Register your models here.
class FrAdmin(admin.ModelAdmin):
    list_display = ('title','status','brevet')

admin.site.register(Bepcfr2020, FrAdmin)
admin.site.register(Bepcfr2019, FrAdmin)
admin.site.register(Bepcfr2018, FrAdmin)
admin.site.register(Bepcfr2017, FrAdmin)
admin.site.register(Bepcfr2016, FrAdmin)
admin.site.register(Bepcfr2015, FrAdmin)
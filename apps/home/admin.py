from django.contrib import admin

# from django_summernote.admin import SummernoteModelAdmin
# from apps.coursar.models import Coursar, Coursesar
from .models import Contact


# from .models import Coursfr
# Register your models here.



# class CoursarAdmin(SummernoteModelAdmin):
    # summernote_fields = '__all__'

# admin.site.register(Coursar)
# admin.site.register(Coursesar)
# class CoursfrAdmin(SummernoteModelAdmin):
    # summernote_fields = '__all__'

admin.site.register(Contact)
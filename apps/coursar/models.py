from django.db import models
# from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _
# brevet your models here.
STATUS = (('draft', 'إخفاء'),
          ('published', 'نشر'))
class Brevet_Ar(models.Model):
    C_brevet_ar = (
          ('brevet_ar_20', 'بريفة 20'),
          ('brevet_ar_19', 'بريفة 19'),
          ('brevet_ar_18', 'بريفة 18'),
          ('brevet_ar_17', 'بريفة 17'),
          ('brevet_ar_16', 'بريفة 16'),
          ('brevet_ar_15', 'بريفة 15')
          )
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField()
    create = models.IntegerField(_("تاريخ مسابقة"), null=True, blank=True)
    select_brevet = models.CharField(_("اختر المسابقة"), max_length=20, choices=C_brevet_ar)
    status = models.CharField(_("الحالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Brevet_Ar'
        verbose_name_plural = 'Brevet_Ar'

class Cours_Ar_T(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(_("العنوان"),    max_length=200, unique=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'c_ar_title'
        verbose_name_plural = 'c_ar_title'
class Cours_Ar(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    title =models.CharField(_("العنوان"),    max_length=200, unique=True)
    text = models.TextField(_("المنشور"))
    Lesson = models.ForeignKey('Cours_Ar_T', related_name='الدروس', on_delete=models.CASCADE)
    create = models.DateTimeField(_("تاريخ"), auto_now_add=True)
    status = models.CharField(_("الحالة"), max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'cours_ar'
        verbose_name_plural = 'cours_ar'
        

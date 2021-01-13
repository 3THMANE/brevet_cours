from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import ugettext_lazy as _
# brevet your models here.
STATUS = (('draft', 'إخفاء'),
          ('published', 'نشر'))
class Bepcar2020(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = HTMLField()
    brevet = models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_AR_2020'
        verbose_name_plural = 'BEPC_AR_2020'

class Bepcar2019(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField(_("النص"))
    brevet = models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_AR_2019'
        verbose_name_plural = 'BEPC_AR_2019'

class Bepcar2018(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField(_("النص"))
    brevet = models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'BEPC_AR_2018'
        verbose_name_plural = 'BEPC_AR_2018'

class Bepcar2017(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField(_("النص"))
    brevet = models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_AR_2017'
        verbose_name_plural = 'BEPC_AR_2017'

class Bepcar2016(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField(_("النص"))
    brevet = models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_AR_2016'
        verbose_name_plural = 'BEPC_AR_2016'

class Bepcar2015(models.Model):
    id = models.AutoField(primary_key=True)  
    # cours = models.ForeignKey(Coursesar, on_delete=models.CASCADE)
    slug = models.CharField(_("رابط"),     max_length=100, unique=True)
    name =models.CharField(_("المادة"),    max_length=200, unique=True)
    title =models.CharField(_("الموضوع"),  max_length=200, unique=True)
    text = models.TextField(_("النص"))
    brevet =models.IntegerField(_("مسابقة"), null=True, blank=True)
    status = models.CharField(_("حالة"),   max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_AR_2015'
        verbose_name_plural = 'BEPC_AR_2015'

from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
STATUS = (('draft', 'Draft'),
          ('published', 'Published'))
class Bepcfr2020(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_FR_2020'
        verbose_name_plural = 'BEPC_FR_2020'
        
class Bepcfr2019(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'BEPC_FR_2019'
        verbose_name_plural = 'BEPC_FR_2019'

class Bepcfr2018(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_FR_2018'
        verbose_name_plural = 'BEPC_FR_2018'

class Bepcfr2017(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_FR_2017'
        verbose_name_plural = 'BEPC_FR_2017'

class Bepcfr2016(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'BEPC_FR_2016'
        verbose_name_plural = 'BEPC_FR_2016'

class Bepcfr2015(models.Model):
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    create = models.DateField(_("brevet"), auto_now_add=False, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BEPC_FR_2015'
        verbose_name_plural = 'BEPC_FR_2015'
from django.db import models
from django.utils.translation import ugettext_lazy as _
# brevet your models here.
STATUS = (('draft', 'Draft'),
          ('published', 'Published'))
class Brevet_Fr(models.Model):
    C_brevet_fr = (
          ('brevet_fr_20', 'brevet 20'),
          ('brevet_fr_19', 'brevet 19'),
          ('brevet_fr_18', 'brevet 18'),
          ('brevet_fr_17', 'brevet 17'),
          ('brevet_fr_16', 'brevet 16'),
          ('brevet_fr_15', 'brevet 15')
          )
    id = models.AutoField(primary_key=True)  
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    name =models.CharField(_("subject"),   max_length=200, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    shor = models.CharField(_("short disc"), max_length=300)
    create = models.IntegerField(_("brevet date"), null=True, blank=True)
    select_brevet = models.CharField(_("choice brevet"), max_length=20, choices=C_brevet_fr)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Brevet_Fr'
        verbose_name_plural = 'Brevet_Fr'
        

class Cours_Fr_T(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'C_Fr_Title'
        verbose_name_plural = 'C_Fr_Title'
class Cours_Fr(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(_("Slug"),     max_length=100, unique=True)
    title =models.CharField(_("Titel"),    max_length=200, unique=True)
    text = models.TextField(_("Post"))
    shor = models.CharField(_("short disc"), max_length=300)
    Lesson = models.ForeignKey('Cours_Fr_T', related_name='Lesson', on_delete=models.CASCADE)
    create = models.DateTimeField(_("date"), auto_now_add=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS, default='draft')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cours_Fr'
        verbose_name_plural = 'Cours_Fr'
        

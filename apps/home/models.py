from django.db import models
# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField( max_length=50, null=True)
    phone = models.CharField( max_length=12, null=True, blank=True)
    email = models.CharField( max_length=50, null=True, blank=True)
    message = models.TextField() 
    time = models.DateTimeField( auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.name)
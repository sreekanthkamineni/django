from django.db import models

# Create your models here.

class Url_list(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
      
    class Meta:
        db_table = 'url_list'
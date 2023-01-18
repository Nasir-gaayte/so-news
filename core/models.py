from django.db import models
from django.forms.widgets import NumberInput
import datetime


# Create your models here.


class TicketModel(models.Model):
    CITY = {
        ('bosaso to qardho', 'bosaaso to qardho'),
        ('bosaso to garowe', 'bosaaso to gaowe'),
        ('bosaso to galkacyo', 'bosaso to galkacyo'),
        ('bosaso to lascano', 'bosaso to lascano'),
        ('non', 'non')
    }

    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    to = models.CharField('toto', max_length=255, choices=CITY, default='non')
    date = models.DateField(auto_now_add=True)
    go_date = models.DateField()
    cost = models.CharField(max_length=255)

    def __str__(self) :
        return self.name + self.cost
    
    
class AdvertModel(models.Model):
        name = models.CharField(max_length=200, blank=True, null=True)
        title = models.CharField(max_length=50,blank=True, null=True)
        image = models.ImageField(blank=True,null=True,upload_to='advert')
        desc = models.TextField(300, blank=True, null=True)
        url = models.URLField()
        
        
        
        def __str__(self):
            return self.name
        
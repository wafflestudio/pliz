from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.
class Errand(models.Model):
    CATEGORY_CHOICES = (
        ("DELIVERY","Delivery"),
        ("HOMEWORK","Homework"),
        ("ERRAND","Errand"),
        ("ETC","Etc"),
    )
    owner = models.ForeignKey(User, related_name='errand', null=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='Blank Title')
    text = models.TextField()
    extraCost = models.PositiveIntegerField()
    reward = models.PositiveIntegerField()
    category = models.CharField(max_length=10, 
            choices=CATEGORY_CHOICES, 
            default="DELIVERY" )
    class Meta:
        ordering = ('created',)
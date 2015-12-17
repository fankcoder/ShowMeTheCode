'''
from django.db import models

# Create your models here.
class comdata(models.Model):
    name = models.CharField(max_length=20)
    comments = models.CharField(max_length=2000)
    create_time = models.DateTimeField(auto_now_add=True)
'''

from django.db import models
#from dango.forms import ModelForm

class CommentData(models.Model):
    name = models.CharField(max_length=20)
    comments = models.CharField(max_length=1200)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__():
        return self.name

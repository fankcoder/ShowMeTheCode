from django.db import models

# Create your models here.
class comdata(models.Model):
    name = models.CharField(max_length=20)
    comments = models.CharField(max_length=2000)
    create_time = models.DateTimeField(auto_now_add=True)

from django.forms import CommentFrom

class ConnectForm(CommentFrom):
    class Meta:
        model = comdata
        fields = ('name', 'comments')

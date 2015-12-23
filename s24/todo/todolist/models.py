from django.db import models

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)

    levelist = (
            (0,'green'),
            (1,'blue'),
            (2,'yellow'),
            (3,'red'),
            )

    level = models.IntegerField(default=0, choices=levelist)

    def __unicode__():
        return self.name

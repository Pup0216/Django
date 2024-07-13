from django.db import models

# Create your models here.
class Publication( models.Model ):
    title = models.CharField(max_length=50)
    content = models.TextField()
    visible = models.BooleanField(default=True)
    
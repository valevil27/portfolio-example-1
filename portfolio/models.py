from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description =models.TextField()
    image = models.ImageField()
    # auto_now_add is executed only on creation
    created = models.DateTimeField(auto_now_add=True)
    # auto_now is executed when we update the model
    updated = models.DateTimeField(auto_now=True)
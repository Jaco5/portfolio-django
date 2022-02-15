from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    hosted = models.URLField(default="www.github.com")
#    image = models.FilePathField(path="/img")

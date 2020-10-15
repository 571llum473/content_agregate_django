from django.db import models

# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

class News(models.Model):
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    news_text = models.CharField(max_length=200)
from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField("id", 'id', True)
    title = models.CharField("title", 'title', max_length=100)

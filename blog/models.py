from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Wanted(models.Model):
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.position
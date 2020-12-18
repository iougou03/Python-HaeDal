from django.db import models

# Create your models here.
class LectureList(models.Model):
    youtube_url = models.URLField(max_length=200)
    title = models.CharField(max_length=50,default='')
    content = models.TextField(default='')

    def __str__(self):
        return self.title


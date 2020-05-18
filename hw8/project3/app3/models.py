from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class News(models.Model)
    headline = models.CharField(max_length = 100)
    content = models.TextField()
    reporter = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'news_images/')

    class Meta:
        ordering = ['-date_reported']

    def __str__(self):
        return self.headline
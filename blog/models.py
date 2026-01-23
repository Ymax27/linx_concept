from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
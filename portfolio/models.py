from django.db import models

# Create your models here.
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('WEB', 'Developpement web'),
        ('GRAPHIC', 'Design graphique'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    
    live_url = models.URLField(blank=True, null=True, help_text="Lien vers le site")
    github_url = models.URLField(blank=True, null=True, help_text="Lien vers le Github")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message de {self.name}"
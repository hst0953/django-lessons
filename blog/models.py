from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    #full_text = models.TextField()
    full_text = RichTextField(blank=True, null=True)
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique = True) 
    # is_published = models.BooleanField() #TODO

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug' : self.slug})
    
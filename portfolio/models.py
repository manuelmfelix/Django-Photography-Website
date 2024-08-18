from django.db import models
from django.urls import reverse
from django.utils.html import linebreaks

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    camera = models.TextField(null=True, blank=True)
    lens = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Convert plain text newlines to HTML paragraphs if needed
        if self.description:
            self.description = linebreaks(self.description)
        super(Catalog, self).save(*args, **kwargs)
    
    def cover_image(self):
        cover_photo = self.photo_set.filter(is_cover_image=True).first()
        if cover_photo:
            return cover_photo.image.url
        return None


class Photo(models.Model):
    index = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/photos/')
    description = models.TextField(null=True, blank=True)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, default=0)
    exposure = models.CharField(max_length=100,null=True, blank=True)
    focal_distance = models.CharField(max_length=100,null=True, blank=True)
    iso = models.IntegerField(null=True, blank=True)
    is_cover_image = models.BooleanField(default=False)


    def __str__(self):
        return self.title
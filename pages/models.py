from django.db import models

# Create your models here.
class Teams(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100, null=True, blank=True)
    twitter_link = models.URLField(max_length=100, null=True, blank=True)
    google_link = models.URLField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Teams'
    
    def __str__(self):
        return self.first_name 
     
    
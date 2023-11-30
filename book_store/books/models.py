from django.db import models
from django.urls import reverse
from jupyterlab_server import slugify
# Create your models here.
class Boooks(models.Model):
    title=models.CharField(max_length=100)
    pages=models.IntegerField(default=0)
    rating=models.IntegerField(max_length=125,null=True)
    slug=models.SlugField(null=True, default="",db_index=True)
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title}, {self.pages}"
    
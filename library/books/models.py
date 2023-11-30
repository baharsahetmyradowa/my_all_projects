from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
  
    rating=models.IntegerField(validators=[
        MinValueValidator(1),MaxValueValidator(10)
    ])
    author=models.CharField(max_length=15)
    is_bestseller=models.BooleanField(default=False)
    slug=models.SlugField(null=False,blank=True)

    def __str__(self):
        return f"{self.author} {self.author}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.author)
        super().save(*args,**kwargs)

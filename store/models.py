from django.db import models
from category.models import category
from django.urls import reverse
# class AvailableSize(models.Model):
#     SMALL = 'S'
#     MEDIUM = 'M'
#     LARGE = 'L'
#     EXTRA_LARGE = 'XL'

#     SIZE_CHOICES = [
#         (SMALL, 'Small'),
#         (MEDIUM, 'Medium'),
#         (LARGE, 'Large'),
#         (EXTRA_LARGE, 'Extra Large'),
#     ]
    
#     size = models.CharField(max_length=2, choices=SIZE_CHOICES)
#     price = models.DecimalField(max_digits=10,decimal_places=2)

#     def __str__(self):
#         return dict(self.SIZE_CHOICES)[self.size]

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    description = models.TextField(max_length=500,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    # availabel_size = models.ManyToManyField(AvailableSize)
    images = models.ImageField(upload_to='photos/product',)
    stock = models.IntegerField()
    is_avaiable = models.BooleanField()
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name
    


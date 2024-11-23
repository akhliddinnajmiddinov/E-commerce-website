from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    num_available = models.IntegerField(default=1)
    parent_product = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True, null=True)

    
    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        
        super().save(*args, **kwargs)
    
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/',blank=True, null=True)


    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)
        
        super().save(*args, **kwargs)
    
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGB")
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)
        
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


    def __str__(self):
        return self.product.title
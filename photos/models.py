from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=60)
    image_description = models.CharField(max_length=200,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE,)
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE,)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def filter_by_location(cls,search_term):
        images = Image.objects.filter(image_location_id=search_term).all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        image = Image.objects.filter(image_category__category__icontains=search_term).all()
        return image

class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
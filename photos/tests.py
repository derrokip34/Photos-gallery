from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTest(TestCase):

    def setUp(self):
        self.gotham = Location(location='Gotham')
        self.gotham.save_location()

        self.batman = Category(category='Movie')
        self.batman.save_category()

        self.batman_image = Image(image='the_bat.jpg',image_name='The Batman',image_description='A photo of Batman fighting The Joker in Gotham(The Dark Knight)',date_posted='2020-05-24',image_category=self.batman,image_location=self.gotham)
        self.batman_image.save_image()

    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.batman_image, Image))

    def test_save_image_method(self):
        self.batman_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        self.batman_image.save_image()
        image = Image.get_image_by_id(1)
        self.assertTrue(len(image)==0)

class LocationTest(TestCase):
    def setUp(self):
        self.brooklyn = Location(location='Brooklyn')
        self.brooklyn.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.brooklyn, Location))

    def test_save_location_method(self):
        self.brooklyn.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

class CategoryTest(TestCase):
    def setUp(self):
        self.tv_show = Category(category='Tv Show')
        self.tv_show.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.tv_show, Category))

    def test_save_category_method(self):
        self.tv_show.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)
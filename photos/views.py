from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def all_photos(request):

    images = Image.get_all_images()
    return render(request, 'all_photos/photos.html',{'images':images})
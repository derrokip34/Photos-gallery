from django.shortcuts import render
from .models import Image,Location,Category
from django.http import Http404

# Create your views here.
def welcome(request):
    return render(request,'index.html')

def all_photos(request):

    images = Image.get_all_images()
    return render(request, 'all_photos/photos.html',{'images':images})

def search_images_by_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'all_photos/search.html',{"message":message,"images":searched_images})
    else:
        message="No category searched"
        return render(request,'all_photos/search.html',{"message":message})
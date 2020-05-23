from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^photos/',views.all_photos,name='all_photos'),
    url(r'^search/',views.search_images_by_category,name='search_images'),
    path('location/<int:location>',views.filter_by_locations,name="locations")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
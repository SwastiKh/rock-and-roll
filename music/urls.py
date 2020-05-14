from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="Music"

urlpatterns = [
    path('', views.index, name='index'),
    
]

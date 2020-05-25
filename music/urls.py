from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name='music'

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    
    #/music/71/
    # url(r'^?P<album_id>[0-9]+)/$', views.detail, name='detail'')
    path('<int:album_id>/', views.detail, name='detail'),

    #/music/<album_id>/favorite/
    path('<int:album_id>/favorite/', views.favorite, name='favorite')
]

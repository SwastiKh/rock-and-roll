from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name='music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    
    #/music/71/
    # url(r'^?P<album_id>[0-9]+)/$', views.detail, name='detail'')
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    #/music/album/2/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/2/delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]

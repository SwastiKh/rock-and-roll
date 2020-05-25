#from django.http import Http404 
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.template import loader
from .models import Album

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    #context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', {'all_albums' : all_albums})

    #html = ''
    #for album in all_albums:
    #    path = 'music/' + str(album_id) + '/'
    #    html += '<a href="' + path + '">' + album.album_title + '</a><br>'
    #return HttpResponse(html)


def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)   #replaces entie try except statement
    return render(request, 'music/detail.html', {'album' : album})
    
    #return HttpResponse("<h2>details for Album id:" + str(album_id) + "</h2>")
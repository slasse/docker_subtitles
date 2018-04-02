from django.shortcuts import render, get_object_or_404
from .my_modules import file_lister, file_delete, downloader
from .models import movie_name, file_list, settings


# Create your views here.

## ff om te testen
def app_folder_setting():
    data = settings.objects.all()
    for x in data:
        return(x.folder_path)
###
path = app_folder_setting()

def index(request):
    list = []
    context = {'list':list}
    return render(request, 'viewer/index.html', context)

def by_withsubs(request):
    identifier = 'films met subs'
    list = movie_name.objects.filter(has_subtitle = True).order_by("moviename")
    context = {'list':list, 'identifier':identifier}
    return render(request, 'viewer/resultview.html', context)

def by_withoutsubs(request):
    identifier = 'films zonder subs'
    list = movie_name.objects.filter(has_subtitle=False).order_by("moviename")
    context = {'list':list, 'identifier':identifier}
    return render(request, 'viewer/resultview.html', context)

def by_folder(request):
    identifier = 'alle films'
    all_movies = movie_name.objects.all().order_by("moviename")
    context = {'all_movies':all_movies, 'identifier':identifier}
    return render(request, 'viewer/allmovies.html', context)

def detail_view(request,m_detail):
    selected_movie = file_list.objects.filter(m_name__moviename__icontains=m_detail.replace("-"," "))
    context = {'selected_movie':selected_movie, 'm_detail':m_detail}
    return render(request,'viewer/detail_view.html', context)

def refresh_list(request):
    file_lister(path)

    return render(request,'viewer/index.html')


def delete_file(request, d_file):
    file_to_delete = d_file
    file_delete(d_file)
    context = {'file_to_delete': file_to_delete}
    return render(request, 'viewer/deleted.html', context)

def download_view(request, f_name):
    subtitle_to_search = f_name
    downloader(f_name)
    context = {'subtitle_to_search': subtitle_to_search}
    return render(request, 'viewer/downloaded.html', context)

#to_check = file_lister(path)

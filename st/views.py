from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .views_helper import *
from .forms import *
# Create your views here.

def home(request):

    content = {}
    return render(request, funct_name_html(), content)
    
def l_shows(request):

    shows = Show.objects.order_by('-imdb_rating')
    context = prepare_list_context(shows)
    return render(request, funct_name_html(), {"shows":context})  
   
def l_seasons(request, name):

    seasons = Season.objects.filter(name=name).order_by('number')
    context = prepare_list_context(seasons)
    return render(request, funct_name_html(), {"seasons":context})  
   
def l_episodes(request, name, number):

    episodes = Season.objects.filter(name=name).filter(number=number).order_by('number')
    context = prepare_list_context(episodes)
    return render(request, funct_name_html(), {"episodes":context})  
   
def show(request, name):

    show = Show.objects.get(name=name)
    context = prepare_context(show)
    return render(request, funct_name_html(), {"show":context}) 

def my_show_info(request, name):

    show_pk = Show.objects.get(name=name).pk
    show_info = User_show_info.objects.get(show=show_pk)
    context = prepare_context(show_info)
    return render(request, funct_name_html(), {"info":context})   

def season(request, name, season):

    show_pk = Show.objects.get(name=name).pk
    season = Season.objects.filter(show=show_pk).get(number=season)
    context = prepare_context(season)
    return render(request, funct_name_html(), {"season":context})  

def episode(request, name, season, episode):

    show_pk = Show.objects.get(name=name).pk
    season_pk = Season.objects.filter(show=show_pk).get(number=season).pk
    ep = Episode.objects.filter(season=season_pk).get(number=episode)
    context = prepare_context(ep)
    return render(request, funct_name_html(), {"episode":context})  

def login():
    pass

def forgot_password():
    pass

def add_show():
    pass

def add_shows():
    pass

def edit_show():
    pass

def delete_show():
    pass

def settings():
    pass

def add_show_info(request):

    form = User_show_info_form()
    if request.method == 'POST':
        form = User_show_info_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    context = {"form": form}
    return render(request, funct_name_html(), context)

def edit_show_info(request, pk):

    obj = User_show_info.objects.get(id=pk)
    form = User_show_info_form(instance=obj)
    if request.method == 'POST':
        form = User_show_info_form(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('')
    context = {"form": form}
    return render(request, funct_name_html(), context)

def delete_show_info(request, name):

    obj = User_show_info.objects.get(show=name)
    if request.method == 'POST':
        obj.delete()
        redirect('shows')
    context = {"item": obj}
    return render(request, funct_name_html(), context)
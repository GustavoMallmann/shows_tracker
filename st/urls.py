from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("shows", l_shows, name="shows"),
    path("seasons/<str:name>", l_seasons, name="seasons"),
    path("episodes/<str:name>/<int:number>", l_episodes, name="episodes"),

    path("show/<str:name>", show, name="show"),
    path("info/<str:name>", myshowinfo, name="myshowinfo"),
    path("season/<str:name>/<int:season>", season, name="season"),
    path("episode/<str:name>/<int:season>/<int:episode>", episode, name="episode"),

    path("login", login, name="login"),
    path("forgot_password", forgot_password, name="forgot_password"),
    path("add_show", add_show, name="add_show"),
    path("add_shows", add_shows, name="add_shows"),
    path("delete_show", delete_show, name="delete_show"),
    path("edit_show", edit_show, name="edit_show"),
    path("settings", settings, name="settings"),
]
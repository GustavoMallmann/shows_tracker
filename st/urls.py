from django.urls import path
from .views import *

urlpatterns = [
    # hoome
    path("", home, name="home"),
    # listas de objetos
    path("shows", l_shows, name="shows"),
    path("seasons/<str:name>", l_seasons, name="seasons"),
    path("episodes/<str:name>/<int:number>", l_episodes, name="episodes"),
    # detalhe dos objetos
    path("show/<str:name>", show, name="show"),
    path("info/<str:name>", my_show_info, name="my_show_info"),
    path("season/<str:name>/<int:season>", season, name="season"),
    path("episode/<str:name>/<int:season>/<int:episode>", episode, name="episode"),
    #usuario
    path("login", login, name="login"),
    path("forgot_password", forgot_password, name="forgot_password"),
    path("settings", settings, name="settings"),
    #criar, editar, apagar (show)
    path("add_show", add_show, name="add_show"),
    path("add_shows", add_shows, name="add_shows"),
    path("edit_show", edit_show, name="edit_show"),
    path("delete_show", delete_show, name="delete_show"),
    #criar, editar, apagar (show_info)
    path("add_show_info", add_show_info, name="add_show_info"),
    path("edit_show_info", edit_show_info, name="edit_show_info"),
    path("delete_show_info/<str:name>", delete_show_info, name="delete_show_info"),
]

from django.contrib import admin
from django.urls import path
from core.views import Suatabela,Home,Base, CriarEletronico, CriarCategoria,CriarSala, Menu,De, Cadastro, Kwh,Dicas
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Base),
    path('home', Home, name='home'),
    path('criar/eletronico', CriarEletronico, name='CE'),
    path('criar/categoria', CriarCategoria, name='CC'),
    path('criar/sala', CriarSala, name='CS'),
    path("login",auth_views.LoginView.as_view(next_page="/"), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("menu", Menu, name="menu"),
    path("deletar_eletronico/<int:id>", De, name="deletarE"),
    path("cadastro", Cadastro, name="cadastro"),
    path("kwh", Kwh, name="kwh"),
    path("dicas",Dicas, name="dicas"),
    path("suatabela",Suatabela,name="ST")
]

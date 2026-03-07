
from django.contrib import admin
from django.urls import path
from core.views import Home,Base, CriarEletronico, CriarCategoria,CriarSala
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
]

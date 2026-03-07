from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from core.models import Eletronicos,Categorias,Salas
from .form import SalasForm, CategoriaForm,EletronicosForm
# Create your views here.
def Base(request):
    if request.user.is_authenticated:
        return redirect('home')  
    else:
        return redirect('login')

@login_required
def Home(request):
  ele = Eletronicos.objects.all()

  return render(request, 'core/home.html',{"Ele":ele})


@login_required
def CriarEletronico(request):
    if request.method == "POST":
        form = EletronicosForm(request.POST)
        if form.is_valid():
            Eletronico = form.save()
          
        
            return redirect("home")
    else:
        form = EletronicosForm()


    return render(request, 'core/criareletronico.html',{"form": form})
@login_required
def CriarCategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            Categoria = form.save()
          
        
            return redirect("home")
    else:
        form = CategoriaForm()


    return render(request, 'core/criarcategoria.html',{"form": form})
@login_required
def CriarSala(request):
    if request.method == "POST":
        form = SalasForm(request.POST)
        if form.is_valid():
            salas = form.save()
          
        
            return redirect("home")
    else:
        form = SalasForm()


    return render(request, 'core/criarsala.html',{"form": form})
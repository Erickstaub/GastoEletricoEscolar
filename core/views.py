from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from core.models import Eletronicos,Categorias,Salas
from .form import SalasForm, CategoriaForm,EletronicosForm
from django.db.models import Sum
# Create your views here.
def e_admin(user):
    return user.is_superuser
def Base(request):
    if request.user.is_authenticated:
        return redirect('menu')  
    else:
        return redirect('login')

@login_required
def Home(request):
    ele = Eletronicos.objects.filter(pertence_a_escola=True)
    total_valor = sum(e.custo for e in ele)
    return render(request, 'core/home.html',{"Ele":ele,'total_custo': total_valor,})


@login_required
def CriarEletronico(request):
    if request.method == 'POST':
        form = EletronicosForm(request.POST, user=request.user)
        if form.is_valid():
            eletronico = form.save(commit=False)
            
            # REGRA 1: O dono é SEMPRE quem está logado (ninguém muda isso)
            eletronico.dono = request.user
            
            # REGRA 2: Se o campo foi removido (user comum), garantimos que seja False
            if not request.user.is_superuser:
             cat_sala, _ = Categorias.objects.get_or_create(nome="Sala de aula", IsSala=True)

             # 2. Depois, criamos a sala vinculando-a à categoria que acabamos de garantir
            sala_padrao, _ = Salas.objects.get_or_create(
            nome="Sala 1", 
            defaults={'categoria': cat_sala} # 'defaults' serve para preencher se precisar criar
            )
    
            eletronico.sala = sala_padrao
            eletronico.pertence_a_escola = False
                
            eletronico.save()
            return redirect('menu')
    else:
        form = EletronicosForm(user=request.user)

    return render(request, 'core/criareletronico.html',{"form": form})
@login_required
@user_passes_test(e_admin)
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
@user_passes_test(e_admin)
def CriarSala(request):
    if request.method == "POST":
        form = SalasForm(request.POST)
        if form.is_valid():
            salas = form.save()
          
        
            return redirect("home")
    else:
        form = SalasForm()


    return render(request, 'core/criarsala.html',{"form": form})



@login_required
def Menu(request):
    return render(request, 'core/menu.html')
@login_required
def De(request, id):
    eletronico = get_object_or_404(Eletronicos, id=id)
    eletronico.delete()
    return redirect('menu')

def Cadastro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Cria o usuário no banco automaticamente
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})
@login_required
def Kwh(request):
    return render(request, 'core/kwh.html')
@login_required
def Dicas(request):
    return render(request, 'core/dicas.html')
@login_required
def Kwh(request):
    return render(request, 'core/kwh.html')

@login_required
def Suatabela(request):
  ele = Eletronicos.objects.filter(pertence_a_escola=False, dono=request.user)
  total_valor = sum(e.custo for e in ele)
  return render(request, 'core/suatabela.html',{"Ele":ele, 'total_custo': total_valor})
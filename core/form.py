from django import forms
from .models import Categorias,Eletronicos,Salas,User

class CategoriaForm(forms.ModelForm):
        class Meta:
            model = Categorias
            fields = "__all__"

class EletronicosForm(forms.ModelForm):
      class Meta:
            model = Eletronicos
            fields = "__all__"
class SalasForm(forms.ModelForm):
    class Meta:
          model = Salas
          fields = "__all__"
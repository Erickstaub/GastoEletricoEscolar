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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra para exibir apenas categorias que NÃO são de salas
        self.fields["categoria"].queryset = Categorias.objects.filter(IsSala=False)
class SalasForm(forms.ModelForm):
      class Meta:
          model = Salas
          fields = "__all__"
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].queryset = Categorias.objects.filter(IsSala=True)
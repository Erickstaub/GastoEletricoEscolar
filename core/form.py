from django import forms
from .models import Categorias,Eletronicos,Salas,User
from django.core.exceptions import ValidationError

class CategoriaForm(forms.ModelForm):
        class Meta:
            model = Categorias
            fields = "__all__"
            

class EletronicosForm(forms.ModelForm):
    class Meta:
        model = Eletronicos
        # Listamos os campos explicitamente para garantir a ordem
        fields = ['nome', 'categoria', 'potencia', 'quantidade', 'sala', 'horas', 'dias', 'pertence_a_escola']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Filtro de categorias (regra que você já tinha)
        self.fields["categoria"].queryset = Categorias.objects.filter(IsSala=False)

        # Regra: Se NÃO for superuser, ele não pode marcar 'pertence_a_escola'
        if self.user and not self.user.is_superuser:
            self.fields.pop('sala')
            self.fields.pop('pertence_a_escola')

    def clean_horas(self):
        horas = self.cleaned_data.get('horas')
        if horas > 24:
            raise ValidationError("Um dia tem apenas 24 horas! Digite um valor válido.")
        if horas < 0:
            raise ValidationError("A hora não pode ser negativa.")
        return horas

    def clean_dias(self):
        dias = self.cleaned_data.get('dias')
        if dias > 31:
            raise ValidationError("Um mês tem no máximo 31 dias.")
        if dias < 0:
            raise ValidationError("A quantidade de dias não pode ser negativa.")
        return dias
class SalasForm(forms.ModelForm):
      class Meta:
          model = Salas
          fields = "__all__"
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].queryset = Categorias.objects.filter(IsSala=True)
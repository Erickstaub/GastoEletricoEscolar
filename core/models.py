from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    IsSala = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Salas(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome




class Eletronicos(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    
    # --- NOVOS CAMPOS ---
    # Vincula o eletrônico a um usuário (dono)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # True = Escola, False = Privado
    pertence_a_escola = models.BooleanField(default=True, verbose_name="É da escola?")
    # --------------------

    potencia = models.IntegerField()  # watts
    quantidade = models.IntegerField()
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    horas = models.IntegerField()
    dias = models.IntegerField(default=26)

    def __str__(self):
        return f"{self.nome} ({'Escola' if self.pertence_a_escola else 'Privado'})"

    @property
    def kwh(self):
        return (self.potencia * self.horas * self.dias * self.quantidade) / 1000

    @property
    def custo(self):
        preco_kwh = 0.92  
        return self.kwh * preco_kwh
from django.db import models


# Create your models here.

class Segmento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True)
    endereco = models.CharField(max_length=200, default="")
    numero = models.IntegerField(null=True)
    complemento = models.CharField(max_length=100, default="")
    bairro = models.CharField(max_length=100, default="")
    cidade = models.CharField(max_length=100, default="")
    uf = models.CharField(max_length=2, default="")
    telefone = models.CharField(max_length=20, default="")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)
    segmento = models.ManyToManyField(Segmento)


    def __str__(self):
        return self.nome



class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    segmento = models.ManyToManyField(Segmento)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.
class Dados_c(models.Model):
    NIVEL = (
    ('F', 'F'),
    ('M', 'M'))
    

    cpf = models.CharField(max_length=11,unique=True)
    nome = models.CharField('Nome Cadastrado:',max_length=100,null=True)
    sobrenome = models.CharField('Sobre Nome:',max_length=150, blank=True,null=True)
    sexo = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='M')
    altura = models.CharField(max_length=20,null=True)
    peso = models.CharField(max_length=20,null=True)
    nascimento= models.DateField()
    numero = models.CharField('numero',max_length=30,null=True)
    foto = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nome
   

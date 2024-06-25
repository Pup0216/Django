from django.db import models
from django.utils import timezone


#makemigrations -> executar quando criar model

# Create your models here.

class Contact( models.Model ):
    name = models.CharField(max_length=50) #field com char de no maximo 50 chars
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    #por padrao esses itens são obrigatorios
    #para colocar como opcional adicionar 'blank = True' depois do maxLength
    created_at = models.DateTimeField(default=timezone.now) #quando o campo for criado;
    description = models.TextField()

    #Esse nome aparecerá na admin do django
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.last_name} {self.email}'
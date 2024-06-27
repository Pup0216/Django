from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#makemigrations -> executar quando criar model

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'



class Contact( models.Model ):
    name = models.CharField(max_length=50) #field com char de no maximo 50 chars
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    #por padrao esses itens são obrigatorios
    #para colocar como opcional adicionar 'blank = True' depois do maxLength
    created_at = models.DateTimeField(default=timezone.now) #quando o campo for criado;
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True,upload_to='pictures/%Y%m')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True, null=True) # CASCADE = deletando category, o contato sera deletado tambem
    
    owner = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    #Esse nome aparecerá na admin do django
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.last_name} {self.email} {self.category}'
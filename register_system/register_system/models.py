from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)  # Usar 'id' é uma prática comum
    email = models.EmailField(max_length=200, unique=True)  # Adiciona a restrição de unicidade para e-mails
    password = models.CharField(max_length=100)  # Mantém o comprimento do campo de senha

    def __str__(self):
        return self.email  

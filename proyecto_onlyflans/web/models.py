from django.db import models
import uuid

# Create your models here.
# Importamos el módulo UUID
import uuid
from django.db import models

#Modelo para almacenar los flanes
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#Modelo para el Formulario
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name
    
#Modelo para realizar los pedidos
from django.db import models

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return f'{self.nombre_cliente}'
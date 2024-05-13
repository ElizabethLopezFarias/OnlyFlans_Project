from django import forms
from .models import ContactForm, Pedido, Flan

# Definición del modelo de formulario para formulario de contacto
class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Correo electrónico',
            'message': 'Mensaje'
        }

# Definición del modelo de formulario para el inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# Definición del modelo de formulario para los pedidos básicos

class PedidoForm(forms.ModelForm):
     producto = forms.ModelChoiceField(queryset=Flan.objects.filter(is_private=False))
     cantidad = forms.IntegerField(min_value=1)
     class Meta:
         model = Pedido
         fields = ['nombre_cliente', 'email', 'direccion', 'telefono', 'producto', 'cantidad']


class PedidoFormPremium(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Flan.objects.all())
    cantidad = forms.IntegerField(min_value=1)
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'email', 'direccion', 'telefono', 'producto', 'cantidad']
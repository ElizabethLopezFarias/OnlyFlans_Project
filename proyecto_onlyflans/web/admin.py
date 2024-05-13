from django.contrib import admin
from .models import Flan, ContactForm, Pedido


# Registrar el modelo Flan en el panel de administración
admin.site.register(Flan)

# Registrar el modelo ContactForm
admin.site.register(ContactForm)

# Registrar el modelo Pedido
admin.site.register(Pedido)
from django.forms import ModelForm
from appCorridasBr.models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'email', 'senha']
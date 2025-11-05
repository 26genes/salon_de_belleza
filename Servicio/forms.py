from django.forms import ModelForm
from .models import Servicio
from django import forms

class FormularioServicio(ModelForm):
    class Meta:
        model = Servicio
        fields = ['imagen','nombre', 'descripcion', 'precio', 'duracion']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': '1000'}),

        }

        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['imagen'].widget.attrs.update(
                {'accept': '.jpg, .jpeg, .png, .gif'})  # Permitir imágenes
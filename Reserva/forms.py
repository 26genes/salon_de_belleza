from datetime import time
from django.forms import ModelForm, ValidationError
from .models import Reserva
from django import forms

class FormularioReserva(ModelForm):
    class Meta:
        model = Reserva
        fields = ['servicio', 'recomendaciones', 'fecha_reserva','hora_reserva']
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date'}),
            'hora_reserva': forms.TimeInput(attrs={'type': 'time'}),
        }
    def clean_hora_reserva(self):
        hora_reserva = self.cleaned_data.get('hora_reserva')

        # Definir las horas de apertura y cierre (8 AM a 8 PM)
        hora_inicio = time(8, 0)  # 08:00 AM
        hora_fin = time(20, 0)  # 08:00 PM

        # Validar si la hora de la reserva está dentro del rango permitido
        if not (hora_inicio <= hora_reserva <= hora_fin):
            raise ValidationError("La hora de la reserva debe estar entre las 8:00 AM y las 8:00 PM.")
        
        return hora_reserva
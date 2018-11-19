from django import forms
from .models import Notas_mat

class notasNovas(forms.ModelForm):
	class Meta():
		model = Notas_mat
		fields = ('nome', 'valor', 'nota')
	
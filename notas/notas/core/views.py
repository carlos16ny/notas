from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Materias, Notas_mat
from .forms import notasNovas


# Create your views here.
def home(request):
	template_name = 'index.html'	
	return render(request, template_name)

def tabela(request, sem):
	mcl = Materias.objects.filter(status__exact=1).values_list('id', flat=True)
	mnc = Materias.objects.filter(status__exact=0)
	seme = Materias.objects.filter(sem__exact=sem)
	todas = Materias.objects.all()
	context = {
		'sem' : seme,
		'td' : todas,
		'mnc' : mnc,
		'mcl' : mcl,
	}
	template_name = 'tabela.html'
	return render(request, template_name, context)


def notas(request, id):
	template_name = 'notas.html'
	materia = Materias.objects.filter(id__exact=id)
	nota = Notas_mat.objects.filter(mat__exact=id)
	form = notasNovas()
	context = {
		'form' : notasNovas,
		'mat' : materia,
		'nota' : nota,
	}
	if request.method == 'POST':
		form = 	notasNovas(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.mat = id
			post.save(force_insert=True)
			return render(request, template_name, context)
	else:
		form = notasNovas()


	return render(request, template_name, context)


	
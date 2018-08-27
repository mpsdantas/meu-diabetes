from django.shortcuts import render, redirect
from .fuzzifier import *
from .models import *
from autentication.models import *
from django.http import JsonResponse

def dashboardInicio(request):
	if request.session['autenticado']:
		if request.method == "GET":
			return render(request, 'dashboard.html')
		elif request.method == "POST":
			if request.POST.get('exercicio') and request.POST.get('glicemia_jejum') and request.POST.get('glicemia_pos'):
			
				resultado = fuzzifier(request.POST['exercicio'], request.POST['glicemia_jejum'], request.POST['glicemia_pos'])

				obj = Parametros.objects.create(
					dias_exercicio = request.POST['exercicio'],
					glicemia_em_jejum = request.POST['glicemia_jejum'],
					glicemia_pos_refeicao = request.POST['glicemia_pos'],
					fuzzy_result = resultado,
					user = Usuario.objects.get(email=request.session['email'])
				)
				obj.save()

		return render(request, 'dashboard.html', {})
	return redirect('loginPage')

def fuzzing(request):

	if request.method == "POST":
		if request.POST.get('exercicio') and request.POST.get('glicemia_jejum') and request.POST.get('glicemia_pos'):
			resultado = fuzzifier(request.POST['exercicio'], request.POST['glicemia_jejum'], request.POST['glicemia_pos'])

			obj = Parametros.objects.create(
				dias_exercicio = request.POST['exercicio'],
				glicemia_em_jejum = request.POST['glicemia_jejum'],
				glicemia_pos_refeicao = request.POST['glicemia_pos'],
				fuzzy_result = resultado,
				user = Usuario.objects.get(email=request.session['email'])
			)
			obj.save()
			return render(request, 'dashboard.html', {})
		return render(request, 'dashboard.html', {})
	return  render(request, 'dashboard.html', {})

 
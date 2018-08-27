from django.shortcuts import render, redirect
from .fuzzifier import *
from .models import *
from autentication.models import *
from django.http import JsonResponse

def dashboardInicio(request):
	if request.session['autenticado']:
		if request.method == "GET":
			active_user = Usuario.objects.get(email=request.session['email'])
			analises = Parametros.objects.filter(user=active_user).order_by('created')
			return render(request, 'dashboard.html', {'nome': request.session['nome'], 
				'email': request.session['email'], 'analises': analises})
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

		return render(request, 'dashboard.html', {'nome': request.session['nome'], 'email': request.session['email']})
	return redirect('loginPage')


def fuzzing(request):
	if request.session['autenticado']:
		if request.method == "GET":
			return render(request, 'cadastro_dados.html')
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

				return redirect('/dashboard')
		return render(request, 'cadastro-dados.html', {})
	return redirect('loginPage')

 
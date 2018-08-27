from django.shortcuts import render, redirect
from .models import Usuario
from .forms import CadastroForm
from django.http import HttpResponse
from django.http import JsonResponse

def paginaInicial(request):
    try:
        autenticado = request.session['autenticado']
        if autenticado:
            return render(request, 'dashboard.html', {'nome': request.session['nome'], 'email': request.session['email']})
    except KeyError:
        pass

    return render(request, 'index.html')

def paginaCadastro(request):
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('loginPage')
    return render(request, 'cadastro.html', {'form': form})

def realizarLogin(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(email=request.POST.get("email"))
        if(usuario.senha==request.POST.get("senha")):
            request.session['autenticado'] = True
            request.session['nome'] = usuario.nome
            request.session['email'] = usuario.email
            return JsonResponse({'status': True, 'login': 'Login autorizado.'})
            #return render(request, 'dashboard.html', {'nome': request.session['nome'], 'email': request.session['email']})
        else:
            return JsonResponse({'status': False, 'erro': 'Usuário ou senha incorretos.'})
    return render(request, 'index.html')

def sair(request):
    try:
        del request.session['nome']
        del request.session['email']
        request.session['autenticado'] = False
    except KeyError:
        pass

    return render(request, 'index.html')
    
        



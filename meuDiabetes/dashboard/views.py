from django.shortcuts import render, redirect

# Create your views here.

def dashboardInicio(request):
    if request.session['autenticado']:
        return render(request, 'dashboard.html')
    return redirect('loginPage')
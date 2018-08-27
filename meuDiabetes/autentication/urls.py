from django.urls import path
from .views import paginaInicial, paginaCadastro, realizarLogin, sair
urlpatterns = [
    path('', paginaInicial, name="loginPage"),
    path('cadastro', paginaCadastro, name="cadastroPage"),
    path('login', realizarLogin, name="login"),
    path('logout', sair, name="sair")
]
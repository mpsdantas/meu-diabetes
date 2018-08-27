from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard', dashboardInicio, name="dashboardHome"),
    path('cadastro-dados', fuzzing, name="fuzzing")
]
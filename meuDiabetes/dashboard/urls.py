from django.urls import path
from .views import dashboardInicio
urlpatterns = [
    path('dashboard', dashboardInicio, name="dashboardHome")
]
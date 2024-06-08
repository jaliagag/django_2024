from django.urls import path
from Tutorial_app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('dashboard', views.dashboards, name="Dashboards"),
    path('login', views.login, name="Login"),
]

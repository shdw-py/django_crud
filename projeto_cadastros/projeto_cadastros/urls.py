from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota/path, view responsavel, nome de referencia
    # usuarios.com
    path('', views.home, name='home'),
    path('usuarios/', views.formulario, name='formulario'),
    path('usuarios/listagem', views.usuarios, name='listagem'),
]

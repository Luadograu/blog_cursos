from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/alimentos/', views.alimentos, name='alimentos'),
    path('cursos/quimica/', views.quimica, name='quimica'),
    path('cursos/ads/', views.ads, name='ads'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.kontrak, name='kontrak'),
    path('tambah_kontrak/', views.tambah_kontrak, name='tambah_kontrak')
]
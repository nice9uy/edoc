from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('tambah_data/', views.tambah_data, name='tambah_data' ),
    path('edit_data/', views.edit, name='edit'),
    path('setting/', views.setting, name='setting')
]
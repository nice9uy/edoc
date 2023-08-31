from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('tambah_data/', views.tambah_data, name='tambah_data' ),
    path('edit_data/', views.edit, name='edit'),
    path('setting/<int:delete_id>', views.setting, name='setting'),
    path('setting_klasifikasi/', views.setting_klasifikasi, name='setting_klasifikasi'),
    path('setting_kelompok/', views.setting_kelompok, name='setting_kelompok'),
    # path('delete_kelompok/', views.setting_kelompok, name='setting_kelompok'),
]
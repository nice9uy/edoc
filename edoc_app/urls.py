from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('tambah_data/', views.tambah_data, name='tambah_data' ),
    path('edit_data/', views.edit, name='edit'),
    path('setting/', views.setting, name='setting'),
    path('setting_surat/', views.setting_surat, name='setting_surat'),
    path('setting_klasifikasi/', views.setting_klasifikasi, name='setting_klasifikasi'),
    path('setting_kelompok/', views.setting_kelompok, name='setting_kelompok'),
    path('edit_setting_surat/<int:id_edit_setting>/', views.edit_setting_surat, name='edit_setting_surat'),
    # path('delete_kelompok/', views.setting_kelompok, name='setting_kelompok'),
]
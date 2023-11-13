from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard' ),

    path('data_surat/', views.home, name='home'),

    path('tambah_data/', views.tambah_data, name='tambah_data' ),
    # path('setting_data/', views.setting_data, name='setting_data'),
    path('setting/', views.setting, name='setting'),

    path('duplikasi_surat/', views.duplikasi_surat, name='duplikasi_surat'),




    path('hari_ini/', views.hari_ini, name='hari_ini'),

    path('olah_data/', views.olah_data, name='olah_data'),
    path('edit_olah_data/<int:id_edit_olah_data>', views.edit_olah_data, name='edit_olah_data'),
    path('delete_olah_data/<int:id_delete_olah_data>', views.delete_olah_data, name='delete_olah_data'),
    
    path('olah_data_harian/', views.olah_data_harian, name='olah_data_harian'),
    path('edit_olah_data_harian/<int:id_edit_olah_data_harian>', views.edit_olah_data_harian, name='edit_olah_data_harian'),
    path('delete_olah_data_harian/<int:id_delete_olah_data_harian>', views.delete_olah_data_harian, name='delete_olah_data_harian'),

    path('setting_surat/', views.setting_surat, name='setting_surat'),
    path('edit_setting_surat/<int:id_edit_setting>/', views.edit_setting_surat, name='edit_setting_surat'),
    path('delete_setting_surat/<int:id_delete_setting>/', views.delete_setting_surat, name='delete_setting_surat'),
    
    path('setting_klasifikasi/', views.setting_klasifikasi, name='setting_klasifikasi'),
    path('edit_setting_klasifikasi/<int:id_edit_klasifikasi>/', views.edit_setting_klasifikasi, name='edit_setting_klasifikasi'),
    path('delete_setting_klasifikasi/<int:id_delete_klasifikasi>/', views.delete_setting_klasifikasi, name='delete_setting_klasifikasi'),

    path('setting_kelompok/', views.setting_kelompok, name='setting_kelompok'),
    path('edit_setting_kelompok/ <int:id_setting_kelompok>/', views.edit_setting_kelompok, name='edit_setting_kelompok'),
    path('delete_setting_kelompok/<int:id_delete_kelompok>/', views.delete_setting_kelompok, name='delete_setting_kelompok'),

    path('laporan_harian/', views.laporan_harian, name='laporan_harian'),
    path('laporan_bulanan/', views.laporan_bulanan, name='laporan_bulanan'),
    
    # path('delete_kelompok/', views.setting_kelompok, name='setting_kelompok'),
]
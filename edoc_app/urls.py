from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('tambah_data/', views.tambah_data, name='tambah_data' ),
    # path('edit_data/', views.edit, name='edit'),
    path('setting/', views.setting, name='setting'),

    path('olah_data/', views.olah_data, name='olah_data'),
    path('edit_olah_data/<int:id_edit_olah_data>', views.edit_olah_data, name='edit_olah_data'),
    path('delete_olah_data/<int:id_delete_olah_data>', views.delete_olah_data, name='delete_olah_data'),

    path('setting_surat/', views.setting_surat, name='setting_surat'),
    path('edit_setting_surat/<int:id_edit_setting>/', views.edit_setting_surat, name='edit_setting_surat'),
    path('delete_setting_surat/<int:id_delete_setting>/', views.delete_setting_surat, name='delete_setting_surat'),
    
    path('setting_klasifikasi/', views.setting_klasifikasi, name='setting_klasifikasi'),
    path('edit_setting_klasifikasi/<int:id_edit_klasifikasi>/', views.edit_setting_klasifikasi, name='edit_setting_klasifikasi'),
    path('delete_setting_klasifikasi/<int:id_delete_klasifikasi>/', views.delete_setting_klasifikasi, name='delete_setting_klasifikasi'),

    path('setting_kelompok/', views.setting_kelompok, name='setting_kelompok'),
    path('edit_setting_kelompok/ <int:id_setting_kelompok>/', views.edit_setting_kelompok, name='edit_setting_kelompok'),
    path('delete_setting_kelompok/<int:id_delete_kelompok>/', views.delete_setting_kelompok, name='delete_setting_kelompok'),



    # path('delete_kelompok/', views.setting_kelompok, name='setting_kelompok'),
]
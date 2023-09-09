from django.contrib import admin

# Register your models here.
from .models import DatabaseSurat
from .models import KlasifikasiSurat
from .models import KelompokSurat
from .models import NamaSurat

class ListDatabaseSurat(admin.ModelAdmin):
    list_display = ('id_user','surat', 'klasifikasi'
                    'kelompok','tgl','no_surat','kepada'
                    'perihal','upload_file','today'
                    )
class ListNamaSurat(admin.ModelAdmin):
    list_display = ('id_user','id' , 'nama_surat')

class ListKlasifikasiSurat(admin.ModelAdmin):
    list_display =  ('id_user','id' , 'nama_klasifikasi')

class ListKelompokSurat(admin.ModelAdmin):
    list_display =  ('id_user','id' , 'nama_kelompok')

admin.site.register(DatabaseSurat)
admin.site.register(NamaSurat, ListNamaSurat)
admin.site.register(KlasifikasiSurat, ListKlasifikasiSurat)
admin.site.register(KelompokSurat,ListKelompokSurat)



from django.contrib import admin

# Register your models here.
from .models import DatabaseSurat
from .models import KlasifikasiSurat
from .models import KelompokSurat

admin.site.register(DatabaseSurat)
admin.site.register(KlasifikasiSurat)
admin.site.register(KelompokSurat)


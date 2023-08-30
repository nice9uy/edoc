from django.db import models

# Create your models here.
def user_folder(instance, filename,):
    return f"{instance.user}/{filename}"

class DatabaseSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    user = models.CharField(max_length=30)
    surat = models.CharField(max_length=10)
    klasifikasi = models.CharField(max_length=30)
    katagori = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.TextField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    today = models.DateField()

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "DatabaseSurat"

class KlasifikasiSurat(models.Model):
    username = models.TextField(max_length=30)
    kode = models.TextField(max_length=10)
    nama_klasifikasi = models.TextField(max_length=30)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = "KlasifikasiSurat"

class JenisSurat(models.Model):
    username = models.TextField(max_length=30)
    kode = models.TextField(max_length=10)
    nama_jenis_surat = models.TextField(max_length=30)

    def __str__(self):
        return str(self.username)

    class Meta:
        db_table = "JenisSurat"
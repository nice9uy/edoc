from django.db import models

# Create your models here.
def user_folder(instance, filename):
    return f"{instance.username}/surat/{filename}"

class DatabaseSurat(models.Model):
  
    id = models.AutoField(primary_key=True, unique=True)
    id_user = models.CharField(max_length=4)
    username = models.CharField(max_length=30)
    surat = models.CharField(max_length=10)
    klasifikasi = models.CharField(max_length=30)
    kelompok = models.CharField(max_length=30)
    tgl = models.DateField()
    no_surat = models.TextField(max_length=200)
    kepada = models.CharField(max_length=200)
    perihal = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to= user_folder, null=False, blank=False)
    today = models.DateField()
    tahun = models.CharField(max_length=4)
    

    class Meta:
        db_table = "DatabaseSurat"

class NamaSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_user = models.CharField(max_length=4)
    nama_surat = models.CharField(max_length=30)

    class Meta:
        db_table = "Surat"

class KlasifikasiSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_user = models.CharField(max_length=4)
    username = models.CharField(max_length=20)
    nama_klasifikasi = models.CharField(max_length=30)

    class Meta:
        db_table = "KlasifikasiSurat"

class KelompokSurat(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_user = models.CharField(max_length=4)
    username = models.CharField(max_length=20)
    nama_kelompok = models.CharField(max_length=30)

    class Meta:
        db_table = "KelompokSurat"
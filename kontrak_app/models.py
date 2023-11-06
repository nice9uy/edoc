from django.db import models

# Create your models here. 
def user_folder(instance, filename):
    return f"{instance.username}/kontrak/{filename}"

class Kontrak(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    id_user = models.CharField(max_length=4)
    username = models.CharField(max_length=30)
    no_kontrak = models.IntegerField()
    sumber_dana = models.CharField(max_length=6)
    tgl = models.DateField()
    tentang = models.CharField(max_length=200)
    upload_file = models.FileField(upload_to=user_folder, null=False, blank=False)
    today = models.DateField()
    tahun = models.CharField(max_length=4)

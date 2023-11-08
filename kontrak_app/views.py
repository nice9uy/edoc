from django.shortcuts import render



# Create your views here.

def kontrak(request):

    id_username = request.user.pk

    user = request.user

    # klasifikasi = DatabaseSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    # kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   

    return render (request, 'kontrak/pages/index.html') 


def tambah_kontrak(request):

    return render (request, 'kontrak/pages/tambah_kontrak.html') 
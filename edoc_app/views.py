from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pathlib import Path
from . models import DatabaseSurat, KlasifikasiSurat, KelompokSurat, NamaSurat
from django.views.decorators.csrf import csrf_protect
from datetime import date
from django.contrib import messages
from django.contrib.auth import get_user_model


@login_required(login_url="/accounts/login/")
def home(request):
    id_username = request.user.pk
    datasemuasurat = DatabaseSurat.objects.filter(id_user = id_username).values()

    context = {
        'page_title'     : 'Home',
        'datasemuasurat' :  datasemuasurat
    }
    
    # print(request.user)
    return render(request,'pages/index.html', context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data(request):
    id_username = request.user.pk

    surat_id = NamaSurat.objects.filter(id_user = id_username).values_list("nama_surat" , flat=True)
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   
    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload)
    upload_name_files = files_name.split(',')

    get_surat = request.POST.get('surat')
    get_klasifikasi = request.POST.get('klasifikasi')
    get_kelompok = request.POST.get('kelompok')
    get_tanggal = request.POST.get('tanggal')
    
    # x = int(get_tanggal[3])

    # print(x)
    
    try:  
        ##### UNTUK TANGGAL  ##########   
        # hari = get_tanggal[:3]
        # bulan = get_tanggal[3:5]
        # tahun = get_tanggal[5:9]
    
        # print(hari)
        # print(bulan)
        # print(tahun)
        
        # tanggal = date(tahun, bulan, hari)
        ################################### 
        no_surat = upload_name_files[0]
        kepada = upload_name_files[1]
        #### UNTUK PRIHAL #################
        prihal = upload_name_files[2]
        prihal_surat = prihal[:-4]
        ###################################
        upload_data_surat = files_upload

        ##### Untuk Tanggal Sekarang ######
        hari_ini = date.today()
 
        upload_data = DatabaseSurat(
            id_user     = surat_id,
            surat       = get_surat,
            klasifikasi = get_klasifikasi,
            kelompok    = get_kelompok,
            # tgl         = tanggal,
            no_surat    = no_surat,
            kepada      = kepada,
            perihal     = prihal_surat,
            upload_file = upload_data_surat,
            today       = hari_ini,
        )
        
    except Exception as errorloading:
        print("Ada yang error karena :" , errorloading )
        messages.error(request, "")
        
    else:
        upload_data.save()
        messages.success(request, "fwedwefef")
        return redirect('home')
        
    context = {
        'page_title' : 'Tambah Data',
        'surat'      : surat_id,
        'klasifikasi' : klasifikasi,
        'kelompok' : kelompok,
        
    }
   
    return render(request,'pages/tambah_data.html', context)

        
@login_required(login_url="/accounts/login/")
def setting(request):
    user_name = request.user.pk
    surat = NamaSurat.objects.filter(id_user = user_name).values()
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = user_name).values()
    kelompok = KelompokSurat.objects.filter(id_user = user_name).values()

    # print(surat)

    context = {
        'page_title' : 'Setting',
        'surat'      : surat,
        'klasifikasi' : klasifikasi,
        'kelompok' : kelompok,
    }    

    return render(request,'pages/setting.html', context)

@csrf_protect
def setting_surat(request):

    if request.method == 'POST':
        user_name = request.user.pk
        nama_surat = request.POST.get('nama_surat')
    
        dbsurat = NamaSurat(
            id_user   = user_name, 
            nama_surat = nama_surat
        )
        dbsurat.save()
        dbsurat.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')
    
@csrf_protect
def edit_setting_surat(request, id_edit_setting):
    edit_surat = get_object_or_404(NamaSurat, pk = id_edit_setting)

    if request.method == 'POST':
        user_name = request.user.pk
        nama_surat = request.POST.get('nama_surat')
    
        edit_surat = NamaSurat(
            id = id_edit_setting,
            id_user   = user_name, 
            nama_surat = nama_surat,
        )
        edit_surat.save()
        edit_surat.clean_fields()
        return redirect('setting')
    
    
    return render(request,'pages/setting.html')

@csrf_protect
def delete_setting_surat(request, id_delete_setting):
    delete_surat = get_object_or_404(NamaSurat, pk = id_delete_setting)

    if request.method == 'POST':
        delete_surat.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')


@csrf_protect
def setting_klasifikasi(request):
    if request.method == 'POST':
        user_name = request.user.pk
        nama_klasifikasi = request.POST.get('nama_klasifikasi_surat')
    
        klasifikasi = KlasifikasiSurat(
            id_user         = user_name,
            nama_klasifikasi = nama_klasifikasi
        )

        klasifikasi.save()
        klasifikasi.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')
    
@csrf_protect
def edit_setting_klasifikasi(request, id_edit_klasifikasi):
    edit_klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_edit_klasifikasi)

    if request.method == 'POST':
        user_name = request.user.pk
        nama_surat = request.POST.get('nama_klasifikasi_surat')
    
        edit_klasifikasi = KlasifikasiSurat(
            id = id_edit_klasifikasi,
            id_user   = user_name, 
            nama_klasifikasi = nama_surat,
        )
        edit_klasifikasi.save()
        edit_klasifikasi.clean_fields()
        return redirect('setting')
    
    
    return render(request,'pages/setting.html')

@csrf_protect
def delete_setting_klasifikasi(request, id_delete_klasifikasi):
    delete_klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_delete_klasifikasi)

    if request.method == 'POST':
        delete_klasifikasi.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')

@csrf_protect
def setting_kelompok(request):
    if request.method == 'POST':
        user_name = request.user.pk
        nama_kelompok = request.POST.get('nama_kelompok_surat')

        kelompok = KelompokSurat(
            id_user      = user_name,
            nama_kelompok = nama_kelompok
        )

        kelompok.save()
        kelompok.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')
    
@csrf_protect
def edit_setting_kelompok(request, id_setting_kelompok):
    edit_kelompok = get_object_or_404(KelompokSurat, pk = id_setting_kelompok)

    if request.method == 'POST':
        user_name = request.user.pk
        nama_surat = request.POST.get('nama_kelompok_surat')
    
        edit_kelompok = KelompokSurat(
            id = id_setting_kelompok,
            id_user   = user_name, 
            nama_kelompok = nama_surat,
        )
        edit_kelompok.save()
        edit_kelompok.clean_fields()
        return redirect('setting')
    
    return render(request,'pages/setting.html')

@csrf_protect
def delete_setting_kelompok(request, id_delete_kelompok):
    delete_klasifikasi = get_object_or_404(KelompokSurat, pk = id_delete_kelompok)

    if request.method == 'POST':
        delete_klasifikasi.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')
    

def edit(request):
    return render(request,'pages/edit_data.html')

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from pathlib import Path
from . models import DatabaseSurat, KlasifikasiSurat, KelompokSurat, NamaSurat
from django.views.decorators.csrf import csrf_protect
from datetime import date
from django.contrib import messages
from django.contrib.auth import get_user_model


@login_required(login_url="/accounts/login/")
def home(request):
    user_name = request.user
    datasemuasurat = DatabaseSurat.objects.filter(user = user_name).values()

    context = {
        'page_title'     : 'Home',
        'datasemuasurat' :  datasemuasurat
    }
    
    # print(request.user)
    return render(request,'pages/index.html', context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data(request):
    user_name = request.user
    surat = NamaSurat.objects.values('nama_surat').distinct().order_by('nama_surat')
    klasifikasi = KlasifikasiSurat.objects.filter(username = user_name).values()
    kelompok = KelompokSurat.objects.filter(username = user_name).values()

    print(surat)
    
    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload)
    upload_name_files = files_name.split(',')


    
    try:  
        surat = upload_name_files[1].capitalize()
        klasifikasi_surat = upload_name_files[0].capitalize()
        jenis_surat = upload_name_files[2]
        ##### UNTUK TANGGAL  ##########
        tgl  = upload_name_files[3]
        
        hari = int(tgl[:3])
        bulan = int(tgl[3:5])
        tahun = int(tgl[5:9])
        
        tanggal = date(tahun, bulan, hari)
        ################################### 
        no_surat = upload_name_files[4]
        kepada = upload_name_files[5]
        #### UNTUK PRIHAL #################
        prihal = upload_name_files[6]
        prihal_surat = prihal[:-4]
        ###################################
        upload_data_surat = files_upload

        ##### Untuk Tanggal Sekarang ######
        hari_ini = date.today()
 
        upload_data = DatabaseSurat(
            user        = user_name,
            surat       = surat,
            klasifikasi = klasifikasi_surat,
            kelompok    = jenis_surat,
            tgl         = tanggal,
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
        'surat'      : surat,
        'klasifikasi' : klasifikasi,
        'kelompok' : kelompok,
        
    }
   
    return render(request,'pages/tambah_data.html', context)

        
@login_required(login_url="/accounts/login/")
def setting(request):
    user_name = request.user
    surat = NamaSurat.objects.filter(username = user_name).values()
    klasifikasi = KlasifikasiSurat.objects.filter(username = user_name).values()
    kelompok = KelompokSurat.objects.filter(username = user_name).values()

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
        user_name = request.user
        nama_surat = request.POST.get('nama_surat')
    
        dbsurat = NamaSurat(
            username   = user_name, 
            nama_surat = nama_surat
        )
        dbsurat.save()
        dbsurat.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')

@csrf_protect
def setting_klasifikasi(request):
    if request.method == 'POST':
        user_name = request.user
        nama_klasifikasi = request.POST.get('nama_klasifikasi_surat')
    
        klasifikasi = KlasifikasiSurat(
            username         = user_name,
            nama_klasifikasi = nama_klasifikasi
        )

        klasifikasi.save()
        klasifikasi.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')

@csrf_protect
def setting_kelompok(request):
    if request.method == 'POST':
        user_name = request.user
        nama_kelompok = request.POST.get('nama_kelompok_surat')

        kelompok = KelompokSurat(
            username      = user_name,
            nama_kelompok = nama_kelompok
        )

        kelompok.save()
        kelompok.clean_fields()
        return redirect('setting')
    else:
        return render(request,'pages/setting.html')
    

def edit(request):
    return render(request,'pages/edit_data.html')

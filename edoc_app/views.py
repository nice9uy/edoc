from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from pathlib import Path
from . models import DatabaseSurat, KlasifikasiSurat, KelompokSurat, NamaSurat
from django.views.decorators.csrf import csrf_protect
from datetime import date
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User
import datetime
from datetime import datetime
from django.utils.dateparse import parse_date



@csrf_protect
@login_required(login_url="/accounts/login/")
def home(request):
    id_username = request.user.pk
    user = request.user
    datasemuasurat = DatabaseSurat.objects.filter(id_user = id_username).values()

    context = {
        'page_title'     : 'Home',
        'datasemuasurat' :  datasemuasurat,
        'user'           :  user
    }
    
    return render(request,'pages/index.html', context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def tambah_data(request):
    id_username = request.user.pk
    username = request.user

    now = datetime.now()
    year = now.strftime("%Y")

    hari_ini = date.today()

    # surat_id = NamaSurat.objects.filter(id_user = id_username).values_list("nama_surat" , flat=True)
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)
   
    get_surat = request.POST.get('surat')
    get_klasifikasi = request.POST.get('klasifikasi')
    get_kelompok = request.POST.get('kelompok')
    get_tanggal = request.POST.get('tanggal')

    files_upload = request.FILES.get('file_name')
    files_name = str(files_upload).split(',')

    filename_list_count = len(files_name)
   
    try:  
        no_surat = files_name[0]
        kepada = files_name[1]
        prihal = files_name[2] 
        prihal_surat = prihal[:-4]


        upload_data = DatabaseSurat(
            id_user     = id_username,
            username    = username,
            surat       = get_surat,
            klasifikasi = get_klasifikasi,
            kelompok    = get_kelompok,
            tgl         = get_tanggal,
            no_surat    = no_surat,
            kepada      = kepada,
            perihal     = prihal_surat,
            upload_file = files_upload,
            today       = hari_ini,
            tahun       = year,
        )
        
    except Exception:
        pass
        
    else:
        if filename_list_count == 3:
            upload_data.save()
            return redirect('home')
        else:
            messages.warning(request,'bzdbdbzdb')
            print("ada yang salah, cek lagi ")
        
    context = {
        'page_title' : 'Tambah Data',
        'klasifikasi' : klasifikasi,
        'kelompok' : kelompok,
        
    }
   
    return render(request,'pages/tambah_data.html', context)

@csrf_protect        
@login_required(login_url="/accounts/login/")
def setting(request):
    user_name = request.user.pk
    surat = NamaSurat.objects.filter(id_user = user_name).values()
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = user_name).values()
    kelompok = KelompokSurat.objects.filter(id_user = user_name).values()

    context = {
        'page_title' : 'Setting',
        'surat'      : surat,
        'klasifikasi' : klasifikasi,
        'kelompok' : kelompok,
    }    

    return render(request,'pages/setting.html', context)

@csrf_protect
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
def delete_setting_surat(request, id_delete_setting):
    delete_surat = get_object_or_404(NamaSurat, pk = id_delete_setting)

    if request.method == 'POST':
        delete_surat.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')


@csrf_protect
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
def delete_setting_klasifikasi(request, id_delete_klasifikasi):
    delete_klasifikasi = get_object_or_404(KlasifikasiSurat, pk = id_delete_klasifikasi)

    if request.method == 'POST':
        delete_klasifikasi.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')

@csrf_protect
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
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
@login_required(login_url="/accounts/login/")
def delete_setting_kelompok(request, id_delete_kelompok):
    delete_klasifikasi = get_object_or_404(KelompokSurat, pk = id_delete_kelompok)

    if request.method == 'POST':
        delete_klasifikasi.delete()
        return redirect('setting')
    
    return render(request,'pages/setting.html')
    
@csrf_protect
@login_required(login_url="/accounts/login/")
def olah_data(request):
    id_username = request.user.pk
    datasemuasurat = DatabaseSurat.objects.filter(id_user = id_username).values()
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)

    if request.method == 'POST':
        tgl = request.POST.get("lapor_per_hari_semua_data")
        cari_tanggal = parse_date(tgl)

        # filter_data_perhari = DatabaseSurat.objects.all().filter(username = id_username , today =  cari_tanggal ).values_list()
        filter_data_perhari = DatabaseSurat.objects.filter(id_user = id_username, today =  cari_tanggal ).values()
        data_count = DatabaseSurat.objects.filter(id_user = id_username, today =  cari_tanggal ).count()


        print(filter_data_perhari)

    context = {
        'page_title'     : 'Olah Data',
        'datasemuasurat' : datasemuasurat,
        'klasifikasi'    : klasifikasi,
        'kelompok'       : kelompok,
        'filter_hari'    : filter_data_perhari,
        'data_count'     : data_count
    }
    return render(request,'pages/olah_data.html', context)

@csrf_protect
@login_required(login_url="/accounts/login/")
def edit_olah_data(request, id_edit_olah_data):
    id_username = request.user
    edit_olah = get_object_or_404(DatabaseSurat, pk = id_edit_olah_data)
    now = datetime.now()
    year = now.strftime("%Y")

    if request.method == 'POST':
        id_user = request.user.pk
        username = str(id_username)
        surat = request.POST.get('surat')
        klasifikasi = request.POST.get('klasifikasi')
        kelompok = request.POST.get('kelompok')
        tgl = request.POST.get('tanggal')
        no_surat = request.POST.get('no_surat')
        kepada = request.POST.get('kepada')
        prihal = request.POST.get('perihal')
        upload = edit_olah.upload_file.name
        today = edit_olah.today
 
        edit_olah = DatabaseSurat(
            id          = id_edit_olah_data,
            id_user     = id_user,  
            username    = username,
            surat       = surat,
            klasifikasi = klasifikasi,
            kelompok    = kelompok,
            tgl         = tgl,
            no_surat    = no_surat,
            kepada      = kepada,
            perihal     = prihal,
            upload_file = upload,
            today       = today,
            tahun       = year,
        )
        edit_olah.save()
        edit_olah.clean_fields()
        return redirect('olah_data')
   
    return render(request,'pages/olah_data.html')

@csrf_protect
@login_required(login_url="/accounts/login/")
def delete_olah_data(request, id_delete_olah_data):
    id_olah_data = request.user.pk
    id_username = request.user
    delete_olah_data = DatabaseSurat.objects.get(pk = id_delete_olah_data).id
    upload_file_files   = DatabaseSurat.objects.get(pk = id_delete_olah_data)
    
    now = datetime.now()
    year = now.strftime("%Y")

    if request.method == 'POST':
        upload_file_files.upload_file.delete()

        id_user = int(id_olah_data)
        username = str(id_username)
        surat = request.POST.get('surat')
        klasifikasi = request.POST.get('klasifikasi')
        kelompok = request.POST.get('kelompok')
        tgl = request.POST.get('tanggal')
        no_surat = request.POST.get('no_surat')
        kepada = request.POST.get('kepada')
        prihal = request.POST.get('perihal')
        hari_ini =    upload_file_files.today
       
        edit_olah = DatabaseSurat(
            id          = delete_olah_data,
            id_user     = id_user,  
            username    = username,
            surat       = surat,
            klasifikasi = klasifikasi,
            kelompok    = kelompok,
            tgl         = tgl,
            no_surat    = no_surat,
            kepada      = kepada,
            perihal     = prihal,
            # upload_file = upload_file,
            today       = hari_ini,
            tahun       = year,
        )
        edit_olah.delete()
        return redirect('olah_data')
    
    return render(request,'pages/olah_data.html')


def hari_ini(request):
    id_username = request.user.pk

    hari_ini = date.today()
    query_hari_ini = DatabaseSurat.objects.filter(id_user = id_username , today = hari_ini ).values()  

    # surat = NamaSurat.objects.filter(id_user = id_username).values_list("nama_surat" , flat=True )
    klasifikasi = KlasifikasiSurat.objects.filter(id_user = id_username).values_list("nama_klasifikasi" , flat=True)
    kelompok = KelompokSurat.objects.filter(id_user = id_username).values_list("nama_kelompok", flat=True)


    # print(query_hari_ini)

    context = {
        'page_title' : 'Hari Ini',
        'datasemuasurat' : query_hari_ini,
        # 'surat'          : surat,
        'klasifikasi'    : klasifikasi,
        'kelompok'       : kelompok,
    }

    return render(request , 'pages/hari_ini.html', context)

def laporan_harian(request):
    all_users = list(User.objects.values_list('username', flat=True))
    hari_ini = date.today()
    
    label = []
    y_masuk = []
    y_keluar = []
    jumlah_surat = []
    harian_temp = []
       
    try : 
        if request.method == 'POST':
            harian = request.POST.get('lapor_per_hari')
            hari = parse_date(harian)
            harian_temp.append(hari)
                        
            for i in all_users:
                label.append(i)
                surat_masuk = DatabaseSurat.objects.filter(username = i, surat = 'Masuk', today =  hari ).count()
                y_masuk.append(surat_masuk)
                surat_keluar = DatabaseSurat.objects.filter(username = i, surat = 'Keluar' , today = hari ).count()
                y_keluar.append(surat_keluar)

                temp_jumlah = surat_masuk + surat_keluar
                jumlah_surat.append(temp_jumlah)
            
        else:

            for i in all_users:
                label.append(i)
                surat_masuk = DatabaseSurat.objects.filter(username = i, surat = 'Masuk', today =  hari_ini ).count()
                y_masuk.append(surat_masuk)
                surat_keluar = DatabaseSurat.objects.filter(username = i, surat = 'Keluar' , today = hari_ini ).count()
                y_keluar.append(surat_keluar)

                temp_jumlah = surat_masuk + surat_keluar
                jumlah_surat.append(temp_jumlah)
    except:
        pass

    list_jumlah = zip(label , jumlah_surat)
    surat = dict(list_jumlah)
    surat_tersedia = sum(y_masuk) + sum(y_keluar)

    context = {
        'page_title' : 'Laporan Harian',
        'label' : label,
        'y_masuk' : y_masuk,
        'y_keluar' : y_keluar,
        'jumlah' :  surat,
        'hari_ini' : hari_ini,
        'harian'  : harian_temp,
        'tersedia' : surat_tersedia
    }

    return render(request , 'pages/laporan_harian.html', context)

def laporan_bulanan(request):
    now = datetime.now()
    month = now.strftime("%m")
    year = now.strftime("%Y")

    label = []
    y_masuk = []
    y_keluar = []
    jumlah_surat = []

    month_temp = []
    year_temp = []
    
    all_users = list(User.objects.all().values_list('username', flat=True ))
    data_tahun = list(DatabaseSurat.objects.all().values_list('tahun', flat=True).distinct())

    try:
        if request.method == 'POST':
            bulanan = request.POST.get('bulan')
            tahun = request.POST.get('tahun')

            datetime_object = datetime.strptime(bulanan, "%m")
            month_name = datetime_object.strftime("%B")
            month_temp.append(month_name)

            year_temp.append(tahun)

            for i in all_users:
                label.append(i)
                surat_masuk = DatabaseSurat.objects.filter(username = i , surat = 'Masuk', today__month = bulanan , today__year = tahun).count()
                y_masuk.append(surat_masuk)
                surat_keluar = DatabaseSurat.objects.filter(username = i, surat = 'Keluar' , today__month = bulanan , today__year = tahun).count()
                y_keluar.append(surat_keluar)

                temp_jumlah = surat_masuk + surat_keluar
                jumlah_surat.append(temp_jumlah)

        else:
            datetime_object = datetime.strptime(month, "%m")
            month_name = datetime_object.strftime("%B")
            month_temp.append(month_name)

            year_temp.append(year)

            for i in all_users:
                label.append(i)
                surat_masuk = DatabaseSurat.objects.filter(username = i , surat = 'Masuk', today__month = month).count()
                y_masuk.append(surat_masuk)
                surat_keluar = DatabaseSurat.objects.filter(username = i, surat = 'Keluar' , today__month = month).count()
                y_keluar.append(surat_keluar)

                temp_jumlah = surat_masuk + surat_keluar
                jumlah_surat.append(temp_jumlah)

    except:
        pass

    
    list_jumlah = zip(label , jumlah_surat)
    surat = dict(list_jumlah)
    surat_tersedia = sum(y_masuk) + sum(y_keluar)

    month_year = zip(month_temp, year_temp)
    final_month_year = dict(month_year)

    context = {
        'page_title' : 'Laporan Bulanan',
        'label' : label,
        'y_masuk' : y_masuk,
        'y_keluar' : y_keluar,
        'jumlah' :  surat,
        'tahun_data' : data_tahun,
        'tersedia' : surat_tersedia,
        'bulan_ini' : month,
        'bulan_tahun' : final_month_year
    }

    return render(request , 'pages/laporan_bulanan.html', context)

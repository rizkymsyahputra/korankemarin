#!/bin/python

#============================================================
# Mengimport modul modul yang di perlukan
import urllib
import urllib.request
import os
import time

# Ambil jam, lalu di pecah-pecah kan per variable
gettime=time.strptime(time.ctime())
tahun= str(gettime[0])
bulan= str(gettime[1])
tanggal= str(gettime[2])
jam= str(gettime[3])
menit= str(gettime[4])

# Format nama folder per harian
foldername= tahun+"_"+bulan+"_"+tanggal

# Cek folder untuk mengisi filenya apa sudah ada atau belum
while True:
    try:
        os.chdir("Serambi_Epapers")
        break
    except FileNotFoundError:
        os.system("mkdir Serambi_Epapers")
        os.chdir("Serambi_Epapers")
        break

while True:
    try:
        os.chdir(foldername)
        break
    except FileNotFoundError:
        os.mkdir(foldername)
        os.chdir(foldername)
        break

# Cek jam dan memberi informasi apakah yang akan di download koran kemarin atau hari ini
if int(jam) > 16:
    print("++ FETCHING ALL PAGE OF TODAY SERAMBI EPAPER ++")
else:
    print("++ FETCHING ALL PAGE OF YESTERDAY SERAMBI EPAPER ++")


# Eksekusi download file halaman pertama sampai halaman terakhir
for page in range(1,25) :
    # Nomer Halaman yang kurang dari 10, di beri digit 0 sebelum nya
    if page<10:
        page=str(page)
        page="0"+page
    # Format Penamaan File
    filename= "SERAMBI_EPAPER_"+tahun+"_"+bulan+"_"+tanggal+"_PAGE"+str(page)+".jpg"
    # Menampilkan informasi halaman berapa yang sedang di download
    print("> DOWNLOADING "+filename)
    # Eksekusi download per halaman
    urllib.request.urlretrieve("https://s3-ap-southeast-1.amazonaws.com/tribun-3/epaper/aceh/"+str(page)+".jpg", filename)

# Selesai
print("++ DONE!! ENJOY YOUR DAY ++")

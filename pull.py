#!/bin/python
import urllib
import urllib.request
import os
import time

gettime=time.strptime(time.ctime())

tahun= str(gettime[0])
bulan= str(gettime[1])
tanggal= str(gettime[2])

print("++ WELCOME TO KORANKEMARIN ... WE'RE GOING TO FETCH ALL PAGE OF YESTERDAY SERAMBI NEWS ++")

for page in range(1,25) :
    if page<10:
        page=str(page)
        page="0"+page
    filename= "SERAMBI_EPAPER_"+tahun+"_"+bulan+"_"+tanggal+"_PAGE"+str(page)+".jpg"
    print("=>DOWNLOADING "+filename)
    urllib.request.urlretrieve("https://s3-ap-southeast-1.amazonaws.com/tribun-3/epaper/aceh/"+str(page)+".jpg", filename)

print("++ DONE!! ENJOY YOUR DAY ++")

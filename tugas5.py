
import time
import os

while True:
    print(" ")
    print("1. balik kata")
    print("2. info + saran")
    print("3. keluar")
    awal = input("masukan pilihan anda -> ")
    
    if awal=="1":
        a = input("masukan sesuatu-> ")
        file = open("data.txt",'w')
        file.write(a)
        file.close()
        b = os.popen("rev data.txt").read()
        time.sleep(1)
        print("kata awal = " , a)
        time.sleep(1)
        print("kata di balik = ", b)
        time.sleep(1)
        if a==b:
            print("ok")

        else:
            print("salah")

    if awal=="2":
        print(" ")
        print("disini saya praktek menggunakan linux jadi di sarankan untuk menjalankan program ini di linux juga, agar script dpt jalan secara lancar")
        print(" ") 

    if awal=="3":
        print(" ")
        print("Sampai Jumpa Lagi :) ")
        break






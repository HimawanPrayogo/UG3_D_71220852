
nama=input("Masukkan Nama Lengkap Anda\t\t\t:")
prodi=input("Masukkan Prodi Anda\t\t\t\t:")
nilai=input("Masukkan Nilai (dalam Huruf) yang Anda Dapat\t:")

try:
    nama=str(nama)
    prodi=str(prodi)
    nilai=str(nilai)
    daftar=[4.0,3.75,3.25,3.0,2.75,2.25,2.0,1.0,0]

    if nilai=="A" or nilai=="a":
        print("Nilai anda adalah",daftar[0],", tbl tbl serem banget lohh")

    elif nilai=="A-" or nilai=="a-":
        print("Nilai anda adalah",daftar[1],", kamu keren!")

    elif nilai=="B+" or nilai=="b+":
        print("Nilai anda adalah",daftar[2],", anda kurang bersemangat")

    elif nilai=="B" or nilai=="b":
        print("Nilai anda adalah",daftar[3],", usaha anda kurang")

    elif nilai=="B-" or nilai=="b-":
        print("Nilai anda adalah",daftar[4],", kurang semangat belajar nihh")

    elif nilai=="C+" or nilai=="c+":
        print("Nilai anda adalah",daftar[5],", anda kurang kerja keras")

    elif nilai=="C" or nilai=="c":
        print("Nilai anda adalah",daftar[6],", anda kurang beruntung")

    elif nilai=="D" or nilai=="d":
        print("Nilai anda adalah",daftar[7],", apakah sudah ada pikiran untuk pindah jurusan?")

    elif nilai=="E" or nilai=="e":
        print("Nilai anda adalah",daftar[8],", niat kuliah nggak sih???")


    else:
        print("inputan nilai yang anda masukkan tidak valid")
        

except:
    print("inputan anda salah")

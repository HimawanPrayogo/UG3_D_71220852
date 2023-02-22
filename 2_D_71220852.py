
nomor=input("Masukkan Plat Nomor :").split()

try:
    b=nomor[1]
    b=int(b)

    if b>=0 and b<=3000:
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif b>=3001 and b<=4000:
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif b>=4001 and b<=5000:
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")
    
except:
    print("Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan")

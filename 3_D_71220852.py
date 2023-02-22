
awal=input("Masukkan awal deret:")
akhir=input("Masukkan akhir deret:")

try:
    awal=int(awal)
    akhir=int(akhir)

    for i in range(awal,akhir,1):
        if (i%6==0) or (i%8==0):
            continue
        print(i,"",end="")
        


except:
    print("inputan anda salah")

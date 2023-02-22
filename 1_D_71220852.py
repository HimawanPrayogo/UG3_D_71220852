
hujan=input("Masukkan nilai curah hujan :")


try:
    hujan=float(hujan)
    print("Cuaca Terang/ Berawan") if hujan==0 else print("curah hujan ringan") if (hujan>=0.5 and hujan<=20) else print("curah hujan sedang") if (hujan>=21 and hujan<=50) else print("curah hujan lebat") if (hujan>=51 and hujan<=100) else print("curah hujan ekstrem")

except:
    print("inputan anda salah")

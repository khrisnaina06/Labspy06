print("=== DAFTAR NILAI MAHASISWA ===")
print()

daftar = {}
    

def no_data():
    print("DAFTAR NILAI")
    print("------------")
    print(72*"=")
    print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} |   {5:^12}  |".format("NIM", "NAMA", "TUGAS", "UTS", "UAS", "NILAI AKHIR"))
    print(72*"=")
    print("|                             TIDAK ADA DATA                           |")
    print(72*"=")
    print()
            

def lihat():
    if len(daftar) <= 0:
        no_data()
    else:
        print("DAFTAR NILAI")
        print("------------")
        print(72*"=")
        print("| {0:^10} | {1:^10} | {2:^6} | {3:^6} | {4:^6} |   {5:^12}  |".format("NIM", "NAMA", "TUGAS", "UTS", "UAS", "NILAI AKHIR"))
        print(72*"=")
        for z in daftar.items():
            print(f"| {z[1][0]:>10} | {z[0]:>10} | {z[1][1]:>6} | {z[1][2]:>6} | {z[1][3]:>6} |   {z[1][4]:>12}  |") 
            print(72*"=")
        print()
            
            
def tambah():
    print("TAMBAH DATA")
    print("------------")
    nama = input("Nama Mahasiswa\t: ")
    nim = int(input("NIM Mahasiswa\t: "))
    tugas = int(input("Nilai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
    daftar[nama] = [nim, tugas, uts, uas, akhir]
    print()


def ubah():
    if len(daftar) <= 0:
        no_data()
    else :
        print("UBAH DATA")
        print("-----------")
        nama = input("Nama Anda\t: ")
        if nama in daftar.keys():
            nim = int(input("NIM Mahasiswa\t: "))
            tugas = int(input("Nilai Tugas\t: "))
            uts = int(input("Nilai UTS\t: "))
            uas = int(input("Nilai UAS\t: "))
            akhir = (tugas*30/100) + (uts*35/100) + (uas*35/100)
            daftar[nama] = [nim, tugas, uts, uas, akhir] 
            print()


def hapus():
    if len(daftar) <=0:
        no_data()
    else:
        print("HAPUS DATA")
        print("-----------")
        nama = input("Nama Anda\t: ")
        if nama in daftar.keys():
            del daftar[nama]
            print()


Loop = True
while Loop:
    print("Pilih Menu")
    print()
    tanya = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar] : ")
    print()

    if tanya=="l" or tanya=="L":
        lihat()
        
    elif tanya=="t" or tanya=="T":
        tambah()
        
    elif tanya=="u" or tanya=="U":
        ubah()
        
    elif tanya=="h" or tanya=="H":
        hapus()
        
    elif tanya=="k" or tanya=="K":
        print("Program Selesai")
        Loop = False
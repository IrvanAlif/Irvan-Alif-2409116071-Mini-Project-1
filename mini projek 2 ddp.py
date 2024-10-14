from prettytable import PrettyTable

def admin():
    return {"username": "admingg", "password": "999"}

def buat_membership():
    nama_member = input("Masukkan nama member: ")
    temukan = False
    for member in membership:
        if member["member"] == nama_member:
            temukan = True
            break
    if temukan:
        jenis_membership = input("Pilih membership (SILVER GOLD PLATINUM):").upper()
        for member in membership:
            if member["member"] == nama_member:
                member["jenis"] = jenis_membership
                print("Membership berhasil ditambahkan")
                return
    else:
        print("TIDAK ADA MEMBER DENGAN NAMA TERSEBUT ")
def cek_membership():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Jenis Membership", "Transaksi"]

    for no in range(len(membership)):
        member = membership[no]
        tabel.add_row([no + 1, member["member"], member["jenis"], member["transaksi"]])

    print(tabel)

def ubah_membership():
    cari = str(input("SIAPA MEMBER YANG INGIN DI UBAH?: "))
    member_ditemukan = False
    for member in membership:
        if member["member"] == cari:
            member_ditemukan = True
            pilihan_diganti = str(input("Pilih apa yang mau di ganti: 1.Nama  2.Jenis Membership  3.Transaksi:"))

            if pilihan_diganti == "1":
                nama_baru = str(input("nama baru member:"))
                member["member"] = nama_baru
                print("BERHASIL MENGGANTI NAMA")
                break
            elif pilihan_diganti == "2":
                membership_baru = str(input("Pilih membership baru: SILVER, GOLD, atau PLATINUM:")).upper()
                member["jenis"] = membership_baru
                print("BERHASIL MENGGANTI MEMBERSHIP")
                break
            elif pilihan_diganti == "3":
                ubah_transaksi = int(input("masukkan nominal : "))
                member["transaksi"] = ubah_transaksi
                print("BERHASIL MENGUBAH SALDO")
                break
            else:
                print("PILIHAN HARUS 1 2 3")
            break

    if not member_ditemukan:
        print("EROR")
        print(f" nama{cari} tidak di temukan")
        
def hapus_membership():
    hapus = str(input("Hapus member gym: "))
    for member in membership:
        if member["member"] == hapus:
            
            print("Berhasil menghapus nama", hapus)
            break
    else:
        print("tidak ada member dengan nama ", hapus)

def menu_admin():
    while True:
        print("pilihan")
        print("1.buat membership")
        print("2.lihat daftar membership")
        print("3.ubah nama, membership, dan transaksi")
        print("4.hapus anggota")
        print("5.keluar")
        print("6.keluar dari program")
        
        pilih_menu_admin = str(input("SILAHKAN PILIH 1 - 6 : "))
        if pilih_menu_admin == "1":
            buat_membership()
        elif pilih_menu_admin == "2":
            cek_membership()
        elif pilih_menu_admin == "3":
            ubah_membership()
        elif pilih_menu_admin == "4":
            hapus_membership()
        elif pilih_menu_admin == "5":
            print()
            break
        elif pilih_menu_admin == "6":
            print()
            exit()
            break
        else:
            print("pilihan tidak ada")
            
def transaksi_user():
    jumlah_transaksi = int(input("Masukkan nominal transaksi: "))
    nama_member = str(input("Masukkan nama member: "))
    transaksi_ditemukan = False

    for member in membership:
        if member["member"] == nama_member:
            member["transaksi"] += jumlah_transaksi
            transaksi_ditemukan = True
            print(" transaksi berhasil")
            break
    if not transaksi_ditemukan:
        print("Member tidak ditemukan.")

def menu_user():
    while True:
        print("Pilihan:")
        print("1.Transaksi")
        print("2.Keluar")
        print("3.keluar dari program")
        pilih_menu_user = str(input("Apakah ingin melakukan transaksi atau keluar? (1/2/3): ")).lower()
        if pilih_menu_user == "1":
            transaksi_user()
        elif pilih_menu_user == "2":
            print("Keluar")
            break
        elif pilih_menu_user == "3":
            print("exit")
            exit()
            break
        else:
            print("Pilihan tidak ada")

user = []
membership =[]

def login_awal():
    akun = input("apakah anda memiliki akun? y/n: ").lower()
    print("===========LOGIN==========")
    if akun == "y":
        username = str(input("masukkan username anda: "))
        password = (input("masukkan password anda: "))
        
        if username == admin()["username"] and password == admin()["password"]:
            print("SELAMAT BEKERJA!!!!")
            menu_admin()
        else:
            pelanggan = False
            for catatan in user:
                if username == catatan["username"] and password == catatan["password"]:
                    print("SIAP OLAHRAGA HARI INI?")
                    menu_user()
                    pelanggan = True
                    break
            if pelanggan:
                print()
            else:
                print("waduhhh kamu salah nih, coba ingat-ingat lagi")
                
    elif akun == "n":
        daftar_username = str(input("masukkan nama anda: "))
        password = (input("masukkan password yang kuat: "))

        if any(catatan["username"] == daftar_username for catatan in user):
            print("username sudah ada")
        else:
            user.append({"username": daftar_username, "password": password})
            membership.append({"member": daftar_username, "jenis":"", "transaksi":0})
            print("selamat datang user baru")
    else:
        print("PILIHAN HANYA BISA y ATAU n")

while True:
    login_awal()

IRVAN ALIF
KELAS B 
2409116071

FLOWCHART
![Untitled Diagram drawio (2)](https://github.com/user-attachments/assets/2e341ceb-5b19-4474-8d37-46824e254641)

gambar 1

line 1

- code(from prettytable import PrettyTable) untuk mengimport prettytable agar bisa membuat tabel


![image](https://github.com/user-attachments/assets/80a74881-579b-4fad-9da0-242d7cafd126)


gambar 2

line 3 - 4

- code (def admin():
    return {"username": "admingg", "password": "999"})dictionary yang berisi username dan password admin untuk login ke menu administrasi

![image](https://github.com/user-attachments/assets/43f6d409-d786-437d-bf75-cbe8478e3a96)

gambar 3 

line 6 - 21

-  mencari apakah nama member sudah ada dalam list membership
- Jika nama member ditemukan, pengguna dapat menambahkan jenis membership. Jika tidak, muncul pesan error
- code(def buat_membership():) untuk membuat fungsi create
- code(input) untuk mengetik nama atau jenis yang ingin di cari
- code (temukan = False)di gunakan untuk mencari nama yang di inputkan
- code (for member in membership:) artinya list member di dictionery membership
- (if member["member"] == nama_member:) artinya jika nama yang di tulis di temukan di list member key member
- (member["jenis"] = jenis_membership) artinya jenis membership yang di ketik dan ada di list member  key jenis
- (return) buat manggil kembali nilai

![image](https://github.com/user-attachments/assets/f27a341f-d216-41eb-bbbf-81c782113d57)


gambar 4

line 22 - 30

- menampilkan daftar membership dalam bentuk tabel dengan kolom: No, Nama, Jenis Membership, dan Transaksi
- (  tabel = PrettyTable()) untuk memunculkan tabelnya
- (tabel.field_names = ["No", "Nama", "Jenis Membership", "Transaksi"]) untuk bagian atas tabel
- (for no in range(len(membership)):
        member = membership[no]
        tabel.add_row([no + 1, member["member"], member["jenis"], member["transaksi"]])) untuk memasukkan list ke tabel secara berurut
  -( print(tabel)) memunculkan tabel di terminal 
  

![image](https://github.com/user-attachments/assets/f62d68eb-8cc8-45fd-aab0-2252bef5bbd5)



gambar 5


line 32 - 61

- memungkinkan admin untuk mengubah nama, jenis membership, atau transaksi pada anggota yang sudah ada
- 9    cari = str(input("SIAPA MEMBER YANG INGIN DI UBAH?: "))
    member_ditemukan = False
    for member in membership:
        if member["member"] == cari:
            member_ditemukan = True
            pilihan_diganti = str(input("Pilih apa yang mau di ganti: 1.Nama  2.Jenis Membership  3.Transaksi:"))) untu mencari nama yang datanya mau di ubah
- (
            if pilihan_diganti == "1":
                nama_baru = str(input("nama baru member:"))
                member["member"] = nama_baru
                print("BERHASIL MENGGANTI NAMA")
                break) untuk mengganti nama
  - (           elif pilihan_diganti == "2":
                membership_baru = str(input("Pilih membership baru: SILVER, GOLD, atau PLATINUM:")).upper()
                member["jenis"] = membership_baru
                print("BERHASIL MENGGANTI MEMBERSHIP")
                break) untuk mengubah membership , str itu dalam bentuk kata
    -(   elif pilihan_diganti == "3":
                ubah_transaksi = int(input("masukkan nominal : "))
                member["transaksi"] = ubah_transaksi
                print("BERHASIL MENGUBAH SALDO")
                break) untuk mengbah transaksi, int dalam bentuk angka

![image](https://github.com/user-attachments/assets/8a3a0e1a-a375-4ca4-b300-5b9fcd17b132)


gambar 6

line 63 - 71

- mencari dan menghapus anggota dari daftar membership berdasarkan nama
- ( membership.remove(member) fungsi utamanya yang di gunakan untuk menghapus


![image](https://github.com/user-attachments/assets/a655ae7a-e6d3-4bfa-91cf-7918c314ec99)


gambar 7 

line 73 - 100


- menampilkan menu untuk admin dan memungkinkan admin memilih untuk membuat, melihat, mengubah, atau menghapus anggota, atau keluar dari program
- di sini semua fungsi di panggil


![image](https://github.com/user-attachments/assets/548b8bd4-ac84-40ef-b67b-03489a6db476)


gambar 8

line 102 - 114


 - menambahkan jumlah transaksi pada anggota yang ditemukan berdasarkan nama yang diinput
 - ini lanjutan setelah masuk ke menu ser dan memilih transaksi
 - di sini melakukan transaksinya 


![image](https://github.com/user-attachments/assets/d514dcd5-1c72-4ba2-8d68-d11567ed5b9e)



gambar 9 

line 116 - 133


- menampilkan menu transaksi bagi user. User bisa memilih untuk melakukan transaksi atau keluar
- untuk menambahkan transaksi user berdasarkan list member key transaksi  dan semua transaksi berturut turut akan di tambah 


![image](https://github.com/user-attachments/assets/b778c333-a3a9-4737-acc1-6bbf2147dd31)


gambar 10

line 135 - 136

- dictionery untuk menyimpan semua key dan value

![image](https://github.com/user-attachments/assets/72a9be31-3132-4931-a3b2-4b2c6c85fa79)


gambar 11 

line 138 - 172

- memungkinkan pengguna untuk login atau mendaftar sebagai user baru
- jika tidak memiliki akun atau pengguna baru maka harus membuat akun baru
- jika login sebagaai admin maka melanjutkan ke fungsimenu admin
- jika login sebagai user maka melanjutkan ke menu user


![image](https://github.com/user-attachments/assets/7777ccb2-9e0e-4d59-a85b-35328af6b68d)
![image](https://github.com/user-attachments/assets/796c49b5-cb7d-4d7b-b654-471c2ae97b6e)



gambar 12 

line 174 -175

-  while true untuk melakukan perulangan
- memanggil fungsi login untuk di jalankan


![image](https://github.com/user-attachments/assets/66eda3dd-cc73-4487-a9fc-19fbedeb1561)



gambar 13

OUTPUT

![image](https://github.com/user-attachments/assets/d4a0b6b9-834e-4d50-a54b-23ca89556f42)
![image](https://github.com/user-attachments/assets/af157fba-142c-4105-94d1-95dc5eb6c1d6)
![image](https://github.com/user-attachments/assets/c91db8d1-35f4-4bfb-9357-0e109afdadd2)
![image](https://github.com/user-attachments/assets/0b07a7d2-7a68-495e-9472-d7d4fa2af66f)






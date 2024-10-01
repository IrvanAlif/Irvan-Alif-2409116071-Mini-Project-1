##### Praktikum PosTest 1
Irvan Alif | 2409116071 | Sistem informasi kelas B
## FLOWCHART

![Praktikum PosTest 1() drawio (1)](https://github.com/user-attachments/assets/d1a04ff9-88a2-4993-8eb5-b45b536ea026)

## DETAIL
8-16 (Login loop):

a. Membuat variabel Nama dan NIM

B. Memulai perulangan untuk proses login.

C. Menampilkan pesan untuk meminta USERNAME dan PASSWORD, lalu menunggu input dari pengguna.

![image](https://github.com/user-attachments/assets/ae910baa-0ccf-4dab-a228-562761a7aa1f)

## DETAIL
18-25 (pengecekan username dan password):

a. Mengecek apakah USERNAME dan PASSWORD sesuai (disini username "I" dan password "71").

b. Jika benar, menampilkan pesan selamat datang dan NIM, lalu keluar dari perulangan.

c. Jika salah, kembali ke awal input

![image](https://github.com/user-attachments/assets/ca50529a-7d94-4d7b-b9f3-a052161ae886)

## DETAIL
27-33 (penginputan gaji loop):

a. Memulai perulangan untuk menghitung gaji karyawan.

b. Meminta input jam kerja dan tarif gaji.

c. Menghitung bonus sebesar 10% dari gaji.

 ![image](https://github.com/user-attachments/assets/85813747-23eb-4c42-b78d-1f1f9614fda6)


## DETAIL
35-41 (penentuan gaji)

a. Mengecek apakah jam kerja lebih dari atau sama dengan 160 jam. Jika ya, menampilkan gaji dengan bonus.

b. Jika jam kerja kurang dari 160 jam, menampilkan gaji tanpa bonus.

![image](https://github.com/user-attachments/assets/24625637-7bff-4871-893c-476ccb3c2e71)


## DETAIL

print("______________________________ \n")
print(" Mini Project 1 (NIM Ganjil)")
print("         Irvan Alif")
print("         2409116071")
print("______________________________ \n")

NAMA = "Irvan Alif"
NIM = 2409116071

while True:
    print("           LOGIN            ")
    print("MASUKKAN USENAME DAN PASSWORD")
    USERNAME = str(input("Username:"))
    PASSWORD = int(input("Password:"))
    
    if USERNAME == "I" and PASSWORD == 71: 
        print("____________________________ \n")
        print("Halo selamat datang, " + NAMA)
        print(NIM)
        break
        
    else:
        print("login gagal, unsername atau password salah")  

while True:
    print("_______________________________________________ \n")
    print("MENGHITUNG JUMLAH GAJI YANG DI TERIMA KARYAWAN")
    jam_kerja = int(input("masukkan jam kerja:"))
    gaji = int(input("masukkan tarif kerja:"))
    bonus = 0.1 * gaji
    if jam_kerja >= 160:
        print("Gaji anda + bonus")
        print(int(bonus + gaji))
    elif jam_kerja < 160:
        print("Gaji anda")
        print(int(gaji))
    ulangi_perintah = str(input("ingin menghitung ulang gaji?(y/n) ")).lower()
    if ulangi_perintah == "y":
        print()
    elif ulangi_perintah == "n":
        print("Selesai menghitung gaji")
        break
    else:
        print("EROR")
        break








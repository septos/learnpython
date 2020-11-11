print("""
============================================================
    Nama : 
    Kelas : 
============================================================
Pilih menu :
1. Tampilkan data belanja saat ini
2. Ubah data belanja
3. Tambah data belanja
4. Hapus data belanja
============================================================
""")
item = ['Lemari','Balok Besi','Lem Kayu','Mesin Bubut']

menu = input("Masukan pilihan menu ? ")


if menu == '1':
    print(item)
elif menu == '2':
    inputubah = input('Silahkan masukan index yang akan diubah ? ')
    print(inputubah)
    ubahcetak = input("Silahkan masukan data baru = ")
    print(ubahcetak)
#ubah
    item.pop(int(inputubah))
    item.insert(int(inputubah), ubahcetak)
    print(item)
elif menu == '3':
    item2 = input("Silahkan masukan data baru = ")
    x = item.copy()
    print('Sebelum ditambahkan : ',x)
    item.append(item2)
    print('Sesudah ditambahkan : ',item)
elif menu == '4':
    x = item.copy()
    print("Sebelum dihapus ",x)
    ab = input("Silahkan masukan data yang akan dihapus ? ")
    item.remove(ab)
    print("Setelah dihapus ",item)
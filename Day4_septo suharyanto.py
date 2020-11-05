'''1) Membuat Program dengan menggunakan fungsi / prosedure sebagai berikut:

    Buatlah sebuah program untuk menentukan bilangan genap dan bilangan ganjil
    Buatlah sebuah sebuah program dengan sebuah fungsi yang dapat mengkonversikan angka bulan menjadi nama bulan.
    Buatlah sebuah program utama yang digunakan untuk memutar 3 buah bilangan. contoh: A=2, B=1, C=3 di tukar menjadi A=3, B=2, C=1'''
print("-->berikut program ke 1")
try:
    bilangan = int(input("masukan bilangan: "))
    if bilangan == 0:
        print("bilangan 0")
    elif bilangan % 2 == 0:
        print("bilangan genap")
    else:
        print("bilangan ganjil")
except ValueError:
    print("anda harus memasukan angka")

print("\n-->berikut program kedua")
bulan = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember", }

angkabulan = int(input("Masukan angka bulan(1-12): "))

if angkabulan == 0:
    print("anda memasukan angka 0")
elif angkabulan <= 12:
    while angkabulan:
        # if nilai == angkabulan:
        print(f"bulan ke- {angkabulan} adalah bulan: ", bulan[angkabulan])
        break
else:
    print("silahkan masukan angka dari 1-12")

    # A = 2, B =1, C=3 di tukar menjadi A = 3, B = 2, C =1
print("\n-->berikut program ketiga")
A = int(input("masukan angka A: "))
B = int(input("masukan angka B: "))
C = int(input("masukan angka C: "))

print(f"anda memasukan angka A:{A}, B:{B}, C:{C}")


def putarbilangan():
    global A
    global B
    global C
    A, B, C = C, A, B


while True:
    tanya = input("apakah ingin diputar (yes/no) ? ")
    if tanya == "yes":
        print("ok")
        putarbilangan()
        print(f"setelah diputar A:{A} B:{B} C:{C}")
        break
    elif tanya == "no":
        print("program selesai")
        break
    else:
        print("anda salah memilih")
        break

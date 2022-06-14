import csv
import hashlib

def readFile(namafile):
    # Fungsi untuk membuka dan membaca file 'namafile'

    # Kamus lokal
    # df : file
    # reader : Hasil pembacaan data csv

    # Algortima lokal
    df = open(namafile)
    reader = csv.reader(df, quoting=csv.QUOTE_NONE)
    return reader

def writeFile(namafile,nama_data):
    #Fungsi untuk menulis data pada database

    # Kamus lokal
    # write_obj : file
    # Data_writer : file yang siap untuk di-write

    # Algoritma lokal
    with open(namafile, 'w', newline='') as write_obj:
        Data_writer = csv.writer(write_obj)
        for row in nama_data:
            Data_writer.writerow(row)
    return

def panjang(array):
    # Fungsi untuk menghitung panjang array

    # Kamus lokal
    # i : integer

    # Algoritma
    i = 0
    for row in array:
        i = i+1
    return i

def nambahdata(array,newdata):
    # Menyimpan newdata ke dalam array dan mengembalikan array yang telah ditambah newdata.

    # Kamus lokal

    # Algoritma
    array = array + ['']
    array[panjang(array)-1] = newdata
    return (array)

def convertkearray(reader):
    # Mengubah file csv yang sudah dibaca menjadi array

    # Kamus lokal
    # array : array
    # i,j : integer

    # Algoritma lokal
    array = []
    for row in reader:
        array = nambahdata(array, row)
    return (array)

def make_pw_hash(password):
    #Fungsi untuk enkripsi password menggunakan library hashlib

    #KAMUS LOKAL
        #Tidak memerlukan kamus lokal

    #ALGORITMA
    return hashlib.sha256(str.encode(password)).hexdigest()

def cekuname(Username):
    # Fungsi untuk memeriksa apakah parameter Username sudah terdaftar pada database user.csv
    # Menghasilkan True jika Username terdapat pada database dan False jika tidak

    # Kamus Lokal
    #N,i : integer
    #found : boolean

    # Algoritma Lokal
    N = panjang(userdata)
    found = False
    i = 1
    while i<N and found == False:
        if userdata[i][3] == Username:
            found = True
        i=i+1
    return found

def isvalidaccount(Username,Password):
    # Fungsi untuk mencek apakah akun sudah terdaftar pada database, dan inputan username dan password telah sesuai.

    # KAMUS LOKAL
    # i : intefer
    # valid : boolean

    # Algoritma lokal
    global name
    valid = False
    i = 1
    while i < panjang(userdata) and valid == False:
        if (userdata[i][3] == Username) and (userdata[i][4] == Password):
            valid = True
            name = userdata[i][0]
        else:
            i = i + 1
    return valid

def cekRole(Username):
    # Fungsi untuk cek Role pengguna lalu mengeluarkan output role pengguna (Admin atau Pemain)
    for i in userdata:
        if Username == i[3]:
            role = i[5]
    return role

def load():
    # Prosedur untuk melakukan load data
    # Data pada file akan disimpan dalam sebuah array yang dapat diproses

    # Kamus lokal

    # Algoritma lokal
    global userdata, wahanadata, pembeliandata, penggunaandata, kepemilikandata, refunddata, kritiksarandata
    userdata = convertkearray(readFile(input("Masukkan nama File User: ")))
    wahanadata = convertkearray(readFile(input("Masukkan nama File Daftar Wahana: ")))
    pembeliandata = convertkearray(readFile(input("Masukkan nama File Pembelian Tiket: ")))
    penggunaandata = convertkearray(readFile(input("Masukkan nama File Penggunaan Tiket: ")))
    kepemilikandata = convertkearray(readFile(input("Masukkan nama File Kepemilikan Tiket: ")))
    refunddata = convertkearray(readFile(input("Masukkan nama File Refund Tiket: ")))
    kritiksarandata = convertkearray(readFile(input("Masukkan nama File Kritik dan Saran: ")))

    print()
    print("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")
    return

def signup():
    #Fungsi untuk melakukan sign up atau pendaftaran data pemain
    #Inputan data pemain yang sudah valid akan disave ke File user.csv

    # Kamus Lokal
        # Nama, Tanggal_Lahir, Tinggi_Badan, Username, Password, Role : string
        # Saldo : integer
        # new_data : List

    # ALGORTIMA
    print()
    Nama = input("Masukkan nama pemain: ")
    Tanggal_Lahir = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
    Tinggi_Badan = input("Masukkan tinggi badan pemain (cm): ")
    # Khusus input username perlu dilakukan validasi (input username tidak boleh sama dengan yang sudah terdaftar)
    Username = input("Masukkan username pemain: ")
    while cekuname(Username):
        print("Username sudah terdaftar. Mohon masukan username lain!")
        Username = input("Masukkan username pemain: ")
    Password = make_pw_hash(input("Masukkan password pemain: "))
    Saldo = 0
    Role = 'Pemain'
    gold = 'N'
    new_user = [Nama,Tanggal_Lahir,Tinggi_Badan,Username,Password,Role,Saldo,gold]
    global userdata
    userdata = nambahdata(userdata,new_user)
    print()
    print("Selamat menjadi pemain, "+Nama+". Selamat bermain.")
    return

def login():
    # Fungsi untuk melakukan login dengan memasukkan username dan password

    # Kamus lokal
    # Username, Password = string

    # Algoritma lokal
    global loggedin
    global Username
    print()
    Username = input("Masukkan username: ")
    Password = make_pw_hash(input("Masukkan password: "))
    while not isvalidaccount(Username, Password):
        print()
        if cekuname(Username):  # Username terdaftar namun password tidak sesuai
            print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami.")
        else:  # username tidak terdaftar
            print("Ups, username tidak ditemukan atau kamu tidak terdaftar dalam sistem kami.")
        print("Silahkan masukkan kembali Username dan Password.\n")
        Username = input("Masukkan username: ")
        Password = make_pw_hash(input("Masukkan password: "))
    print()
    print("Selamat bersenang-senang, " + name + "!")
    loggedin = True
    return

def cari_pemain():
    # Fungsi untuk melakukan pencarian pemain berdasarkan username pemain
    # Fungsi dapat dilakukan jika pengguna sudah melakukan login

    # Kamus Lokal
    # Username, nama, tanggal_lahir, tinggi : string

    # Algoritma lokal
    Username = input("Masukkan username: ")
    if cekuname(Username):
        for i in range(1, panjang(userdata)):
            if userdata[i][3] == Username:
                nama = userdata[i][0]
                tanggal_lahir = userdata[i][1]
                tinggi = userdata[i][2]
                print("Nama Pemain: " + nama)
                print("Tinggi Pemain: " + str(tinggi) + " cm")
                print("Tanggal Lahir Pemain: " + tanggal_lahir)
                break
    else:  # Username tidak ditemukan pada database
        print("Pemain tidak ditemukan.")
    return

def Save():
    # Fungsi untuk mengubah Array berisi data ke file csv agar tersimpan di database

    # Save ke Database File User
    File_User = input("Masukkan nama File User: ")
    writeFile(File_User,userdata)
    # Save ke Database File Wahana
    File_Wahana = input("Masukkan nama File wahana: ")
    writeFile(File_Wahana, wahanadata)
    # Save ke Database File Pembelian Tiket
    File_PembelianTiket = input("Masukkan nama File Pembelian Tiket: ")
    writeFile(File_PembelianTiket, pembeliandata)
    # Save ke Database File Penggunaan Tiket
    File_PenggunaanTiket = input("Masukkan nama File Penggunaan Tiket: ")
    writeFile(File_PenggunaanTiket, penggunaandata)
    # Save ke Database File Kepemilikan Tiket
    File_KepemilikanTiket = input("Masukkan nama File Kepemilikan Tiket: ")
    writeFile(File_KepemilikanTiket, kepemilikandata)
    # Save ke Database File Refund Tiket
    File_RefundTiket = input("Masukkan nama File Refund Tiket: ")
    writeFile(File_RefundTiket, refunddata)
    # Save Database File Kritik dan Saran
    File_KritikSaran = input("Masukkan nama File Kritik dan Saran: ")
    writeFile(File_KritikSaran, kritiksarandata)

    print()
    print("Data berhasil disimpan!")

def Exit():
    global loggedin
    # Fungsi untuk melakukan logout account yang telah logim.
    save = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)? ")
    if save == 'Y':
        Save()
    loggedin = False
    return


def tambah_wahana():
    if loggedin:
        print("Masukkan Informasi Wahana yang ditambahkan:")
        a = input("Masukkan ID Wahana: ")
        b = input("Masukkan Nama Wahana: ")
        c = input("Masukkan Harga Tiket: ")
        d = input("Batasan umur: ")
        e = input("Batasan tinggi badan: ")
        global new_wahana, wahanadata
        new_wahana = [a, b, c, d, e]
        wahanadata = nambahdata(wahanadata,new_wahana)
        print()
        print("Info wahana telah ditambahkan!")
    else:
        print("Silakan login terlebih dahulu.")
        login()
    return


def tiket_pemain():
    if loggedin:
        urname = input("Masukkan username: ")
        print("Riwayat:")
        for i in kepemilikandata:
            if (i[0] == urname):
                for j in wahanadata:
                    if (i[1] == j[0]):
                        print(str(i[1]) + ' | ' + str(j[1]) + ' | ' + str(i[2]))
    else:
        print("Silakan login terlebih dahulu.")
        login()


def riwayat_wahana():
    ide = input("Masukkan ID Wahana: ")
    print("Riwayat:")
    for row in penggunaandata:
        if (row[2] == ide):
            print(str(row[1]) + ' | ' + str(row[0]) + ' | ' + str(row[3]))

def topup():
    if loggedin:
        uname = input("Masukkan username: ")
        for i in range(0, panjang(userdata)):
            if (userdata[i][3] == uname):
                saldo = float(input("Masukkan saldo yang di-top up: "))
                newSaldo = float(userdata[i][6]) + saldo
                userdata[i][6] = newSaldo
        print()
        for row in userdata:
            if (row[3] == uname):
                print("Top up berhasil. Saldo " + str(row[0]) + " bertambah menjadi " + str(round(row[6])))

    else:
        print("Silakan login terlebih dahulu.")
        login()


def tiket_hilang():
    uname = input("Masukkan username: ")
    tanggal = input("Tanggal kehilangan tiket: ")
    aidi = input("ID wahana: ")

    for i in range(0, panjang(kepemilikandata)):
        if (kepemilikandata[i][0] == uname):
            if (kepemilikandata[i][1] == aidi):
                hilang = int(input("Jumlah tiket yang dihilangkan: "))
                newTiket = int(kepemilikandata[i][2]) - hilang
                kepemilikandata[i][2] = newTiket
    print()
    print("Laporan kehilangan tiket Anda telah direkam.")

def pencarian_wahana():
    global wahanadata
    #Print pilihan
    print("Jenis batasan umur:")
    print("1. Anak-anak (<17 tahun)")
    print("2. Dewasa (>=17 tahun)")
    print("3. Semua umur")
    print("")
    print("Jenis batasan tinggi badan: ")
    print("1. Lebih dari 170 cm")
    print("2. Tanpa batasan")
    print("")

    #Input pilihan
    umur=input("Batasan umur pemain: ")
    if (umur!='1') and (umur!='2') and (umur!='3'):
        while (umur!='1') and (umur!='2') and (umur!='3'):         #Validasi
            print("Batasan umur tidak valid!")
            umur=input("Batasan umur pemain: ")

    tinggi=input("Batasan tinggi badan: ")
    if(tinggi!='1' and tinggi!='2'):
        while (tinggi!='1' and tinggi!='2'):                      #Validasi
            print("Batasan tinggi badan tidak valid!")
            tinggi=input("Batasan tinggi badan: ")     

    print(" ")
    count=0
    N=panjang(wahanadata)

    if (umur=='1') and (tinggi=='1'):
        for i in range (N):
            if(wahanadata[i][3]=="anak-anak") and (wahanadata[i][4]==">=170cm"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j])

    if (umur=='1') and (tinggi=='2'):
        for i in range (N):
            if(wahanadata[i][3]=="anak-anak") and (wahanadata[i][4]=="tanpa batasan"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j],"|",end=" ")
                print()
            
    if (umur=='2') and (tinggi=='1'):
        for i in range (N):
            if(wahanadata[i][3]=="dewasa") and (wahanadata[i][4]==">=170cm"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j],"|",end=" ")
                print()
            
    if (umur=='2') and (tinggi=='2'):
        for i in range (N):
            if(wahanadata[i][3]=="dewasa") and (wahanadata[i][4]=="tanpa batasan"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j],"|",end=" ")
                print()
            
    if (umur=='3') and (tinggi=='1'):
        for i in range (N):
            if(wahanadata[i][3]=="semua umur") and (wahanadata[i][4]==">=170cm"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j],"|",end=" ")
                print()
            
    if (umur=='3') and (tinggi=='2'):
        for i in range (N):
            if(wahanadata[i][3]=="semua umur") and (wahanadata[i][4]=="tanpa batasan"):
                count+=1
                for j in range (5):
                    print(wahanadata[i][j],"|",end=" ")
                print()

    if count==0:
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

def syarat_umur(umur,batasan_umur):
    if (umur<17) and (batasan_umur=="anak-anak"):
        return True
    elif (umur>=17) and (batasan_umur=="dewasa"):
        return True
    elif (batasan_umur=="semua umur"):
        return True
    else:
        return False

def syarat_tinggi(tinggi,batasan_tinggi):
    if (tinggi>=170) and (batasan_tinggi==">=170cm"):
        return True
    elif (batasan_tinggi=="tanpa batasan"):
        return True
    else:
        return False

def hitung_umur(tgl,ttl):
    tahun_lahir=int(ttl[6]+ttl[7]+ttl[8]+ttl[9])
    tahun_ini=int(tgl[6]+tgl[7]+tgl[8]+tgl[9])
    bulan_lahir=int(ttl[3]+ttl[4])
    bulan_ini=int(tgl[3]+tgl[4])
    hari_lahir=int(ttl[0]+ttl[1])
    hari_ini=int(tgl[0]+tgl[1])

    umur= tahun_ini - tahun_lahir
    monthVeri = bulan_ini - bulan_lahir
    dateVeri = hari_ini - hari_lahir

    if monthVeri < 0 :
        umur = umur-1
    elif dateVeri < 0 and monthVeri == 0:
        umur = umur-1

    return umur

def beli_tiket(Username):
    global userdata, kepemilikandata, wahanadata, pembeliandata
    #Input ID
    id=input("Masukkan ID wahana: ")
    tgl=input("Masukkan tanggal hari ini (dd/mm/yyyy): ")
    jml=int(input("Jumlah tiket yang dibeli: "))
    print(" ")

    #Hitung saldo,umur, dan tinggi user
    for i in range (panjang(userdata)):
        if (Username==userdata[i][3]):
            a=i
            saldo=float(userdata[i][6])
            ttl=userdata[i][1]
            tinggi=float(userdata[i][2])
            gold = userdata[i][7]

    #Hitung umur
    umur= hitung_umur(tgl,ttl)

    #Cek ID Wahana dan batasan
    for i in range(panjang(wahanadata)):
        if (id==wahanadata[i][0]):
            namawahana=wahanadata[i][1]
            if gold == 'Y': #jika golden account maka harga tiket adalah setengah harga sebenarnya
                harga = 0.5 * float(wahanadata[i][2])
            else: #bukan golden account
                harga=float(wahanadata[i][2])
            batasan_umur=wahanadata[i][3]
            batasan_tinggi=wahanadata[i][4]

    #Mengecek apakah user memenuhi syarat
    if syarat_umur(umur,batasan_umur) and syarat_tinggi(tinggi,batasan_tinggi): #Memenuhi syarat
        if (saldo>(jml*harga)):   #Saldo memenuhi
            userdata[a][6]=saldo-(jml*harga)
            pembeliandata=pembeliandata + [[Username,tgl,id,jml]]
            kepemilikandata = kepemilikandata + [[Username,id,jml]]
            print("Selamat bersenang-senang di",namawahana)

        else:   #Saldo tidak memenuhi
            print("Saldo Anda tidak cukup.")
            print("Silakan mengisi saldo Anda.")

    else:   #Tidak memenuhi syarat
        print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
        print("Silakan menggunakan wahana lain yang tersedia.")

def main(Username):
    global kepemilikandata, penggunaandata
    #Input
    id=input("Masukkan ID wahana: ")
    tgl=input("Masukkan tanggal hari ini: ")
    jml=input("Jumlah tiket yang digunakan: ")
    print("")
    valid=False
    #Pengecekan Valid
    for i in range (panjang(kepemilikandata)):
        if (Username==kepemilikandata[i][0]):
            if (kepemilikandata[i][1]==id) and (int(kepemilikandata[i][2])!=0 and int(jml)<=int(kepemilikandata[i][2])):
                valid=True

    if valid==True :
        penggunaandata = penggunaandata + [[Username,tgl,id,jml]]
        kepemilikandata[i][2]=str(int(kepemilikandata[i][2])-int(jml))
        print("Terima kasih telah bermain.")
    else:
        print("Tiket Anda tidak valid dalam sistem kami.")

def best_wahana():
    global pembeliandata, wahanadata

    sumtiket=[[0 for j in range (3)] for i in range (panjang(wahanadata))]  #Inisialisasi Array Total Tiket
    for i in range (1,panjang(wahanadata),1):
        sumtiket[i-1][0]=wahanadata[i][0]
        sumtiket[i-1][1]=wahanadata[i][1]

    #Pemasukan jumlah tiket ke dalam array
    for i in range (panjang(sumtiket)): 
        count=0
        for j in range (1,panjang(pembeliandata),1):
            if (sumtiket[i][0]==pembeliandata[j][2]):
                count=count+int(pembeliandata[j][3])
        sumtiket[i][2]=str(count)
    
    #Mengurutkan wahana berdasarkan jumlah tiket
    urutantiket = [[0 for j in range (3)] for i in range (3)]
    maks1=0
    maks2=0
    maks3=0
    for i in range (panjang(sumtiket)):
        if (int(sumtiket[i][2])>=maks1):
            maks1=int(sumtiket[i][2])
            urutantiket[0]=sumtiket[i]

    for i in range (panjang(sumtiket)):
        if (int(sumtiket[i][2])==maks1 and sumtiket[i]==urutantiket[0]):
            sumtiket[i][2]=0

    for i in range (panjang(sumtiket)):
        if (int(sumtiket[i][2])>=maks2):
            maks2=int(sumtiket[i][2])
            urutantiket[1]=sumtiket[i]

    for i in range (panjang(sumtiket)):
        if (int(sumtiket[i][2])==maks2 and sumtiket[i]==urutantiket[1]):
            sumtiket[i][2]=0

    for i in range (panjang(sumtiket)):
        if (int(sumtiket[i][2])>=maks3):
            maks3=int(sumtiket[i][2])
            urutantiket[2]=sumtiket[i]

    urutantiket[0][2]=str(maks1)
    urutantiket[1][2]=str(maks2)
    urutantiket[2][2]=str(maks3)

    #Menampilkan best wahana yang sudah terurut
    for i in range(3):
        print(i+1,"|",end=' ')
        for j in range(3):
            if j<2:
                print(urutantiket[i][j],"|" ,end=' ')
            else:
                print(urutantiket[i][j],end='')
        print()


def refund(Username):
    global userdata, kepemilikandata, wahanadata, refunddata
    #Input
    id=input("Masukkan ID wahana: ")
    tgl=input("Masukan tanggal refund: ")
    jml=int(input("Jumlah tiket yang di-refund: "))
    print("")
    #Pengecekan user
    for i in range (panjang(userdata)):
        if (Username==userdata[i][3]):
            x=i
            saldo=float(userdata[i][6])
            gold = userdata[i][7]
    #Pengecekan Wahana
    for i in range(panjang(wahanadata)):
        if (id==wahanadata[i][0]):
            harga=float(wahanadata[i][2])
    #Pengecekan dan penambahan saldo
    found = False
    i = 0
    while i<panjang(kepemilikandata) and found == False:
        if (Username==kepemilikandata[i][0]) and kepemilikandata[i][1]==id and jml<=int(kepemilikandata[i][2])!=0:
            found= True
            refunddata = refunddata + [[Username,tgl,id,jml]]
            kepemilikandata[i][2]=str(int(kepemilikandata[i][2])-int(jml))
            if gold == 'Y':
                saldo = saldo + ((0.5*harga*jml)*0.8)
            else:
                saldo=saldo+((harga*jml)*0.8)
            userdata[x][6] = saldo
            print("Uang refund sudah kami berikan pada akun Anda.")
        i=i+1
    if found == False:
        print("Anda tidak memiliki tiket terkait.")


def kritik_saran():
    global kritiksarandata
    #Input
    id = input("Masukkan ID wahana: ")
    tgl = input("Masukkan tanggal pelaporan: ")
    krisar = input("Kritik/saran Anda: ")
    #Penambahan data
    newkrisar = [Username, tgl, id, krisar]
    kritiksarandata = nambahdata(kritiksarandata, newkrisar)
    print()
    print("Kritik dan saran Anda kami terima.")


def lihat_laporan():
    global kritiksarandata
    #Deklarasi array pembantu
    baru = []
    N = panjang(kritiksarandata)
    krisarbaru = [[0 for i in range(4)] for j in range(N)]
    #Pemisahan bagian yg akan di urutkan
    for i in range(N):
        baru = nambahdata(baru, kritiksarandata[i][2])
    #Pengurutan id wahana
    for i in range(panjang(baru) - 1, 0, -1):
        for j in range(i):
            if baru[j] > baru[j + 1]:
                temp = baru[j]
                baru[j] = baru[j + 1]
                baru[j + 1] = temp
    #Menaruh temporary hasil pengurutan id beserta variabel lain
    for i in range(N):
        for j in range(N):
            if kritiksarandata[j][2] == baru[i]:
                for k in range(4):
                    krisarbaru[i][k] = kritiksarandata[j][k]
    #Menaruh hasil akhir ke array utamanya
    for i in range(N):
        for j in range(4):
            kritiksarandata[i][j] = krisarbaru[i][j]

    print("Kritik dan saran: ")
    for row in kritiksarandata:
        print(str(row[2]) + ' | ' + str(row[1]) + ' | ' + str(row[0]) + ' | ' + str(row[3]))

def upgrade_gold():
    # Fungsi untuk melakukan upgrade akun menjadi golden account

    # KAMUS LOKAL
    # price,i,a,saldo : integer

    # Algoritma Lokal
    price = 100000
    Username = input("Masukkan username yang ingin di-upgrade: ")
    print()
    # Cek data pengguna
    for i in range(panjang(userdata)):
        if userdata[i][3] == Username:
            a = i
    # Mengupgrade account
    userdata[a][7] = 'Y'
    print("Akun Anda telah diupgrade.")
    return

# ALGORITMA UTAMA

# Load Data
print("Load Data ...")
load()
loggedin = False

# Loop Program, Loop akan berhenti jika pengguna memngetikkan 'Exit'
while True:
    print()
    print("""---------------------------------------------------------------------------------------------
-------------- Selamat Datang di Wahana Bermain Perusahaan Coklat Willy Wangky --------------
---------------------------------------------------------------------------------------------""")
    print("Silahkan login atau minta admin untuk mendaftarkan Anda!")
    login()
    # Cek apakah pengguna yang login adalah admin atau pemain, lalu mengeluarkan tampilan menu utama sesuai role account.
    if cekRole(Username) == 'Admin':
        while loggedin:
            print()
            print("""Daftar Menu : 
            1. Pendaftaran Pemain                   : signup
            2. Pencarian Pemain                     : cari_pemain
            3. Pencarian Wahana                     : cari_wahana
            4. Melihat Kritik dan Saran             : lihat_laporan
            5. Menambahkan Wahana Baru              : tambah_wahana
            6. Top Up Saldo                         : topup
            7. Melihat Riwayat Penggunaan Wahana    : riwayat_wahana
            8. Melihat Jumlah Tiket Pemain          : tiket_pemain
            9. Upgrade Golden Account               : upgrade_gold
            10.Penyimpanan Data                     : save
            11. Exit                                : exit""")
            # Menerima input menu pilihan admin, lalu melakukan proses sesuai menu yang dipilih
            menu = input("Ketikkan Menu Pilihan : ")
            print()
            if menu == 'signup':
                signup()
            elif menu == 'cari_pemain':
                cari_pemain()
            elif menu == 'cari_wahana':
                pencarian_wahana()
            elif menu == 'lihat_laporan':
                lihat_laporan()
            elif menu == 'tambah_wahana':
                tambah_wahana()
            elif menu == 'topup':
                topup()
            elif menu == 'riwayat_wahana':
                riwayat_wahana()
            elif menu == 'tiket_pemain':
                tiket_pemain()
            elif menu == 'upgrade_gold':
                upgrade_gold()
            elif menu == 'save':
                Save()
            elif menu == 'exit':
                Exit()
            else:
                print("Menu tidak tersedia. Mohon masukkan menu yang terdapat pada Daftar Menu!")
    else:  # Pengguna wahana merupakan pemain
        while loggedin:
            print()
            print("""Daftar Menu :
            1. Pencarian Wahana             : cari_wahana
            2. Pembelian Tiket              : beli_tiket
            3. Menggunakan Tiket            : main
            4. Refund                       : refund
            5. Kritik dan Saran             : kritik_saran
            6. Best Wahana                  : best_wahana
            7. Laporan Kehilangan Tiket     : tiket_hilang
            8. Penyimpanan Data             : save
            9. Exit                         : exit""")
            #Meminta input menu pilihan pemain, kemudian melakukan proses sesuai menu yang dipilih"
            menu = input("Ketikkan menu pilihan : ")
            print()
            if menu == 'cari_wahana':
                pencarian_wahana()
            elif menu == 'beli_tiket':
                beli_tiket(Username)
            elif menu == 'main':
                main(Username)
            elif menu == 'refund':
                refund(Username)
            elif menu == 'kritik_saran':
                kritik_saran()
            elif menu == 'upgrade_gold':
                upgrade_gold()
            elif menu == 'best_wahana':
                best_wahana()
            elif menu == 'tiket_hilang':
                tiket_hilang()
            elif menu == 'save':
                Save()
            elif menu == 'exit':
                Exit()
            else:
                print("Menu tidak tersedia. Mohon masukkan menu yang terdapat pada Daftar Menu!")
    # Pengguna telah melakukan exit, loggedin = False
    print("\nTerimakasih sudah berkunjung. Sampai bertemu lagi "+name+"!")
    # Diminta input untuk menentukan apakah ingin melanjutkan penggunaan atau menghentikan program wahana
    print("\nEnter to continue or 'Exit' to turn off the program ...")
    pilihan = input()
    if pilihan == 'Exit':
        exit()

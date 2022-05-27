##CAPSTONE PROJECT MINI APPS (CRUD) - Data Sepatu
'''
Yosafat Rogika (Ogik)
'''
dict_sepatu =  {"A01" : {"Brand" : "Adidas", "Kategori" : "Sport", "Warna" : "Hitam", "Size" : 40},
                "A02" : {"Brand" : "Adidas", "Kategori" : "Sneakers", "Warna" : "Biru", "Size" : 44},
             "T01" : {"Brand" : "Timberland", "Kategori" : "Safety Shoes", "Warna" : "Cokelat", "Size" : 44},
             "V01" : {"Brand" : "Vans", "Kategori" : "Sport", "Warna" : "Pink", "Size" : 38},
             "C01" : {"Brand" : "Crocodile", "Kategori" : "Pantofel", "Warna" : "Hitam", "Size" : 42}}
sepatu_baru = {}

### Koding Menu Utama
def menu_utama():
    print("")
    print("=======Data Stok Gudang Sepatu=======")
    print("1. Report Data Sepatu")
    print("2. Menambahkan Data Sepatu")
    print("3. Mengubah Data Sepatu")
    print("4. Menghapus Data Sepatu")
    print("5. Exit")
    main_menu = input("Silakan Pilih Main_Menu [1-5] : ")
    if main_menu == '1':
        menu_read()
    elif main_menu == '2':
        menu_create()
    elif main_menu == '3':
        menu_update()
    elif main_menu == '4':
        menu_delete()
    elif main_menu == '5':
        print("Thank you and Good Bye!!")
    else:
        print("")
        print("====Pilihan yang anda masukkan salah====")
        menu_utama()


### Menu Read Data
def menu_read():
    print("")
    print("======Report Data Sepatu======")
    print("1. Report Seluruh Data")
    print("2. Report Data Tertentu")
    print("3. Kembali Ke Menu Utama")
    read_menu = input("Silakan Pilih Sub Menu Read Data [1-3] : ")
    if read_menu == '1':
        read_all_data()
    elif read_menu == '2':
        read_spesific_data()
    elif read_menu == '3':
        menu_utama()
    else:
        menu_read()

### Read Seluruh Data
def read_all_data():
    if len(dict_sepatu) != 0:
        print("")
        for i in dict_sepatu:
            print("Kode Sepatu : {}, Brand : {}, Kategori : {}, Warna : {}, Size : {}".format(i,dict_sepatu[i]["Brand"], dict_sepatu[i]["Kategori"], dict_sepatu[i]["Warna"], dict_sepatu[i]["Size"]) )
        menu_read()
    else:
        print("")
        print("---Tidak Ada Data Sepatu---")
        menu_read()

### Read Data Tertentu
def read_spesific_data():
    code = input("Masukkan Kode Sepatu : ").capitalize()
    if code in dict_sepatu.keys():
        print("")
        print("Kode Sepatu : {}, Brand : {}, Kategori : {}, Warna : {}, Size : {}".format(code,dict_sepatu[code]["Brand"], dict_sepatu[code]["Kategori"], dict_sepatu[code]["Warna"], dict_sepatu[code]["Size"]))
        menu_read()
    else:
        print("")
        print("---Tidak Ada Data Sepatu---")
        menu_read()


### Menu Create Data
def menu_create():
    print("")
    print("======Menambah Data Sepatu======")
    print("1. Tambah Data Sepatu")
    print("2. Kembali Ke Menu Utama")
    create_menu = input("Silakan Pilih Sub Menu Create Data [1-2] : ")
    if create_menu == '1':
        create_data()
    elif create_menu == '2':
        menu_utama()
    else:
        menu_create()

### Create Data
def create_data():    
    global new_code
    new_code = input("Masukkan Kode Sepatu : ").capitalize()
    if new_code in dict_sepatu.keys():
        print("")
        print("---Data Sudah Ada---")
        menu_create()
    else:
        global brand
        brand = input("Masukkan Brand : ")
        sepatu_baru["Brand"] = brand 
        global kategori
        kategori = input("Masukkan Kategori : ")
        sepatu_baru["Kategori"] = kategori
        global warna
        warna = input("Masukkan Warna : ")
        sepatu_baru["Warna"] = warna
        global size
        size = input("Masukkan Size : ")
        sepatu_baru["Size"] = size
        simpan_data_baru()
    
### Simpan Create Data
def simpan_data_baru():
    simpan = input("Apakah Data akan disimpan? (Y/N) : ").capitalize()
    global sepatu_baru
    global dict_sepatu
    if simpan == 'Y':
        print("")
        print("Data Tersimpan")
        dict_sepatu[new_code] = sepatu_baru
        menu_create()        
    elif simpan == 'N':
        dict_sepatu = dict_sepatu
        print("")
        print("Data Tidak Tersimpan")
        menu_create()
    else:
        simpan_data_baru()
             

#### Menu Update Data
def menu_update():
    print("")
    print("======Mengubah Data Sepatu=====")
    print("1. Ubah Data Sepatu")
    print("2. Kembali Ke Menu Utama")
    update_menu = input("Silakan Pilih Menu Update Data [1-2] : ")
    if update_menu == '1':
        check_data()
    elif update_menu == '2':
        menu_utama()
    else:
        menu_update()

### check update data
def check_data():
    global update_code
    update_code = input("Masukkan Kode Sepatu : ").capitalize()
    if update_code in dict_sepatu:
        print("")
        print("Kode Sepatu : {}, Brand : {}, Kategori : {}, Warna : {}, Size : {}".format(update_code,dict_sepatu[update_code]["Brand"], dict_sepatu[update_code]["Kategori"], dict_sepatu[update_code]["Warna"], dict_sepatu[update_code]["Size"]))
        update_data()
    else:
        print("")
        print("Data Tidak Ada")
        menu_update()

### Check keterangan yg ingin di update        
def kolom_edit():
    update_key = input("Masukkan Kolom/Keterangan yg ingin di edit : ").capitalize()
    if update_key in dict_sepatu[update_code]:
        data_ubah = input("Masukkan {} Baru : ".format(update_key)).capitalize()
        m = 1
        while m != 0:
            simpan_update = input("Apakah Data akan diUpdate? (Y/N) : ").capitalize()
            if simpan_update == 'Y':
                dict_sepatu[update_code][update_key] = data_ubah
                print("")
                print("Data Updated")
                menu_update()
                m = 0
            elif simpan_update == 'N':
                print("")
                print("Data Tidak TerUpdate")
                menu_update()
                m = 0
            else:
                m = 1
    else:
        print("Mohon Masukkan Kolom/Keterangan yang benar")
        kolom_edit()

### check update data
def update_data():
    pil_upd = input("Tekan Y jika ingin lanjut Update Data atau N jika ingin cancel Update (Y/N) : ").capitalize()
    if pil_upd == 'Y':
        kolom_edit()
    elif pil_upd == 'N':
        print("")
        print("Data Tidak TerUpdate")
        menu_update()
    else:
        update_data()


### Menu Delete Data
def menu_delete():
    print("")
    print("============Menghapus Data Sepatu============")
    print("1. Hapus Data Sepatu")
    print("2. Kembali Ke Menu Utama")
    delete_menu = input("Silakan Pilih Sub Menu Hapus Data [1-2] : ")
    if delete_menu == '1':
        delete_data()
    elif delete_menu == '2':
        menu_utama()
    else:
        menu_delete()

### Hapus Data
def delete_data():
    global delete_code
    delete_code = input("Masukkan Kode Sepatu : ").capitalize()
    if delete_code in dict_sepatu.keys():
        delete_data_notif()
    else:
        print("")
        print("Data Tidak Ada")
        menu_delete()

### Simpan Hapus Data
def delete_data_notif():
    hapus_data = input("Apakah data akan dihapus? (Y/N) : ").capitalize()
    if hapus_data == 'Y':
        print("")
        print("Data Terhapus")
        dict_sepatu.pop(delete_code)
        menu_delete()
    elif hapus_data == 'N':
        print("")
        print("Data Tidak Terhapus")
        menu_delete()
    else:
        delete_data_notif()



menu_utama()
        
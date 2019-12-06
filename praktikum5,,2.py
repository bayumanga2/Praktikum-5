data={}
while True:
    print(" ")
    c = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar : ")
    if c.lower() == 'k':
        break
    
    elif c.lower() == 't':
        print("=======Tambah Data===")
        nama=input('Nama                  :')        
        nim=input('Nim                  : ')
        tugas=float(input('masukan nilai tugas : '))
        uts=float(input('masukan nilai uts : '))
        uas=float(input('masukan nilai uas : '))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim, tugas, uts, uas, akhir

    elif c.lower() == 'h':
        print('====hapus data mahasiswa====')
        nama=input('nama :  ' )
        if nama in data.keys():
            del data[nama]
    elif c.lower() == 'c':
        print("Cari Data")
        nama= input("Nama : ")
        if nama in data.keys():
            print("Datanya {0} adalah {1}"\
                  .format(nama, data[nama]))
            
    elif c.lower() == 'l':
        print("==================================================")
        print("|NO|  NAMA  | NIM         |TUGAS|UTS |UAS |AKHIR |")
        print("--------------------------------------------------") 
        i = 0
        for x in data.items():
            i+=1
        print("| {6:2} | {0:12s} | {1:9s} | {2:3} | {3:3} | {4:4} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        
        print("=============================================================================================================================")
     

    elif c.lower() =='u' :
        print("Ubah Data")
        nama = input("Nama: ")
        if nama in data.keys():
            nama=input('Nama                  :')        
            nim=input('Nim                  : ')
            tugas=float(input('masukan nilai tugas : '))
            uts=float(input('masukan nilai uts: '))
            uas=float(input('masukan nilai uas : '))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir

        else:
            print("=====================================Tidak Ada Data=================================")

            

    elif c.lower() == 'c':
        print('===cari data mahasiswa==')
        nama=input('masukan Nama : ')
        if nama in data.keys():
            print("Datanya", nama,"adalah {0}".format( data[nama]))

        else:
            print("===================================Tidak Ada Data==================================")

  

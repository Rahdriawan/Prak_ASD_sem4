def cetakSiku():
    baris = 5
    for i in range(baris + 1):
        for j in range(i):
            print("*", end="")  #end berfungsi untuk menambahkan string tambahan di akhir string
        print("*")

#run
cetakSiku()


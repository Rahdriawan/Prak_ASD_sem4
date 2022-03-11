import random   #modul untuk mengenerate angka sembarang

def tebakAngka():
    """Tebak Angka antara 1 - 100"""
    angkaRandom = random.randint(1, 100)   #fungsi randint untuk memberikan range di sembarang angka
    urutan = 0
    hitungan = 0

    #untuk test program
    #print(angkaRandom)

    while hitungan < 7:
        urutan += 1
        hitungan += 1
        inputUser = int(input("Masukkan tebakan ke-{}:> ".format(urutan)))
        if inputUser > angkaRandom:
            print("Itu terlalu besar, coba lagi.")
        elif inputUser == angkaRandom:
            print("Ya. Anda benar!")
            break
        else:
            print("Ite terlalu kecil, coba lagi.")
    else:
        print("Kesempatan anda telah habis!")

tebakAngka()
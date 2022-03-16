def fungsiCetak():
    """Mencetak angka 1-100 dengan kondisi kelipatan 3 = 'Python'
    kelipatan 5 = cetak 'UMS', 3 & 5 = "Python UMS'"""
    n = 0
    while n < 100:
        n += 1
        if n % 3 == 0:
            print("Python")
            continue
        elif n % 5 == 0:
            print("UMS")
            continue
        elif n % 3 == 0 and n % 5 == 0:
            print("Python UMS")
            continue
        print(n)

fungsiCetak()


def formatRupiah(nominal):
    a = str(nominal)
    if len(a) <= 3:
        return "Rp " + a
    else:
        p = a[-3:]
        q = a[:-3]
        return formatRupiah(q) + "." + p
        print("Rp" + formatRupiah(q) + "." + p)

print(formatRupiah(1500))
print(formatRupiah(24554300))

#No 3
def jumlahHurufVokal(text):
    vocalCount = 0
    for i in text:
        if i in ["a", "i", "u", "e", "o"]:
            vocalCount += 1
    print("(Jumlah karakter: {}, jumlah vokal: {})".format(len(text), vocalCount))

def jumlahKonsonan(text):
    konsonan = 0
    for i in text:
        if i not in ["a", "i", "u", "e", "o"]:
            konsonan += 1
    print("(Jumlah karakter: {}, jumlah konsonan: {})".format(len(text), konsonan))


jumlahHurufVokal("aakl")
jumlahKonsonan("cindi")
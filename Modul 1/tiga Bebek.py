def jumlahHurufVokal(text):
    """Menghitung jumlah huruf vokal dalam 1 kata"""
    vocalCount = 0
    for i in text:
        if i in ["a", "i", "u", "e", "o"]:
            vocalCount += 1
    print("Jumlah karakter: {}, jumlah vokal: {}".format(len(text), vocalCount))

def jumlahKonsonan(text):
    """Menghitung jumlah huruf konsonan dalam 1 kata"""
    konsonan = 0
    for i in text:
        if i not in ["a", "i", "u", "e", "o"]:
            konsonan += 1
    print("Jumlah karakter: {}, jumlah konsonan: {}".format(len(text), konsonan))


jumlahHurufVokal("aakl")
jumlahKonsonan("cindi")

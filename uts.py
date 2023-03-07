from math import pi

class Lingkaran:
    def __init__(self, diameter):
        self.diameter = diameter
        
    def Luas(self):
        print("Luas lingkaran:", pi * ((self.diameter/2) ** 2))
        
    def Keliling(self):
        print("Keliling lingkaran", 2 * pi * self.diameter)
        

class Tabung(Lingkaran):
    
    def __init__(self, tinggiTabung, diameter):
        self.tinggiTabung = tinggiTabung
        self.diameter = diameter

    def LuasPermukaan(self):
        print("Luas Permukaan:", (pi * ((self.diameter/2) ** 2)) + self.tinggiTabung)
        
    def Volume(self):
        print("Volume tabung:", pi * ((self.diameter/2) ** 2) * self.tinggiTabung)
        
        
aa = Lingkaran(34)
aa.Luas()
aa.Keliling()

print("-"*30)
bb = Tabung(23, 34)
bb.LuasPermukaan()
bb.Volume()

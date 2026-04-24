#6-masala
class Telefon:
    def yoq(self):
        print("Telefon yoqildi")

    def qongiroq(self):
        self.yoq()
        print("Qo'ng'iroq qilinyapti")

    def ochir(self):
        self.qongiroq()
        print("Telefon o'chirildi")

t = Telefon()
t.yoq()


#7-misol
class Kitob:
    def och(self):
        print("Kitob ochildi")

    def oqi(self):
        self.och()
        print("Kitob o'qilmoqda")

    def yoq(self):
        self.oqi()
        print("Kitob yopildi")

k = Kitob()
k.oqi()

#8-misol
class Ovqat:
    def tayyorla(self):
        print("Ovqat tayyorlandi")

    def ye(self):
        self.tayyorla()
        print("Ovqat yeyildi")

    def yuv(self):
        self.ye()
        print("Idishlar yuvildi")

o = Ovqat()
o.tayyorla()

#9-misol
class Dars:
    def boshlash(self):
        print("Dars boshlandi")

    def tushuntirish(self):
        self.tushuntirish()
        print("Mavzu tushuntirildi")

    def yakunlash(self):
        self.yakunlash()
        print("Dars tugadi")

d = Dars()
d.boshlash()


#10-misol
class Kompyuter:
    def yoq(self):
        print("Kompyuter yoqildi")

    def ishla(self):
        self.yoq()
        print("Kompyuter ishlamoqda")

    def ochir(self):
        self.ishla()
        print("Kompyuter o'chirildi")

k = Kompyuter()
k.ishla()

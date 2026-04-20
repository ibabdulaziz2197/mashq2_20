# 1
class Talaba:
    def __init__(self, i, y, k):
        self.ism = i
        self.yosh = y
        self.kurs = k

a = Talaba("Ali", 20, 2)
print(a.ism, a.yosh, a.kurs)

b = Talaba("Vali", 22, 3)
print(b.ism, b.yosh, b.kurs)

# 2
class Kitob:
    def __init__(self, n, m, s):
        self.nomi = n
        self.muallif = m
        self.sahifa_soni = s

a = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 300)
print(a.nomi, a.muallif, a.sahifa_soni)

b = Kitob("Alkimyogar", "Paulo Coelho", 200)
print(b.nomi, b.muallif, b.sahifa_soni)

# 3
class Telefon:
    def __init__(self, m, r, n):
        self.model = m
        self.rang = r
        self.narx = n

a = Telefon("iPhone 13", "qora", 1200)
print(a.model, a.rang, a.narx)

b = Telefon("Samsung S21", "oq", 900)
print(b.model, b.rang, b.narx)

# 4
class Mashina:
    def __init__(self, m, r, y):
        self.model = m
        self.rang = r
        self.yil = y

a = Mashina("Cobalt", "qizil", 2099)
print(a.model, a.rang, a.yil)

b = Mashina("Matiz", "oq", 1999)
print(b.model, b.rang, b.yil)

# 5
class Xodim:
    def __init__(self, i, l, m):
        self.ism = i
        self.lovozim = l
        self.maosh = m

a = Xodim("Ali", "Dasturchi", 1000)
print(a.ism, a.lovozim, a.maosh)

b = Xodim("Vali", "Manager", 1500)
print(b.ism, b.lovozim, b.maosh)

c = Xodim("Hasan", "Dizayner", 1200)
print(c.ism, c.lovozim ,c.maosh)

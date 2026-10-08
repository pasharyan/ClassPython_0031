class Rectangle:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def keliling(self):
        return 2 * (self.p + self.l)
    
    def luas(self):
        return self.p * self.l

    def __str__(self):
        return f"Rectangle, panjang {self.p} cm dan lebar {self.l} cm"

# Input panjang
p = float(input("Masukkan panjang: "))

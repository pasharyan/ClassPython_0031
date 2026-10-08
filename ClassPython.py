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

while p <= 0:
    print("Panjang tidak boleh 0 atau negatif!")
    p = float(input("Masukkan panjang: "))

# Input lebar
l = float(input("Masukkan lebar: "))

while l <= 0:
    print("Lebar tidak boleh 0 atau negatif!")
    l = float(input("Masukkan lebar: "))

# Membuat object
r = Rectangle(p, l)

# Memanggil semua fungsi
print("\nHasil:")
print(r)
print("Keliling:", r.keliling(), "cm")
print("Luas:", r.luas(), "cm²")


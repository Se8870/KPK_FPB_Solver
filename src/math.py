# untuk digunakan dalam penghitungan
# sekala besar.
from functools import reduce

def FPB(*args: int):
    """
    Mengambil data dari dalam args (jika terdedia)
    dan membaginya hingga paling terkecil

    Returns:
    hasil pembagian dari jumlah yang disimpan dalam args
    """
    def do_math(x, y):
        while (y):
            x, y = y, x % y
        return x

	return reduce(do_math, args)
	
def KPK(*args: int):
    """
    Mengambil data dari dalam args (jika terdedia)
    dan mengkalikan semua untuk mendapatkan hasil

    Returns:
    hasil perkalian dari jumlah yang disimpan dalam args
    """
    def do_math(x, y):
        return int(x*y//FPB(x,y))

    return reduce(do_math, args)

factor_a = int(input("Masukkan angka pertama: "))
factor_b = int(input("Masukkan angka kedua: "))

# Menggunakan try dan except untuk mencegah error keluar akibat data tidak terisi
# sebagai gantinya, digantikan oleh menggunakan 0 sebagai default.
try:
    factor_c = int(input("Masukkan angka ketiga (Jika tidak ada, hiraukan): ")) 
except:
    factor_c = 0

# Formating biar lebih rapih pada saat penampilan text
strOutput = f" dan {factor_b}" if factor_c == 0 else f", {factor_b}, dan {factor_c}"
print(f"Hasil dari {factor_a}{strOutput} adalah:\nFPB: {FPB(factor_a, factor_b, factor_c)}\nKPK: {KPK(factor_a, factor_b, factor_c)}")

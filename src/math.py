
def FPB(x, y, z = 0):
  """
  Mengambil data dari X, Y, dan Z (Jika Z tersedia)
  dan membaginya hingga paling terkecil
  
  Returns:
  hasil pembagian dari X, Y, dan Z (Jika Z tersedia)
  """
    while (y):
        x, y = y, x % y
    
    if z != 0:
        return FPB(z, x)

    return x

def KPK(x, y, z = 0):
  """
  Mengambil data dari X, Y, dan Z (Jika Z tersedia)
  dan mengkalikan semua untuk mendapatkan hasil
  
  Returns:
  hasil perkalian dari X, Y, dan Z (Jika Z tersedia)
  """
    ret = int(x*y/FPB(x, y))
    
    if z != 0:
        return KPK(ret, z)
        
    return ret

factor_a = int(input("Masukkan angka pertama: "))
factor_b = int(input("Masukkan angka kedua: "))

# Menggunakan try dan except untuk mencegah error keluar akibat data tidak terisi
# sebagai gantinya, digantikan oleh menggunakan 0 sebagai default.
try:
    factor_c = int(input("Masukkan angka ketiga (Jika tidak ada, hiraukan): ")) 
except:
    factor_c = 0

# Formating biar lebih rapih pada saat penampilan text
strOutput = f"dan {factor_b}" if factor_c == 0 else f",{factor_b} dan {factor_c}"
print(f"Hasil dari {factor_a} {strOutput} adalah:\nFPB: {FPB(factor_a, factor_b, factor_c)}\nKPK: {KPK(factor_a, factor_b, factor_c)}")

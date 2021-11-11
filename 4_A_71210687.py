print("=====MASUKKAN JUMLAH MAKANAN YANG DIPESAN=====")
daftarmenu_A = int(input("IKAN BAKAR      Rp 25.000,00   : "))
daftarmenu_B = int(input("ES DOGER        Rp 6.000,00    : "))
daftarmenu_C = int(input("RUJAK CINGUR    Rp 8.000,00    : "))
print("=====TOTAL=====")
hargatotalmenu_A = daftarmenu_A*25000
hargatotalmenu_B = daftarmenu_B*6000
hargatotalmenu_C = daftarmenu_C*8000
print("TOTAL IKAN BAKAR      : Rp ",hargatotalmenu_A)
print("TOTAL ES DOGER        : Rp ",hargatotalmenu_B)
print("TOTAL RUJAK CINGUR    : Rp ",hargatotalmenu_C)
print("Jumlah total biaya yang harus dibayar adalah RP",hargatotalmenu_A+hargatotalmenu_B+hargatotalmenu_C)
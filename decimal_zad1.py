# decimal - biblioteka do działania na prcyzyjnych liczbach zmienoprzecinkowych

from decimal import Decimal, getcontext

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')
print(kwota1 + kwota2)  # 15.75

precyzja = Decimal('0.00')

roznica = kwota1 - kwota2
print("Różnica", roznica)  # 4.75
print("Różnica", roznica.quantize(precyzja))  # Różnica 4.75

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem", kwota_z_podatkiem)  # Kwota z podatkiem 12.6075
print("Kwota z podatkiem", kwota_z_podatkiem.quantize(precyzja))  # Kwota z podatkiem 12.61

a = Decimal('1.2345')
b = Decimal('2.2345')

c = a + b
print("Wynik", a + b)  # 3.4690
precyzja2 = Decimal('0.001')
print("Wynik zaokrąglony", c.quantize(precyzja2))  # Wynik 3.469
print(c)  # 3.4690

getcontext().prec = 2
a = Decimal('1.23456789')
b = Decimal('2.23456789')
c = a + b
print(c)  # 3.5 - dwie cyfry dozwolone
d = Decimal('135')
print(d)
print(a / b)  # 0.55

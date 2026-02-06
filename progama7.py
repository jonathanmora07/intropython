#crear un programa que le pida un numero comprendido entre 1 y 100
import os 

os.system("cls")

print("---------------------conteo binario----------------------") 

v = False
while v = True: 
    num = 1 int(input("ingresa un numero entre 1 y 100: "))
 if  num < 1 or num > 100:
while numero < 1 or numero > 100: 
    print("numero fuera de rango.")
    numero = int(input("intnta de nuevo, ingresa un numero entre 1 y 100"))
else: 
    v = True
print("\numero valido", numero)

bin = "" 
i = num

while i > 0: 
    bin = str(i % 2) + bin 
    i -i // 2

print("el valor binario es: ",bin) 
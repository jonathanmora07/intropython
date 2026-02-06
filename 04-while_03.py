
import os
op=0

while op:=5:
    os.system("cls")
print("1.-suma\n2.-resta\n3.- multiplicacion\n4.- division\n5.- salir")
op=int(input("selecciona una opcion (1-5):"))
if op==1:
    num1=int(input("ingresa el primer numero"))
    um2=int(input("ingresa el segundo numero:"))
    print("la summa de {} + {} es: {}.format(num1,num2,num1+num2)")
    input("presiona Enter para continuar...")
if op==2:
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingrese el segudo numero: "))
    print("la resta de {} - {} es: {} .format (num1,num2,num1-num2)")
    input("presione enter para continuar...")
if op==3:
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingrese el segudo numero: "))
    print("la multiplicacion de {} - {} es: {} .format (num1,num2,num1=num2)")
    input("presione enter para continuar...")
if op==4:
    num1=int(input("ingresa el primer numero: "))
    num2=int(input("ingrese el segudo numero: "))
    print("la resta de {} - {} es: {} .format (num1,num2,num1-num2)")
    input("presione enter para continuar...")
    
        
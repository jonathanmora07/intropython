import math 

while True:
    
print("n\ Menu de opciones")
print("1. Tringulo")
print("2. Cuadro")
print("3. Circulo")
print("4. Pentagono")
print("5. Salir a menu")


opcion = input("Seleciona una opcion:")

if opcion =="1": 
    print("1 seleccionado: Tringualo ")
    base = float (input("ingresar la base: "))
    altura = float(input("ingrese la altura: "))
    area = (base * altura) / 2
    print("El area del triangulo es:")
    
elif opcion == "2":
    print("2 seleccionado: uCadrado")
    lado = float(input("ingrese el lado: "))
    area = lado * 2 
    print("El area del cuadrado es:")
    
elif opcion == "3":
    print("2 seleccionado: Circulo")
    radio = float (input("ingrese el radio:"))
    area = pi.*radio ** 2
    print("el area de circulo es:")
    
elif opcion == "4":
    print("4 seleccionado: Pentagono")
    Perimetro = float(input("ingrese el perimetro:"))
    apotema = float(input("ingresa el apotema:"))
    area = (perimetro * apotema) / 2 
    print("El area del pentagono es:") 
    
elif opcion == 5: 
    print("Saliendo a menu...")
    
else: 
    print("opcion no valida")
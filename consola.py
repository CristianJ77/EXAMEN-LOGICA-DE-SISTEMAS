from tkinter import*


#Curso: Logica de Sistemas
#Semestre: ciclo 1
#Nombre: Cristian Jose Figueroa Estrada
#carne: 0907-29-22929


print("Ingrese primer numero")
n1 = int(input())

print("Ingrese segundo numero")
n2 = int(input())

print("Ingrese tercer numero")
n3 = int(input())

if(n1>n3):
    print("La multiplacion de los 3 valores es")
    print(n1*n2*n3)

if(n1==n2==n3):
    print("La suma de los 3 valores es")
    print(n1+n2+n3)
    
if(n2==0):
   if(n1>n3):
    print("La resta de los valores es")
    print(n3-n1)
    
if(n3>n1):
    print("La resta de los valores es")
    print(n1-n3)
    







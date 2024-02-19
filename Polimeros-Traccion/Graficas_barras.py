#Graficos de barras
import matplotlib.pyplot as plt
import numpy as np

#Datos
polimeros = ["PS","PEAD","ABS","NYLON","PVC-P"]
Modulo_elastico = [2073, 652, 1796, 1217, 11]
Esfuerzo_fluencia = [0, 23, 49, 35, 5.9]
Esfuerzo_fractura = [39, 8.29, 40.2, 40, 14]
Ductilidad = [1.6, 80, 10, 7, 247]
Tenacidad = [0.37, 12, 4.2, 2, 22]

colores = ['blue', 'green', 'red', 'magenta', 'yellow'] 
alp = 0.6

#Grafico de barras
plt.figure(1)
plt.bar(polimeros, Esfuerzo_fluencia, color = colores, alpha = alp)
plt.title("Esfuerzo de fluencia de polimeros")
plt.xlabel("Polimeros")
plt.ylabel("σs Esfuerzo de fluencia (Mpa)")

plt.figure(2)
plt.bar(polimeros, Esfuerzo_fractura, color=colores, alpha = alp)
plt.title("Resistencia a la traccion de polimeros")
plt.xlabel("Polimeros")
plt.ylabel("σt Esfuerzo de traccion (Mpa)")

plt.figure(3)
plt.bar(polimeros, Modulo_elastico, color=colores, alpha = alp)
plt.title("Modulo elastico de polimeros")
plt.xlabel("Polimeros")
plt.ylabel("E Modulo elastico (Mpa)")

plt.figure(4)
plt.bar(polimeros, Ductilidad, color=colores, alpha = alp)
plt.title("Ductilidad de polimeros")
plt.xlabel("Polimeros")
plt.ylabel("ε Ductilidad %")

plt.figure(5)
plt.bar(polimeros, Tenacidad, color=colores, alpha = alp)
plt.title("Tenacidad de polimeros")
plt.xlabel("Polimeros")
plt.ylabel("Tenacidad (J/mm²)")

plt.show()

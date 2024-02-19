#Analisis esfuerzo - deformacion de una probeta de acero 1045
#Autor: Antony Rangel 16-10962

#Importamos las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

#Nota global: round(numero, decimales) para redondear los numeros a un numero de decimales especific
print('------------------------Analisis esfuerzo - deformacion de una probeta de PEAD ------------------------ \n')
#Ruta de carga de datos
archivo = 'PEAD-3.txt'

#Carga de datos 
datos = np.loadtxt(archivo, skiprows=1) #skiprows=1 para saltar las dos primeras filas

#Valores de fuerza y posicion
fuerza = datos[:,1] #Fuerza en N 
posicion = datos[:,0] #Posicion en mm
#print(fuerza[:10])

#Datos generales
espesor = 4.00 #Espesor de la probeta en mm
ancho = 8.04 #Diametro final de la probeta en mm
area =  espesor*ancho #Area de la probeta en mm^2
longitud_inicial = 107.2 #Longitud inicial de la probeta en mm
longitud_final = 150 #Longitud final de la probeta en mm

#Calculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo = fuerza/area

#Calculo de la deformacion ingenieril [mm/mm]
deformacion = posicion/longitud_inicial

#Zona elastica. Toma de datos de la zona elastica luego de visulaizar la grafica
esfuerzo_elastica = esfuerzo[0:20] 
deformacion_elastica = deformacion[0:20]

#Calculo del modulo de elasticidad o modulo de Young
pendiente = np.polyfit(deformacion_elastica, esfuerzo_elastica, 1)
mod_elasticidad = round(pendiente[0],3)
print(f'El modulo de elasticidad es: {mod_elasticidad} MPa')

#Metodo offset
# esfuerzo_offset = mod_elasticidad*deformacion[0:20]
# deformacion_offset = deformacion[0:20]+0.002
# pendiente_offset = np.polyfit(deformacion_offset,esfuerzo_offset, 1)

#Calculo del esfuerzo de fluencia maximo
# Sf_max = (np.abs(esfuerzo[:600] - 839.39)).argmin()
# esfuerzo_fluencia_max = round(esfuerzo[Sf_max],3)
# deformacion_fluencia_max = round(deformacion[Sf_max],3)
# # print(Sf_max)
# # print(deformacion_fluencia_max)
# print(f'El esfuerzo de fluencia maximo es: {esfuerzo_fluencia_max} MPa')

#Calculo del esfuerzo de fluencia minimo
# Sf_min = (np.abs(esfuerzo[:600] - 740.2)).argmin()
# esfuerzo_fluencia_min = round(esfuerzo[Sf_min],3)
# deformacion_fluencia_min = round(deformacion[Sf_min],3)
#print(f'El esfuerzo de fluencia minimo es: {esfuerzo_fluencia_min} MPa')

#Calculo del esfuerzo a la fluencia o esfuerzo maximo
esfuerzo_max = round(np.max(esfuerzo),3)
dx_max = deformacion[np.argmax(esfuerzo)]
print(f'El esfuerzo a la fluencia o maximo es: {esfuerzo_max} MPa')
print(f'Deformacion a la fluencia: {dx_max}')

#Calculo del esfuerzo a la fractura o esfuerzo ultimo
esfuerzo_ultimo = round(esfuerzo[-1],3)
dx_ultimo = deformacion[-1]
print(f'El esfuerzo a la fractura o ultimo es: {esfuerzo_ultimo} MPa')
print(f'Deformacion a la fractura: {dx_ultimo}')

#Calculo ductilidad - Grafica
ductilidad_grafica = round((deformacion[-1] - deformacion[0])*100 , 3)
print(f'Ductilidad medido por la grafica es: {ductilidad_grafica}%')
#Calculo de ductilidad - Probeta
ductilidad_probeta = round((longitud_final - longitud_inicial)/longitud_inicial*100 ,3)
print(f'Ductilidad medido de la probeta es: {ductilidad_probeta}%')

#Calculo de tenacidad
x_tenacidad = deformacion
y_tenacidad = esfuerzo
area_tenacidad = round(spi.trapezoid(y_tenacidad, x_tenacidad), 3)
print(f'El area de tenacidad graficamente es: {area_tenacidad} J/mm^2')

##############################################################################
#Zona de calculos con curvas de esfuerzo y deformacion reales

#Calculo de esfuerzo real [MPa = N/mm^2]
esfuerzo_real = esfuerzo*(1+deformacion)

#Calculo de la deformacion real [mm/mm]
deformacion_real = np.log(1+deformacion)


##############################################################################
#Graficas
#Grafica de esfuerzo vs deformacion ingenieril
plt.figure(1)
plt.plot(deformacion, esfuerzo)
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Esfuerzo vs Deformacion')

#Grafica de esfuerzo vs deformacion en la zona elastica
plt.figure(2)
plt.plot(deformacion_elastica, esfuerzo_elastica)
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Esfuerzo vs Deformacion (Zona elastica)')

#Grafica del modulo de elasticidad
plt.figure(3)
plt.plot(deformacion_elastica, pendiente[0]*deformacion_elastica + pendiente[1], label='Modulo de elasticidad' , color='red')
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Esfuerzo vs Deformacion (Zona elastica)')
plt.legend([ f"Modulo de Young: {mod_elasticidad} Mpa"], loc='upper left')

#Grafica del metodo offset
plt.figure(4)
plt.plot(deformacion, esfuerzo)
plt.plot(deformacion[:50], mod_elasticidad*deformacion[:50] + pendiente[1], label='Modulo de young' , color='orange', linestyle='--')
# plt.plot(deformacion_offset, mod_elasticidad*deformacion_offset + pendiente_offset[1], label='Offset' , color='black', linestyle='--')
# plt.plot(deformacion_fluencia_max, esfuerzo_fluencia_max, 'ro')
#plt.plot(deformacion_fluencia_min, esfuerzo_fluencia_min, 'ro')
plt.plot(dx_max, esfuerzo_max, 'ro')
plt.plot(dx_ultimo, esfuerzo_ultimo, 'rx')
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Esfuerzo vs Deformacion')
plt.legend(["Esfuerzo vs Deformacion",f"Modulo de Young: {mod_elasticidad} Mpa", f"Sy_fluencia: {esfuerzo_max} Mpa", f"Sb_fractura: {esfuerzo_ultimo} Mpa"], loc='upper right')

#Gráfica de resiliencia y tenacidad
plt.figure(5)
#plt.plot(deformacion, esfuerzo)
# plt.plot(x_resiliencia, y_resiliencia, label='Resiliencia', color='red')
plt.plot(x_tenacidad, y_tenacidad, label='Tenacidad', color='green')
# plt.fill_between(x_resiliencia, y_resiliencia, color='red', alpha=0.4, label='Área de resiliencia')
plt.fill_between(x_tenacidad, y_tenacidad, color='green', alpha=0.4, label='Área de tenacidad')
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Esfuerzo vs Deformacion')
plt.legend([ f"Tenacidad: {area_tenacidad} J/mm^2"], loc='upper right')


#Grficas de curvas reales
#Grafica de esfuerzo vs deformacion real
plt.figure(6)
plt.plot(deformacion_real, esfuerzo_real, color='orange')
plt.xlabel('Deformacion real [mm/mm]')
plt.ylabel('Esfuerzo real [MPa]')
plt.title('Esfuerzo real vs Deformacion real')

plt.figure(7)
plt.plot(deformacion, esfuerzo, color='blue')
plt.plot(deformacion_real, esfuerzo_real, color='orange')
plt.xlabel('Deformacion [mm/mm]')
plt.ylabel('Esfuerzo [MPa]')
plt.title('Curva ingenieril vs real')
plt.legend(["Curva ingenieril", "Curva real"], loc='upper right')

plt.show()
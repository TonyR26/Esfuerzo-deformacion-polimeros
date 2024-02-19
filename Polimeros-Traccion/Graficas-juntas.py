#Graficas esfuerzo - deformacion (Materiales Polimeros)
#Autor: Antony Rangel 16-10962

import numpy as np
import matplotlib.pyplot as plt


#Carga de datos

#PEAD
PEAD_3 = np.loadtxt('PEAD-P3.txt',skiprows=1)
PEAD_4 = np.loadtxt('PEAD-P4.txt',skiprows=1)

# Valores de fuerza y posición
fuerza_PEAD3 = PEAD_3[:, 1]  # Fuerza en N
posicion_PEAD3 = PEAD_3[:, 0]  # Posición en mm

fuerza_PEAD4 = PEAD_4[:, 1]  # Fuerza en N
posicion_PEAD4 = PEAD_4[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_PEAD3 = 107.20  # Longitud inicial de la probeta en mm
longitud_inicial_PEAD4 = 107.20  # Longitud inicial de la probeta en mm
ancho_PEAD3 = 8.04  # Ancho de la probeta en mm
ancho_PEAD4 = 18.05  # Ancho de la probeta en mm
espesor_PEAD3 = 4.00  # Espesor de la probeta en mm
espesor_PEAD4 = 3.98  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_PEAD3 = espesor_PEAD3 * ancho_PEAD3
area_PEAD4 = espesor_PEAD4 * ancho_PEAD4

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_PEAD3 = fuerza_PEAD3 / area_PEAD3
esfuerzo_PEAD4 = fuerza_PEAD4 / area_PEAD4

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_PEAD3 = posicion_PEAD3 / longitud_inicial_PEAD3
deformacion_PEAD4 = posicion_PEAD4 / longitud_inicial_PEAD4

#PS
PS_1 = np.loadtxt('PS-P1.txt', skiprows=1)
PS_2 = np.loadtxt('PS-P2.txt', skiprows=1)
PS_3 = np.loadtxt('PS-P3.txt', skiprows=1)
PS_4 = np.loadtxt('PS-P4.txt', skiprows=1)

# Valores de fuerza y posición
fuerza_PS1 = PS_1[:, 1]  # Fuerza en N
posicion_PS1 = PS_1[:, 0]  # Posición en mm

fuerza_PS2 = PS_2[:, 1]  # Fuerza en N
posicion_PS2 = PS_2[:, 0]  # Posición en mm

fuerza_PS3 = PS_3[:, 1]  # Fuerza en N
posicion_PS3 = PS_3[:, 0]  # Posición en mm

fuerza_PS4 = PS_4[:, 1]  # Fuerza en N
posicion_PS4 = PS_4[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_PS1 = 107.20  # Longitud inicial de la probeta en mm
longitud_inicial_PS2 = 107.20  # Longitud inicial de la probeta en mm
longitud_inicial_PS3 = 107.20  # Longitud inicial de la probeta en mm
longitud_inicial_PS4 = 107.20  # Longitud inicial de la probeta en mm

ancho_PS1 = 8.5  # Ancho de la probeta en mm
ancho_PS2 = 8.1  # Ancho de la probeta en mm
ancho_PS3 = 8.0  # Ancho de la probeta en mm
ancho_PS4 = 8.42  # Ancho de la probeta en mm

espesor_PS1 = 3.9  # Espesor de la probeta en mm
espesor_PS2 = 3.72  # Espesor de la probeta en mm
espesor_PS3 = 3.82  # Espesor de la probeta en mm
espesor_PS4 = 4.21  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_PS1 = espesor_PS1 * ancho_PS1
area_PS2 = espesor_PS2 * ancho_PS2
area_PS3 = espesor_PS3 * ancho_PS3
area_PS4 = espesor_PS4 * ancho_PS4

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_PS1 = fuerza_PS1 / area_PS1
esfuerzo_PS2 = fuerza_PS2 / area_PS2
esfuerzo_PS3 = fuerza_PS3 / area_PS3
esfuerzo_PS4 = fuerza_PS4 / area_PS4

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_PS1 = posicion_PS1 / longitud_inicial_PS1
deformacion_PS2 = posicion_PS2 / longitud_inicial_PS2
deformacion_PS3 = posicion_PS3 / longitud_inicial_PS3
deformacion_PS4 = posicion_PS4 / longitud_inicial_PS4

#ABS
ABS_1 = np.loadtxt('ABS-P1.txt', skiprows=1)
ABS_2 = np.loadtxt('ABS-P2.txt', skiprows=1)
ABS_3 = np.loadtxt('ABS-P3.txt', skiprows=1)

# Valores de fuerza y posición
fuerza_ABS1 = ABS_1[:, 1]  # Fuerza en N
posicion_ABS1 = ABS_1[:, 0]  # Posición en mm

fuerza_ABS2 = ABS_2[:, 1]  # Fuerza en N
posicion_ABS2 = ABS_2[:, 0]  # Posición en mm

fuerza_ABS3 = ABS_3[:, 1]  # Fuerza en N
posicion_ABS3 = ABS_3[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_ABS1 = 122.40  # Longitud inicial de la probeta en mm
longitud_inicial_ABS2 = 122.40  # Longitud inicial de la probeta en mm
longitud_inicial_ABS3 = 122.40  # Longitud inicial de la probeta en mm

ancho_ABS1 = 12.60  # Ancho de la probeta en mm
ancho_ABS2 = 12.56  # Ancho de la probeta en mm
ancho_ABS3 = 12.47  # Ancho de la probeta en mm

espesor_ABS1 = 3.25  # Espesor de la probeta en mm
espesor_ABS2 = 3.22  # Espesor de la probeta en mm
espesor_ABS3 = 3.23  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_ABS1 = espesor_ABS1 * ancho_ABS1
area_ABS2 = espesor_ABS2 * ancho_ABS2
area_ABS3 = espesor_ABS3 * ancho_ABS3

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_ABS1 = fuerza_ABS1 / area_ABS1
esfuerzo_ABS2 = fuerza_ABS2 / area_ABS2
esfuerzo_ABS3 = fuerza_ABS3 / area_ABS3

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_ABS1 = posicion_ABS1 / longitud_inicial_ABS1
deformacion_ABS2 = posicion_ABS2 / longitud_inicial_ABS2
deformacion_ABS3 = posicion_ABS3 / longitud_inicial_ABS3

#ELASTOMEROS
ELASTOMERO_1 = np.loadtxt('ELASTOMERO-P1.txt', skiprows=1)
ELASTOMERO_2 = np.loadtxt('ELASTOMERO-P2.txt', skiprows=1)
ELASTOMERO_3 = np.loadtxt('ELASTOMERO-P3.txt', skiprows=1)

# Valores de fuerza y posición
fuerza_ELASTOMERO1 = ELASTOMERO_1[:, 1]  # Fuerza en N
posicion_ELASTOMERO1 = ELASTOMERO_1[:, 0]  # Posición en mm

fuerza_ELASTOMERO2 = ELASTOMERO_2[:, 1]  # Fuerza en N
posicion_ELASTOMERO2 = ELASTOMERO_2[:, 0]  # Posición en mm

fuerza_ELASTOMERO3 = ELASTOMERO_3[:, 1]  # Fuerza en N
posicion_ELASTOMERO3 = ELASTOMERO_3[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_ELASTOMERO1 = 67.7  # Longitud inicial de la probeta en mm
longitud_inicial_ELASTOMERO2 = 67.7  # Longitud inicial de la probeta en mm
longitud_inicial_ELASTOMERO3 = 67.7  # Longitud inicial de la probeta en mm

ancho_ELASTOMERO1 = 5.57  # Ancho de la probeta en mm
ancho_ELASTOMERO2 = 5.69  # Ancho de la probeta en mm
ancho_ELASTOMERO3 = 5.72  # Ancho de la probeta en mm

espesor_ELASTOMERO1 = 1.91  # Espesor de la probeta en mm
espesor_ELASTOMERO2 = 1.83  # Espesor de la probeta en mm
espesor_ELASTOMERO3 = 1.92  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_ELASTOMERO1 = espesor_ELASTOMERO1 * ancho_ELASTOMERO1
area_ELASTOMERO2 = espesor_ELASTOMERO2 * ancho_ELASTOMERO2
area_ELASTOMERO3 = espesor_ELASTOMERO3 * ancho_ELASTOMERO3

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_ELASTOMERO1 = fuerza_ELASTOMERO1 / area_ELASTOMERO1
esfuerzo_ELASTOMERO2 = fuerza_ELASTOMERO2 / area_ELASTOMERO2
esfuerzo_ELASTOMERO3 = fuerza_ELASTOMERO3 / area_ELASTOMERO3

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_ELASTOMERO1 = posicion_ELASTOMERO1 / longitud_inicial_ELASTOMERO1
deformacion_ELASTOMERO2 = posicion_ELASTOMERO2 / longitud_inicial_ELASTOMERO2
deformacion_ELASTOMERO3 = posicion_ELASTOMERO3 / longitud_inicial_ELASTOMERO3


#NYLON
NYLON_1 = np.loadtxt('NYLON6-P1.txt', skiprows=1)
NYLON_2 = np.loadtxt('NYLON6-P2.txt', skiprows=1)
NYLON_3 = np.loadtxt('NYLON6-P3.txt', skiprows=1)
NYLON_4 = np.loadtxt('NYLON6-P4.txt', skiprows=1)

# Valores de fuerza y posición
fuerza_NYLON1 = NYLON_1[:, 1]  # Fuerza en N
posicion_NYLON1 = NYLON_1[:, 0]  # Posición en mm

fuerza_NYLON2 = NYLON_2[:, 1]  # Fuerza en N
posicion_NYLON2 = NYLON_2[:, 0]  # Posición en mm

fuerza_NYLON3 = NYLON_3[:, 1]  # Fuerza en N
posicion_NYLON3 = NYLON_3[:, 0]  # Posición en mm

fuerza_NYLON4 = NYLON_4[:, 1]  # Fuerza en N
posicion_NYLON4 = NYLON_4[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_NYLON1 = 117.20  # Longitud inicial de la probeta en mm
longitud_inicial_NYLON2 = 117.20  # Longitud inicial de la probeta en mm
longitud_inicial_NYLON3 = 117.20  # Longitud inicial de la probeta en mm
longitud_inicial_NYLON4 = 117.20  # Longitud inicial de la probeta en mm

ancho_NYLON1 = 8.25  # Ancho de la probeta en mm
ancho_NYLON2 = 8.15  # Ancho de la probeta en mm
ancho_NYLON3 = 8.16  # Ancho de la probeta en mm
ancho_NYLON4 = 8.15  # Ancho de la probeta en mm

espesor_NYLON1 = 4.10  # Espesor de la probeta en mm
espesor_NYLON2 = 4.14  # Espesor de la probeta en mm
espesor_NYLON3 = 4.11  # Espesor de la probeta en mm
espesor_NYLON4 = 4.10  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_NYLON1 = espesor_NYLON1 * ancho_NYLON1
area_NYLON2 = espesor_NYLON2 * ancho_NYLON2
area_NYLON3 = espesor_NYLON3 * ancho_NYLON3
area_NYLON4 = espesor_NYLON4 * ancho_NYLON4

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_NYLON1 = fuerza_NYLON1 / area_NYLON1
esfuerzo_NYLON2 = fuerza_NYLON2 / area_NYLON2
esfuerzo_NYLON3 = fuerza_NYLON3 / area_NYLON3
esfuerzo_NYLON4 = fuerza_NYLON4 / area_NYLON4

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_NYLON1 = posicion_NYLON1 / longitud_inicial_NYLON1
deformacion_NYLON2 = posicion_NYLON2 / longitud_inicial_NYLON2
deformacion_NYLON3 = posicion_NYLON3 / longitud_inicial_NYLON3
deformacion_NYLON4 = posicion_NYLON4 / longitud_inicial_NYLON4

#PVC+P
PVC_P_1 = np.loadtxt('PVC+P-P1.txt', skiprows=1)
PVC_P_2 = np.loadtxt('PVC+P-P2.txt', skiprows=1)
PVC_P_3 = np.loadtxt('PVC+P-P3.txt', skiprows=1)

# Valores de fuerza y posición
fuerza_PVC_P1 = PVC_P_1[:, 1]  # Fuerza en N
posicion_PVC_P1 = PVC_P_1[:, 0]  # Posición en mm

fuerza_PVC_P2 = PVC_P_2[:, 1]  # Fuerza en N
posicion_PVC_P2 = PVC_P_2[:, 0]  # Posición en mm

fuerza_PVC_P3 = PVC_P_3[:, 1]  # Fuerza en N
posicion_PVC_P3 = PVC_P_3[:, 0]  # Posición en mm

# Valores de las dimensiones de la probeta
longitud_inicial_PVC_P1 = 58.40  # Longitud inicial de la probeta en mm
longitud_inicial_PVC_P2 = 58.40  # Longitud inicial de la probeta en mm
longitud_inicial_PVC_P3 = 58.40  # Longitud inicial de la probeta en mm

ancho_PVC_P1 = 5.69  # Ancho de la probeta en mm
ancho_PVC_P2 = 5.61  # Ancho de la probeta en mm
ancho_PVC_P3 = 5.59  # Ancho de la probeta en mm

espesor_PVC_P1 = 3.15  # Espesor de la probeta en mm
espesor_PVC_P2 = 2.87  # Espesor de la probeta en mm
espesor_PVC_P3 = 2.33  # Espesor de la probeta en mm

# Área de la probeta en mm^2
area_PVC_P1 = espesor_PVC_P1 * ancho_PVC_P1
area_PVC_P2 = espesor_PVC_P2 * ancho_PVC_P2
area_PVC_P3 = espesor_PVC_P3 * ancho_PVC_P3

# Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
esfuerzo_PVC_P1 = fuerza_PVC_P1 / area_PVC_P1
esfuerzo_PVC_P2 = fuerza_PVC_P2 / area_PVC_P2
esfuerzo_PVC_P3 = fuerza_PVC_P3 / area_PVC_P3

# Cálculo de la deformación ingenieril [mm/mm]
deformacion_PVC_P1 = posicion_PVC_P1 / longitud_inicial_PVC_P1
deformacion_PVC_P2 = posicion_PVC_P2 / longitud_inicial_PVC_P2
deformacion_PVC_P3 = posicion_PVC_P3 / longitud_inicial_PVC_P3


#Graficas
plt.figure(1)
plt.plot(deformacion_PEAD3, esfuerzo_PEAD3, label='PEAD-P3', color='blue')
plt.plot(deformacion_PEAD4, esfuerzo_PEAD4, label='PEAD-P4', color='red')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación PEAD')
plt.legend()

plt.figure(2)
plt.plot(deformacion_PS1, esfuerzo_PS1, label='PS-P1', color='blue')
plt.plot(deformacion_PS2, esfuerzo_PS2, label='PS-P2', color='red')
plt.plot(deformacion_PS3, esfuerzo_PS3, label='PS-P3', color='green')
plt.plot(deformacion_PS4, esfuerzo_PS4, label='PS-P4', color='orange')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación PS')
plt.legend()

plt.figure(3)
plt.plot(deformacion_ABS1, esfuerzo_ABS1, label='ABS-P1', color='blue')
plt.plot(deformacion_ABS2, esfuerzo_ABS2, label='ABS-P2', color='red')
plt.plot(deformacion_ABS3, esfuerzo_ABS3, label='ABS-P3', color='green')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación ABS')
plt.legend()

plt.figure(4)
plt.plot(deformacion_ELASTOMERO1, esfuerzo_ELASTOMERO1, label='ELASTOMERO-P1', color='blue')
plt.plot(deformacion_ELASTOMERO2, esfuerzo_ELASTOMERO2, label='ELASTOMERO-P2', color='red')
plt.plot(deformacion_ELASTOMERO3, esfuerzo_ELASTOMERO3, label='ELASTOMERO-P3', color='green')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación ELASTOMERO')
plt.legend()

plt.figure(5)
plt.plot(deformacion_NYLON1, esfuerzo_NYLON1, label='NYLON6-P1', color='blue')
plt.plot(deformacion_NYLON2, esfuerzo_NYLON2, label='NYLON6-P2', color='red')
plt.plot(deformacion_NYLON3, esfuerzo_NYLON3, label='NYLON6-P3', color='green')
plt.plot(deformacion_NYLON4, esfuerzo_NYLON4, label='NYLON6-P4', color='orange')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación NYLON6')
plt.legend()

plt.figure(6)
plt.plot(deformacion_PVC_P1, esfuerzo_PVC_P1, label='PVC+P-P1', color='blue')
plt.plot(deformacion_PVC_P2, esfuerzo_PVC_P2, label='PVC+P-P2', color='red')
plt.plot(deformacion_PVC_P3, esfuerzo_PVC_P3, label='PVC+P-P3', color='green')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación PVC+P')
plt.legend()

plt.figure(7)
plt.plot(deformacion_PEAD3, esfuerzo_PEAD3, label='PEAD-P3', color='blue')
plt.plot(deformacion_PS2, esfuerzo_PS2, label='PS-P2', color='red')
plt.plot(deformacion_ABS2, esfuerzo_ABS2, label='ABS-P2', color='green')
plt.plot(deformacion_ELASTOMERO2, esfuerzo_ELASTOMERO2, label='ELASTOMERO-P2', color='orange')
plt.plot(deformacion_NYLON2, esfuerzo_NYLON2, label='NYLON6-P2', color='purple')
plt.plot(deformacion_PVC_P2, esfuerzo_PVC_P2, label='PVC+P-P2', color='brown')
plt.xlabel('Deformación (mm/mm)')
plt.ylabel('Esfuerzo (MPa)')
plt.title('Esfuerzo - Deformación Materiales Polimeros')


fila = 3
columnas = 2
fig, axs = plt.subplots(fila, columnas, figsize=(10, 20))
fig.suptitle('Esfuerzo - Deformación Materiales Polimeros')

axs[0, 0].plot(deformacion_PEAD3, esfuerzo_PEAD3, label='PEAD-P3', color='blue')
axs[0, 0].set_title('PEAD-P3')

axs[0, 1].plot(deformacion_PS2, esfuerzo_PS2, label='PS-P2', color='red')
axs[0, 1].set_title('PS-P2')

axs[1, 0].plot(deformacion_ABS2, esfuerzo_ABS2, label='ABS-P2', color='green')
axs[1, 0].set_title('ABS-P2')

axs[1, 1].plot(deformacion_ELASTOMERO2, esfuerzo_ELASTOMERO2, label='ELASTOMERO-P2', color='orange')
axs[1, 1].set_title('ELASTOMERO-P2')

axs[2, 0].plot(deformacion_NYLON2, esfuerzo_NYLON2, label='NYLON6-P2', color='purple')
axs[2, 0].set_title('NYLON6-P2')

axs[2, 1].plot(deformacion_PVC_P2, esfuerzo_PVC_P2, label='PVC+P-P2', color='brown')
axs[2, 1].set_title('PVC+P-P2')

plt.tight_layout()
plt.show()


plt.show()




#Analisis esfuerzo - deformacion (Materiales Polimeros)
#Autor: Antony Rangel 16-10962


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def analisis_probeta(archivo, d, b, L, elastomero):
    # Carga de datos
    datos = np.loadtxt(archivo, skiprows=1)
    nombre_probeta = archivo.rstrip('.txt')

    # Valores de fuerza (P) y posición o maxima deflaxion(D)
    P = datos[:, 1]  # Fuerza en N
    D = datos[:, 0]  # Posición en mm


    # Cálculo del esfuerzo ingenieril [MPa = N/mm^2]
    esfuerzo_y = (3*P*L)/(2*b*d**2)

    # Cálculo de la deformación ingenieril [mm/mm]
    deformacion_x = (6*D*d)/(L**2)

    if nombre_probeta.startswith('NYLON') or nombre_probeta.startswith('PS'):
        xx = len(deformacion_x) #Se toma todos los valores de la deformacion
    elif nombre_probeta.startswith('PEAD'):
        xx = len(deformacion_x) #Se toma 1/6 de los valor de la deformacion
    else:
        xx = len(deformacion_x) #Se toma 1/2 de los valor de la deformacion

    # Cálculo del de propiedades mecanicas
    if elastomero.lower() == 'no':
        
        # Visualización de la gráfica para seleccionar rango de datos limpios
        plt.plot(deformacion_x, esfuerzo_y)
        plt.xlabel('Deflexion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Deflexion')
        plt.show()

        #Limpieza de datos
        limpiar_datos = input("Desea limpiar los datos de la gráfica? (Si o No): ")
        if limpiar_datos.lower() == 'si':
            rango = input("Desea seleccionar un rango de datos para el analisis? (Si o No): ")
            if rango.lower() == "si":
                #Zona para limpiar datos de la gráfica
                #Ingrese el rango de datos limpo que se desea tomar
                inicio_deformacion = float(input("Ingrese el valor inicial de la deflexion: "))
                fin_deformacion = float(input("Ingrese el valor final de la deflexion: "))
                inicio_esfuero = float(input("Ingrese el valor inicial del esfuerzo: "))
                fin_esfuerzo = float(input("Ingrese el valor final del esfuerzo: "))

                #Limpieza de datos
                mask_deformacion = (deformacion_x >= inicio_deformacion) & (deformacion_x <= fin_deformacion)
                mask_esfuerzo = (esfuerzo_y >= inicio_esfuero) & (esfuerzo_y <= fin_esfuerzo)
                # Crea una máscara única que combine mask_deformacion y mask_esfuerzo
                mask_unica = mask_deformacion & mask_esfuerzo

                # Aplica la máscara única a deformacion y esfuerzo
                deformacion = deformacion_x[mask_unica]
                esfuerzo = esfuerzo_y[mask_unica]
                
            else:
                deformacion = deformacion_x
                esfuerzo = esfuerzo_y
            


            # Calcular la media y la desviación estándar
            media_deformacion = np.mean(deformacion)
            std_deformacion = np.std(deformacion)

            # Definir un umbral para los valores atípicos
            umbral = 7

            # Crear una máscara booleana para los valores atípicos
            mask_atipicos_deformacion = np.abs(deformacion - media_deformacion) < umbral * std_deformacion

            # Aplicar la máscara para eliminar los valores atípicos
            deformacion_x_recortado = deformacion[mask_atipicos_deformacion]

            # Repetir el proceso para esfuerzo_y
            media_esfuerzo = np.mean(esfuerzo)
            std_esfuerzo = np.std(esfuerzo)
            mask_atipicos_esfuerzo = np.abs(esfuerzo - media_esfuerzo) < umbral * std_esfuerzo
            esfuerzo_y_recortado = esfuerzo[mask_atipicos_esfuerzo]

            # Aplicar un filtro de media móvil
            ventana = 5  # Tamaño de la ventana para el filtro de media móvil
            kernel = np.ones(ventana) / ventana
            deformacion_x_suavizada = np.convolve(deformacion_x_recortado, kernel, mode='valid')
            esfuerzo_y_suavizado = np.convolve(esfuerzo_y_recortado, kernel, mode='valid')

            # Recortar 'deformacion_x_suavizada' para que tenga la misma longitud que 'esfuerzo_y_suavizado'
            deformacion_x_suavizada = deformacion_x_suavizada[(ventana-1)//2:-(ventana//2)]

            # Datos limpios
            deformacion = deformacion_x_suavizada
            esfuerzo = esfuerzo_y_suavizado

            
        else:
            deformacion = deformacion_x
            esfuerzo = esfuerzo_y


        # Asegurarse de que ambas listas tengan la misma longitud
        if len(deformacion) > len(esfuerzo):
            deformacion = deformacion[:len(esfuerzo)]
        elif len(esfuerzo) > len(deformacion):
            esfuerzo = esfuerzo[:len(deformacion)]
        
        deformacion -= deformacion[0]
        # esfuerzo = esfuerzo.values
        # deformacion = deformacion.values


        # Visualización de la gráfica para seleccionar rango de la zona elástica y cálculo del módulo de elasticidad
        plt.figure(1)
        plt.plot(deformacion, esfuerzo)
        plt.xlabel('Deflexion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Deflexion')
        plt.show()

        # Ingreso del rango para la zona elástica
        inicio_elastica = float(input("Ingrese el valor inicial del rango elástico (Deflexion): "))
        fin_elastica = float(input("Ingrese el valor final del rango elástico (Deflexion): "))

        # Zona elástica. Tomar datos de la zona elástica según el rango ingresado
        mask_elastica = (deformacion >= inicio_elastica) & (deformacion <= fin_elastica)
        esfuerzo_elastica = esfuerzo[mask_elastica]
        deformacion_elastica = deformacion[mask_elastica]

        # Cálculo del módulo de elasticidad o módulo de Young
        pendiente = np.polyfit(deformacion_elastica, esfuerzo_elastica, 1)
        m_pendiente = round(pendiente[0], 3)
        print(f'Pendiente (m) de la zona lineal: {m_pendiente} MPa')
        mod_elasticidad = (L**3 * m_pendiente )/ (4 * b * d**3)
        print(f'Módulo elastico tangencial (Eb) es: {mod_elasticidad} MPa')


        #Tipo de fractura
        fractura = input("Ingrese el tipo de fractura que observa (Ductil, fragil:elastico o anelastico, comportamiento cauchoso): ")
        metodo = input("Desea calcular el esfuerzo de fluencia por metodo offset? (Si o No): ")

        if metodo.lower() == "si":

            if fractura.lower() == "ductil" or fractura.lower() == "fragil anelastico":
                #Metodo offset
                esfuerzo_offset = m_pendiente*deformacion_elastica
                deformacion_offset = deformacion_elastica+0.002
                pendiente_offset = np.polyfit(deformacion_offset,esfuerzo_offset, 1)
                offet_o = np.abs(deformacion - 0.002).argmin() #Se toma un valor de 0.02 para el offset
                # Crear un array de x
                x_space = np.linspace(deformacion_offset, 0.5, 100)
            


                # Visualización de la gráfica para seleccionar el esfuerzo de fluencia
                plt.figure(1)
                plt.plot(deformacion, esfuerzo)
                plt.plot(deformacion[:xx], m_pendiente*deformacion[:xx] + pendiente[1], label='Pendiente (m)' , color='orange', linestyle='--')
                plt.plot(deformacion[offet_o:xx], m_pendiente*deformacion[offet_o:xx] + pendiente_offset[1], label='offset' , color='black', linestyle='--')
                plt.xlabel('Defleccion [mm/mm]')
                plt.ylabel('Esfuerzo [MPa]')
                plt.title('Esfuerzo vs Defleccion')
                plt.show()

                # Ingreso del valor de esfuerzo de fluencia por metodo offset
                esfuerzo_offset = float(input("Ingrese el valor que considere para el esfuerzo de fluencia (Esfuerzo): "))

                # # Tomar dato del esfuerzo de fluencia por metodo offset
                # tolerancia = 1  # Define tu propia tolerancia
                # mask_fluencia = np.isclose(esfuerzo, esfuerzo_offset, atol=tolerancia)
                # #mask_fluencia = (esfuerzo == esfuerzo_offset) 
                # esf_seleccionado = esfuerzo[mask_fluencia]

                #Calculo del esfuerzo de fluencia maximo
                Sf_max = (np.abs(esfuerzo - esfuerzo_offset)).argmin()
                esfuerzo_fluencia_max = round(esfuerzo[Sf_max],3)
                deformacion_fluencia_max = round(deformacion[Sf_max],3)
                # print(Sf_max)
                print(f'El esfuerzo de fluencia maximo es: {esfuerzo_fluencia_max} MPa')
                print(f'Deformacion a la fluencia maxima: {deformacion_fluencia_max} mm/mm')

        else:
            #Calculo del esfuerzo a la fluencia o esfuerzo maximo
            esfuerzo_max = round(np.max(esfuerzo),3)
            dx_max = deformacion[np.argmax(esfuerzo)]
            print(f'El esfuerzo a la fluencia o maximo es: {esfuerzo_max} MPa')
            print(f'Deformacion a la fluencia: {dx_max} mm/mm')
    else:
        deformacion = deformacion_x
        esfuerzo = esfuerzo_y

    # Cálculo del esfuerzo a la fractura o esfuerzo último
    esfuerzo_ultimo = round(esfuerzo[-1], 3)
    dx_ultimo = round(deformacion[-1],3)
    print(f'El esfuerzo a la fractura o último es: {esfuerzo_ultimo} MPa')
    print(f'Deformación a la fractura: {dx_ultimo} mm/mm')


    # Cálculo ductilidad - Grafica
    if elastomero.lower() == 'no':
        ductilidad_grafica = round((deformacion[-1] - deformacion[0]) * 100, 3)
        print(f'Ductilidad medida por la gráfica es: {ductilidad_grafica} %')

        # Cálculo de tenacidad
        x_tenacidad = deformacion
        y_tenacidad = esfuerzo
        area_tenacidad = round(spi.trapezoid(y_tenacidad, x_tenacidad), 3)
        print(f'El área de tenacidad gráficamente es: {area_tenacidad} J/mm^2')

    # Cálculos con curvas de esfuerzo y deformación reales
    esfuerzo_real = esfuerzo * (1 + deformacion)
    deformacion_real = np.log(1 + deformacion)


    #Esfuerzo maximo real
    if elastomero.lower() == 'no':
        esfuerzo_max_real = round(np.max(esfuerzo_real), 3)
        dx_max_real = deformacion_real[np.argmax(esfuerzo_real)]
        print(f'El esfuerzo a la fluencia o máximo esfuerzo real es: {esfuerzo_max_real} MPa')
        print(f'Deformación a la fluencia real: {dx_max_real} mm/mm')

    # Gráficas
    # Grafica de esfuerzo vs deformacion ingenieril
    plt.figure(1)
    plt.plot(deformacion_x, esfuerzo_y)
    plt.xlabel('Defleccion [mm/mm]')
    plt.ylabel('Esfuerzo [MPa]')
    plt.title('Esfuerzo vs Defleccion')
    plt.legend([nombre_probeta], loc='upper left')

    plt.figure(2)
    plt.plot(deformacion, esfuerzo)
    plt.xlabel('Defleccion [mm/mm]')
    plt.ylabel('Esfuerzo [MPa]')
    plt.title('Esfuerzo vs Defleccion')
    plt.legend([nombre_probeta], loc='upper left')

    #Grafica de esfuerzo vs deformacion en la zona elastica
    if elastomero.lower() == 'no':
        plt.figure(3)
        plt.plot(deformacion_elastica, esfuerzo_elastica)
        plt.xlabel('Deformacion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Deformacion (Zona elastica)')
    
        #Grafica del modulo de elasticidad
        plt.figure(4)
        plt.plot(deformacion_elastica, pendiente[0]*deformacion_elastica + pendiente[1], label='Modulo de elasticidad' , color='red')
        plt.xlabel('Deformacion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Deformacion (Zona elastica)')
        plt.legend([ f"Pendiente (m): {m_pendiente} Mpa"], loc='upper left')

        #Grafica de propiedades
        if metodo.lower() == "si":
            if fractura.lower() == "ductil" or fractura.lower() == "fragil anelastico":
                plt.figure(5)
                plt.plot(deformacion, esfuerzo)
                plt.plot(deformacion[:xx], m_pendiente*deformacion[:xx] + pendiente[1], label='Pendiente (m)' , color='orange', linestyle='--')
                plt.plot(deformacion[offet_o:xx], m_pendiente*deformacion[offet_o:xx] + pendiente_offset[1], label='offset' , color='black', linestyle='--')
                plt.plot(deformacion_fluencia_max, esfuerzo_fluencia_max, 'ro')
                plt.plot(dx_ultimo, esfuerzo_ultimo, 'rx')
                plt.xlabel('Defleccion [mm/mm]')
                plt.ylabel('Esfuerzo [MPa]')
                plt.title('Esfuerzo vs Defleccion')
                plt.legend([nombre_probeta, f"Pendiente (m): {m_pendiente} Mpa", "Metodo offset", f"Sy_fluencia: {esfuerzo_fluencia_max} Mpa", f"Sb_fractura: {esfuerzo_ultimo} Mpa",f"Eb: {mod_elasticidad}"], loc='upper left')
        else:
            plt.figure(5)
            plt.plot(deformacion, esfuerzo)
            plt.plot(deformacion[:xx], m_pendiente*deformacion[:xx] + pendiente[1], label='Pendiente (m)' , color='orange', linestyle='--')
            plt.plot(dx_max, esfuerzo_max, 'ro')
            plt.plot(dx_ultimo, esfuerzo_ultimo, 'rx')
            plt.xlabel('Defleccion [mm/mm]')
            plt.ylabel('Esfuerzo [MPa]')
            plt.title('Esfuerzo vs Defleccion')
            plt.legend([nombre_probeta, f"Pendiente (m): {m_pendiente} Mpa", f"Sy_fluencia: {esfuerzo_max} Mpa", f"Sb_fractura: {esfuerzo_ultimo} Mpa",f"Eb: {mod_elasticidad}"], loc='upper left')


        plt.figure(6)
        plt.plot(deformacion, esfuerzo)
        plt.plot(deformacion[:xx], m_pendiente*deformacion[:xx] + pendiente[1], label='Pendiente (m)' , color='orange', linestyle='--')
        plt.plot(dx_ultimo, esfuerzo_ultimo, 'rx')
        plt.xlabel('Defleccion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Defleccion')
        plt.legend([nombre_probeta, f"Pendiente (m): {m_pendiente} Mpa", f"Sb_fractura: {esfuerzo_ultimo} Mpa",f"Eb: {mod_elasticidad}"], loc='upper left')
        
        #Gráfica de tenacidad
        plt.figure(7)
        plt.plot(x_tenacidad, y_tenacidad, label='Tenacidad', color='green')
        plt.fill_between(x_tenacidad, y_tenacidad, color='green', alpha=0.4, label='Área de tenacidad')
        plt.xlabel('Defleccion [mm/mm]')
        plt.ylabel('Esfuerzo [MPa]')
        plt.title('Esfuerzo vs Defleccion')
        plt.legend([ f"Tenacidad: {area_tenacidad} J/mm^2"], loc='upper left')

    #Grficas de curvas reales
    #Grafica de esfuerzo vs deformacion real
    plt.figure(8)
    plt.plot(deformacion_real, esfuerzo_real, color='orange')
    plt.xlabel('Deformacion real [mm/mm]')
    plt.ylabel('Esfuerzo real [MPa]')
    plt.title('Esfuerzo real vs Deformacion real')

    plt.figure(9)
    plt.plot(deformacion, esfuerzo, color='blue')
    plt.plot(deformacion_real, esfuerzo_real, color='orange')
    plt.xlabel('Deformacion [mm/mm]')
    plt.ylabel('Esfuerzo [MPa]')
    plt.title('Curva ingenieril vs real')
    plt.legend(["Curva ingenieril", "Curva real"], loc='upper right')

    plt.show()

# Uso de la función con valores proporcionados por el usuario
archivo = input("Ingrese el nombre del archivo .txt con los datos de la probeta: ")
d_usuario = float(input("Ingrese el espesor (d) de la probeta en mm: "))
b_usuario = float(input("Ingrese el ancho (b) de la probeta en mm: "))
L_usuario = float(input("Ingrese la longitud (L) o ditancia entre puntos de apoyo en mm: "))
#longitud_final_usuario = float(input("Ingrese la longitud final de la probeta en mm: "))
elastomero_usuario = input("El polimero es un elastomero si o no?: ")

analisis_probeta(archivo, d_usuario, b_usuario, L_usuario, elastomero_usuario)

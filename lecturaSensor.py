import serial #Para la comunicación serial
import csv #Para la creación de archivo csv
import win32api #Para detectar que una tecla ha sido presionada
from datetime import datetime #Para registrar la hora actual

import winsound

puertoArduino = "COM5" #Define el puerto al que está conectado el arduino
baudios = 9600 #Define la tasa de baudios
nombreArchivo = "datosSensor.csv"
lecturas = 30 #Número de lecturas por realizar, para poner fin al ciclo
linea = 0 #linea inicial
datos = [] #lista para almacenar los valores

#El programa espera a que uno indique que está listo para iniciar la toma de medidas
#al presionar la tecla "espacio".
while True:
    if win32api.GetKeyState(0x20)<0:
        print("Listo")
        break

#Al iniciar la toma de medidades del sensor de fuerza por medio de un click derecho
#el programa comienza simultáneamente la toma de medidades del sensor de efecto Hall
while True: 
    if win32api.GetKeyState(0x01)<0:
        ser = serial.Serial(puertoArduino, baudios) #abre puerto serial
        print("Conectado al puerto:" + puertoArduino)
        file = open(nombreArchivo, "w") # "a" agrega datos a archivo existente, "w" crea un archivo

        lecturaActual=str( "Voltaje (mV),  Hora")
        datos.append(lecturaActual.split(", "))

        #Obtención de datos
        while linea <= lecturas:
            #Lee una linea enviada por Serial.println() en el Arduino y la convierte en string 
            
            horaActual = str(datetime.now())[11:]
            lecturaActual=str(ser.readline().decode())[:-2] + ", " + horaActual
                    
            #Separa el string en elementos utilizando una coma como separador (CSV)
            #y los agrega al final de la lista 
            datos.append(lecturaActual.split(", "))
            linea = linea+1
            print(linea)


        #Creación del archivo
        with open(nombreArchivo, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(datos)

        print("Archivo creado con éxito")
        winsound.Beep(1000,500)
        file.close() #Cierra el archivo
        ser.close() #Cierra la conección al puerto serial
        break


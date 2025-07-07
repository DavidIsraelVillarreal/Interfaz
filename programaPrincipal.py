from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica
import time #Nos permite trabajar con delays
import board # type: ignore #Nos permite trabajar con los pines GPIO 
import digitalio # type: ignore
import adafruit_dht # type: ignore #Nos permite trabajar con el sensor DHT22
import busio # type: ignore #Permite la interacción con los buses I2C
import adafruit_ads1x15.ads1115 as ADS # type: ignore #Nos permite trabajar con el conversor ADC (ADS1115)
from serial import Serial, EIGHTBITS, STOPBITS_ONE, PARITY_NONE
from serial.serialutil import SerialException # type: ignore
import threading  # Sirve para ejecutar la lectura del sensor en un hilo separado
import firebase_admin # type: ignore
from firebase_admin import credentials, firestore # type: ignore
import requests
import os
import creacionInterfazPrincipal
import funcionesLecturaSensores

#Impedir que la pantalla se apague durante la ejecución del programa.
os.system("xset -dpms")
os.system("xset s noblank")
os.system("xset s off")

#Declarar diccionario que contendrá variables de datos de los sensores.
varCompartidas = {
    "pm25": -1,
    "pm10": -1,
    "datoHI": "---",
    "valueHeatIndex": -1,
    "uvIntensity": -1,
    "indicadorParada": False,
    "temperaturaFAjustada": -1000,
    "temperaturaCAjustada": -1000,
    "humedadC": -1,
    "interfazActiva": True
}

#Declarar e iniciar de variables
d=0 #Variable que incrementa al esperar que se ejecute el programa durante 5 segundos.
tiempoEjecucionInicio=time.time() #Marca de tiempo para ejecición del programa.
tiempoEjecucionFin = 0 #Marca de tiempo para ejecución del programa
internet = False 

#Configurar pin para detectar voltaje de batería
outRelay = digitalio.DigitalInOut(board.D5)
outRelay.direction = digitalio.Direction.OUTPUT
outRelay.value = True


#Establecer parámetros de la comunicación serie
port = "/dev/ttyUSB0" # Dirección del puerto serie al que se conectará.
baudrate = 9600

#CONVERSOR ADC
#Comandos para uso deL conversor ADC (ADS1115)
ADS.gain=1 #Establecer la ganancia con la que se manejará la lectura del conversor ADC
UVOUT = ADS.P2 #Pin A2 al que está conectada la salida del sensor GYML8511.
BATERYOUT = ADS.P0 # Pin A0 al que está conectada el divisor de voltaje.
i2c = busio.I2C(board.SCL, board.SDA) #Permite la comunicación por I2C (crea un objeto de la clase I2C y lo asigna a la variable i2c)
ads = ADS.ADS1115(i2c) #Creación de objeto de la clase ADS1115.

# Crear un objeto serial para comunicarse con el sensor
ser = Serial(port, baudrate=baudrate, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE)
ser.flushInput() # Limpiar el buffer de entrada

#SENSOR DE HUMEDAD Y TEMPERATURA DHT22
#Inicializar el sensor DHT22:
dhtDeviceExterior = adafruit_dht.DHT22(board.D6, use_pulseio=False)
dhtDeviceBateria = adafruit_dht.DHT22(board.D27, use_pulseio=False)

#------------------------------------------ FUNCIONES ------------------------------------------------------------
# Funciones de conectividad
def verificarInternet(): #Comprueba si hay conexión a internet
    global internet

    while internet == False:
        try:
            respuesta = requests.get("https://www.google.com", timeout=5)
            respuesta.raise_for_status()  # Lanza una excepción para códigos de error HTTP
            internet = True
        except requests.exceptions.RequestException as errorInternet:
            print("Error en la conexión a internet")
            print(errorInternet)
            internet = False
            continue

def iniciarFirestore():
    # Ruta al archivo de credenciales descargado desde Firebase
    cred = credentials.Certificate("/home/xibernetiq/Documents/Tesis/Interfaz/clave.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()

#---------------------------------------------------------------------------------------------------------------------
try:
    tiempoEjecucionFin = time.time()
    while (tiempoEjecucionFin - tiempoEjecucionInicio <= 5): #Esperar 5 segundos desde que se enciende la placa.
        d=d+1
        #print("ESPERE POR FAVOR")
        tiempoEjecucionFin = time.time()

    verificarInternet() #Verificar acceso a internet
    if (internet == True):
        #CONFIGURACIÓN DE INTERFAZ
        raiz = Tk() #Crea la raiz
        raiz.attributes('-fullscreen', True)
        interfaz = creacionInterfazPrincipal.interfazConContraseña(raiz, varCompartidas)
        db = iniciarFirestore()
        hiloLectura = threading.Thread(target=funcionesLecturaSensores.lecturaSensores, args=(varCompartidas, UVOUT, BATERYOUT, outRelay, dhtDeviceExterior, dhtDeviceBateria, ads, ser, i2c, interfaz, db))
        time.sleep(1)
        hiloLectura.start()
        raiz.mainloop() #Establece un bucle para que la raiz esté activa siempre
    else:
        print("No hay conexión a internet")

except KeyboardInterrupt:
    print("*****SALIDA DEL PROGRAMA*****")
    exit(0)
    
except RuntimeError as error:
    print(f"El error fue: {error}") 

except Exception as error:
    print(f"El error fue:{error}") 

except BaseException as error:
    print(f"El error fue:{error}")
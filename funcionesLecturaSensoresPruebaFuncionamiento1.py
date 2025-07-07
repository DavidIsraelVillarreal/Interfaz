from __future__ import print_function
import time, struct #Nos permite trabajar con delays
from adafruit_ads1x15.analog_in import AnalogIn # type: ignore #Nos permite leer los valores analógicos.
import datetime
import subprocess
import matplotlib.pyplot as plt
import ajustarValores


#------------------------------------------ FUNCIONES ------------------------------------------------------------
# Función para subir datos a Firestore
def subirDatosFirestore(collection_name, document_id, data, db, varCompartidas):
    """
    Sube datos a Firestore.

    Args:
        collection_name (str): El nombre de la colección en Firestore.
        document_id (str): El ID del documento (puedes usar None para generar un ID automáticamente).
        data (dict): Los datos a guardar en Firestore.

    Returns:
        str: Mensaje de éxito o error.
    """
    #Inicializar variables de tiempo:
    tiempoInicioLatencia = 0
    tiempoFinLatencia = 0
    tiempoInicioLatenciaSinID=0
    tiempoFinLatenciaSinID = 0
    latencia = 0
    valorPromedioConID=0
    valorMinConID=0
    valorMaxConID=0
    valorPromedioSinID=0
    valorMinSinID=0
    valorMaxSinID=0

    try:
        if (varCompartidas["tiempo2minFin"]-varCompartidas["tiempo2minInicio"] < 600 and varCompartidas["indic"] == 0):
            varCompartidas["tiempo2minInicio"] = time.time()
            varCompartidas["indic"] = varCompartidas["indic"]+1
        print("1")
        if(document_id=="null"):
            tiempoInicioLatenciaSinID=time.time()
            db.collection(collection_name).add(data)
            tiempoFinLatenciaSinID=time.time()
            print("*-*-*-*-*-*- Entro a (1) *-*-*-*-*-*- ")
            print("Datos subidos a Firestore sin id doc")
            latenciaSinID = tiempoFinLatenciaSinID-tiempoInicioLatenciaSinID
            print(">>>>>>>> Latencia (sin id doc): {:.3f} <<<<<<<<<<".format(latenciaSinID))
            varCompartidas["listaLatenciasSinID"].append(latenciaSinID)
            varCompartidas["tiempo2minFin"] = time.time()
        print("2")
        if document_id != "null":
            tiempoInicioLatencia=time.time()
            db.collection(collection_name).document(document_id).set(data)
            tiempoFinLatencia=time.time()
            print("*-*-*-*-*-*- Entro a (2) *-*-*-*-*-*- ")
            print("Datos subidos a Firestore con id doc")
            latencia = tiempoFinLatencia-tiempoInicioLatencia
            print(">>>>>>>> Latencia: {:.3f} <<<<<<<<<<".format(latencia))
            varCompartidas["listaLatencias"].append(latencia)
            varCompartidas["tiempo2minFin"] = time.time()
        print("3")
        print(varCompartidas["indic"])
        if (varCompartidas["tiempo2minFin"]-varCompartidas["tiempo2minInicio"] >= 600 and varCompartidas["indic"] ==1):
            print("4")
            varCompartidas["indicadorParada"] = True
            #Valor promedio, mínimo y máximo de la latencia con ID especificado
            valorPromedioConID=sum(varCompartidas["listaLatencias"])/len(varCompartidas["listaLatencias"])
            valorMinConID=min(varCompartidas["listaLatencias"])
            valorMaxConID=max(varCompartidas["listaLatencias"])
            print("**** Valores para latencias (con ID) ****")
            print("Valor promedio: {}".format(valorPromedioConID))
            print("Valor mínimo: {}".format(valorMinConID))
            print("Valor máximo: {}".format(valorMaxConID))
            print("Total de escrituras: {}".format(len(varCompartidas["listaLatencias"])))

            #Valor promedio, mínimo y máximo de la latencia sin ID especificado
            valorPromedioSinID=sum(varCompartidas["listaLatenciasSinID"])/len(varCompartidas["listaLatenciasSinID"])
            valorMinSinID=min(varCompartidas["listaLatenciasSinID"])
            valorMaxSinID=max(varCompartidas["listaLatenciasSinID"])
            print()
            print("**** Valores para latencias (sin ID) ****")
            print("Valor promedio: {}".format(valorPromedioSinID))
            print("Valor mínimo: {}".format(valorMinSinID))
            print("Valor máximo: {}".format(valorMaxSinID))
            print("Total de escrituras: {}".format(len(varCompartidas["listaLatenciasSinID"])))

            #Gráficas de latencia
            plt.plot(varCompartidas["listaLatencias"], label="Con ID especificado")
            plt.plot(varCompartidas["listaLatenciasSinID"], label="Sin ID especificado")
            plt.xlabel("Número de escritura")
            plt.ylabel("Latencia (s)")
            plt.title("Latencias de Escritura en Firestore en 10 min")
            plt.legend()
            plt.ylim(0,0.5)
            plt.show()
            varCompartidas["tiempo2minInicio"] = time.time()
            varCompartidas["tiempo2minFin"] = time.time() 
            varCompartidas["listaLatencias"]=[]
            varCompartidas["listaLatenciasSinID"]=[]
            varCompartidas["indic"]=0

    except Exception as e:
        print(f"Error al subir los datos: {e}")

# Funciones para sensor GYLM8511 
def mapfloat(chan, in_min,  in_max,  out_min,  out_max): #Función para realizar una función map con flotantes.
    return (chan - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def heatIndexCalc(t, rH):
    heatIndex = 16.923+((1.85212*pow(10,-1))*t)+(5.37941*rH)-((1.00254*pow(10,-1))*t*rH)+((0.41695*pow(10,-3))*pow(t,2))+((7.28898*pow(10,-3)*pow(rH,2)))+((3.45372*pow(10,-4))*pow(t,2)*rH)-((8.14971*pow(10,-4))*t*pow(rH,2))+((1.02102*pow(10,-5))*pow(t,2)*pow(rH,2))-((3.8646*pow(10,-5))*pow(t,3))+((2.91583*pow(10,-5))*pow(rH,3))+((1.42721*pow(10,-6))*pow(t,3)*rH)+((1.97483*pow(10,-7))*t*pow(rH,3))-((2.18429*pow(10,-8))*pow(t,3)*pow(rH,2))+((8.43296*pow(10,-10))*pow(t,2)*pow(rH,3))-((4.81975*pow(10,-11))*pow(t,3)*pow(rH,3))
    return heatIndex

#----------------------------------------  LECTURA DE SENSORES ---------------------------------------- 
def lecturaSensores(varCompartidas, UVOUT, BATERYOUT, outRelay, dhtDeviceExterior, dhtDeviceBateria, ads, ser, i2c, db):
    #Declaración de variables y constantes para la función
    finalizaPorVoltaje = False #Marca para detectar si se cerró el programa a causa de un bajo voltaje.
    temperaturaC=-1000 #Mandar
    humedad=-1 #Mandar
    apagadoExitoso = False #Indica si el proceso de apagado de la Raspberry Pi tuvo algún inconveniente.
    voltajeBateria = 0 #Variable que almacena el voltaje actual de la batería.
    lecturaInicialDHT22 = 0 #Variable que indica si se realizó la medición inicial de los sensores DHT22.
    tiempoUltimaLecturaDHT22_1=0 #Marca de tiempo para el sensor DHT22 que está hacia el exterior.
    tiempoUltimaLecturaDHT22_2=0 #Marca de tiempo para el sensor DHT22 de la batería.
    temperaturaCAnterior1 = -1000 # Variable que permite el intento de una nueva medición del DHT22 en caso de un error durante la lectura.
    temperaturaCAnterior2 = -1000 # Variable que permite el intento de una nueva medición del DHT22 en caso de un error durante la lectura.
    temperatura2 = -1000 #Temperatura del sensor DHT22 para la batería
    tiempoUltimaLecturaSDS011=0 #Tiempo de referencia para ejecutar lecturas de sensor SDS011 y su impresión de resultados.
    tiempoImpresion = 0 #Marca de tiempo para imprimir los datos en Firestore.
    HEADER_BYTE = b"\xAA" #Byte de inicio del paquete
    COMMANDER_BYTE = b"\xC0" #Byte de comando
    TAIL_BYTE = b"\xAB" #Byte final del paquete
    byte, previousbyte = b"\x00", b"\x00" #Variables para almacenar bytes recibidos
    tail = b'\x00' 
    checksum_verified = False
    tiempoActualizarInterfazFin = 0 #Marca de tiempo para actualizar interfaz.
    tiempoActualizarInterfazInicio = time.time() #Marca de tiempo para actualizar interfaz.
    tiempoBateria = time.time()
    voltajeChan0=13.27 #Variable en la que se almacena el voltaje detectado en el divisor de voltaje.
    horaActual = datetime.datetime.now().time() #Marca de tiempo para subir datos a Firestore
    horaInicio = datetime.time(10, 0)  # 10:00 AM
    horaFin = datetime.time(14, 0)    # 14:00 PM
    hora = 0 #Marca de tiempo para ajuste de valores
    minuto = 0 #Marca de tiempo para ajuste de valores

    while varCompartidas["indicadorParada"] == False:
        try:
            outRelay.value = True #Hacer que el relé esté sin activarse.
            tiempoActual = time.time() #Establecer el tiempo actual en el que comienza la lectura de los sensores            
            #---------------------------- Obtener datos del sensor DHT22 y el índice de calor e imprimirlos----------------------------            
            if (tiempoActual - tiempoUltimaLecturaDHT22_1 >= 2) and (tiempoActual - tiempoUltimaLecturaDHT22_2 >= 2):
                temperaturaC = dhtDeviceExterior.temperature #Obtener la temperatura por el sensor DHT22
                humedad = dhtDeviceExterior.humidity #Obtiene la humedad del ambiente
                temperatura2 = dhtDeviceBateria.temperature
                tiempoActual = time.time()
                tiempoUltimaLecturaDHT22_1 = tiempoActual
                tiempoUltimaLecturaDHT22_2 = time.time()
                lecturaInicialDHT22 = lecturaInicialDHT22+1
            
                if (lecturaInicialDHT22 == 1):
                    while(temperaturaC==-1000 and humedad==-1) or (temperaturaC == None and humedad==None):
                        try:
                            tiempoActual = time.time()
                            if tiempoActual - tiempoUltimaLecturaDHT22_1 >= 2:
                                temperaturaC = dhtDeviceExterior.temperature #Obtener la temperatura por el sensor DHT22
                                humedad = dhtDeviceExterior.humidity #Obtiene la humedad del ambiente
                                tiempoActual = time.time()
                                tiempoUltimaLecturaDHT22_1 = tiempoActual
                        except RuntimeError as error1:
                            print(f"1* El error fue: {error1}")
                            tiempoActual = time.time()
                            tiempoUltimaLecturaDHT22_1 = tiempoActual
                            temperaturaC= temperaturaCAnterior1
                            continue # Genera la siguiente iteración del bucle

                        except Exception as error2:
                            print(f"2* El error fue:{error2}")
                            continue # Genera la siguiente iteración del bucle

                        except BaseException as error3:
                            print(f"3* El error fue:{error3}")
                            continue

                    while(temperatura2==-1000) or (temperatura2 == None):
                        try:
                            tiempoActual = time.time()
                            if tiempoActual - tiempoUltimaLecturaDHT22_2 >= 2:
                                temperatura2 = dhtDeviceBateria.temperature #Obtener la temperatura por el sensor DHT22
                                tiempoActual = time.time()
                                tiempoUltimaLecturaDHT22_2 = time.time()
                        except RuntimeError as errorExtra1:
                            print(f"1* El error fue: {errorExtra1}") # Nos muestra especificamente cuál fue el error que se generó
                            tiempoActual = time.time()
                            tiempoUltimaLecturaDHT22_2 = time.time
                            temperatura2= temperaturaCAnterior2
                            continue # Genera la siguiente iteración del bucle

                        except Exception as errorExtra2:
                            print(f"2* El error fue:{errorExtra2}") # Nos muestra especificamente cuál fue la excepción que se generó
                            continue # Genera la siguiente iteración del bucle

                        except BaseException as errorExtra3:
                            print(f"3* El error fue:{errorExtra3}")
                            continue

                    lecturaInicialDHT22 = 0

                    now = datetime.datetime.now()
                    hora= now.hour
                    minuto = now.minute

                    varCompartidas["temperaturaCAjustada"] = ajustarValores.ajustarValoresTemperatura(temperaturaC, hora)
                    varCompartidas["temperaturaFAjustada"] = varCompartidas["temperaturaCAjustada"] * (9 / 5) + 32 #Convertir de grados centígrados a grados Fahrenheit
                    varCompartidas["humedadC"] = ajustarValores.ajustarValoresHumedad(temperaturaC, humedad, hora)
                    varCompartidas["valueHeatIndex"] = round(heatIndexCalc(varCompartidas["temperaturaFAjustada"], varCompartidas["humedadC"]))
                    #Impresión de valores en el Terminal
                    print("----------------------- TEMPERATURA, HUMEDAD E ÍNDICE DE CALOR -----------------------")
                    print("Temp: {:.1f} °F / {:.1f} °C    Humedad: {:.2f}% ".format(varCompartidas["temperaturaFAjustada"], varCompartidas["temperaturaCAjustada"], varCompartidas["humedadC"]))

                    if (varCompartidas["valueHeatIndex"] <= 26) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Seguro".format(varCompartidas["valueHeatIndex"]))
                    elif (27 <= varCompartidas["valueHeatIndex"] <= 32) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Precaución".format(varCompartidas["valueHeatIndex"]))
                    elif (33 <= varCompartidas["valueHeatIndex"] <= 40) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Precaución Extrema".format(varCompartidas["valueHeatIndex"]))
                    elif (41 <= varCompartidas["valueHeatIndex"] <= 51) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Peligro".format(varCompartidas["valueHeatIndex"]))
                    elif (52 <= varCompartidas["valueHeatIndex"] <= 92) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Peligro Extremo".format(varCompartidas["valueHeatIndex"]))
                    elif (93 <= varCompartidas["valueHeatIndex"]) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"]<= 100):
                        print("Índice de calor: {} / Mortal".format(varCompartidas["valueHeatIndex"]))
                    else:
                        print("No cumple el rango de temperatura de 80-110 °F o el de humedad relativa de 40-100% (Heat Index: {})".format(varCompartidas["valueHeatIndex"]))
            #---------------------------- Obtener datos del sensor SDS011 e imprimirlos en conjunto con los del GYML8511 ----------------------------
            tiempoActual = time.time()
            if tiempoActual - tiempoUltimaLecturaSDS011 >= 1:
                #---------------------------- Sensor GYLM8511 ----------------------------  
                voltajeChan2 = AnalogIn(ads, UVOUT).voltage #Obtiene el valor del voltaje del pin UVOUT.
                varCompartidas["uvIntensity"] = mapfloat(voltajeChan2, 0.99, 2.8, 0.0, 15.0) #Valores obtenidos del datasheet.

                #---------------------------- Sensor SDS011 -----------------------------
                #Inicializar variables para que ingrese siempre al bucle while:
                checksum_verified = False
                tail = b'\x00'
                TAIL_BYTE = b"\xAB"

                while (tail != TAIL_BYTE and checksum_verified == False):
                    try:
                        tiempoActual = time.time()
                        if (tiempoActual - tiempoUltimaLecturaSDS011>=1):
                            previousbyte = byte
                            byte = ser.read(size=1) #Leer 1 byte del sensor.
                            #print(byte)
                            tiempoActual = time.time()
                            tiempoUltimaLecturaSDS011 = tiempoActual
                            while (previousbyte != HEADER_BYTE and byte != COMMANDER_BYTE):
                                try:
                                    tiempoActual = time.time()
                                    if (tiempoActual - tiempoUltimaLecturaSDS011>=1):
                                        previousbyte = byte
                                        byte = ser.read(size=1) #Leer 1 byte del sensor.
                                        #print(byte)
                                        tiempoActual = time.time()
                                        tiempoUltimaLecturaSDS011 = tiempoActual
                                except KeyboardInterrupt:
                                    print("*****SALIDA DEL PROGRAMA (2)*****")
                                    #sys.exit()
                                    exit(0)
                                except BaseException as error4:
                                    print(f"1**) El error fue:{error4}")
                                    continue
                            #Al salir del while nos indica que Obtuvimos un encabezado de paquete válido
                            packet = ser.read(size=8) # Leer 8 bytes
                                    
                            #Utiliza struct.unpack para extraer los valores de PM2.5, PM10, ID y checksum del paquete.
                            readings = struct.unpack('<HHcccc', packet)
                                    
                            #Medidas obtenidas del sensor.
                            varCompartidas["pm25"] = readings[0]/10.0
                            varCompartidas ["pm10"] = readings[1]/10.0
                                    
                                    
                            #Realización de checksums para verificar que no existieron fallos en la transmisión.
                            checksum = readings[4][0]
                            calculated_checksum = sum(packet[:6]) & 0xFF
                            checksum_verified = (calculated_checksum == checksum)
                                    
                            # Message tail.
                            tail = readings[5]
                            tiempoActual = time.time()
                            tiempoUltimaLecturaSDS011 = tiempoActual
                    except KeyboardInterrupt:
                            print("*****SALIDA DEL PROGRAMA (3)*****")
                            #sys.exit()
                            exit(0)
                    except BaseException as error5:
                        print(f"1**) El error fue:{error5}")
                        continue
                
                # Impresión de datos en el Terminal
                print("********* Tiempo de finalización de lectura de sensores:  {:.2f} s *********".format(time.time()))
                print("----------------------- INTENSIDAD UV, PM2,5 Y PM10 -----------------------")
                print("Intensidad UV: {} (mW/cm^2) y con decimales: {}".format(round(varCompartidas["uvIntensity"]), varCompartidas["uvIntensity"]))
                print("PM 2.5:", varCompartidas["pm25"], " µg/m³  PM 10:", varCompartidas ["pm10"], " µg/m³")
                print(" ") 
            #----------------------------------------  IMPRESIÓN a Firebase---------------------------------------- 
            horaActual = datetime.datetime.now().time() #Este debo borrar cuando deje el definitivo
            tiempoActual = time.time()            
            if horaInicio <= horaActual <= horaFin:
                if tiempoActual - tiempoImpresion >= 2:
                    data_real_time = {
                        "temperatura":varCompartidas["temperaturaCAjustada"],
                        "calor":varCompartidas["valueHeatIndex"],
                        "humedad": varCompartidas["humedadC"],
                        "radiacion":round(varCompartidas["uvIntensity"]),
                        "pm10": varCompartidas ["pm10"],
                        "pm25": varCompartidas["pm25"]
                    }
                    data_historial = {
                        "temperatura": varCompartidas["temperaturaCAjustada"],
                        "calor":varCompartidas["valueHeatIndex"],
                        "humedad": varCompartidas["humedadC"],
                        "radiacion":round(varCompartidas["uvIntensity"]),
                        "pm10": varCompartidas ["pm10"],
                        "pm25": varCompartidas["pm25"],
                        "tiempo":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                    subirDatosFirestore("real_time", "datos_actuales", data_real_time, db, varCompartidas)
                    subirDatosFirestore("historial", "null", data_historial, db, varCompartidas)
                    tiempoActual = time.time()
                    tiempoImpresion = tiempoActual
            
            #------------------------------------------------------------------------------------------------------------            
            tiempoActualizarInterfazFin = time.time()
            if (tiempoActualizarInterfazFin - tiempoActualizarInterfazInicio >= 2) and (varCompartidas["interfazActiva"] == True):
                #funcionesInterfaz.actualizarInterfaz(varCompartidas,  interfaz.dato1, interfaz.imagen1, interfaz.dato2, interfaz.imagen2, interfaz.dato3, interfaz.imagen3, interfaz.dato4, interfaz.imagen4, interfaz.dato5, interfaz.raiz)
                tiempoActualizarInterfazFin = time.time()
                tiempoActualizarInterfazInicio = time.time()
                
            tiempoActual = time.time()
            if (tiempoActual - tiempoBateria >= 60) or (temperatura2 >= 42): #Medición de voltaje cada minuto.
                outRelay.value = False
                time.sleep(0.5)
                voltajeChan0 = AnalogIn(ads, BATERYOUT).voltage # Obtiene el valor del divisor de voltaje.
                voltajeBateria = (voltajeChan0*4420)/1000 #Calcula el voltaje de la batería
                print("Voltaje Batería: {} (V)".format(voltajeBateria))
                outRelay.value = True
                tiempoBateria = time.time()
                tiempoActual = time.time()
                if (voltajeBateria<=11) or (temperatura2 >= 42): #Cerrar aplicación y apagar placa cuando el voltje de batería sea menor o igual a 10,55 V o cuando la temperatura de la batería sea mayor o igual a 56 C.
                    finalizaPorVoltaje = True
                    varCompartidas["indicadorParada"] = True


        except KeyboardInterrupt:
            print("*****SALIDA DEL PROGRAMA (4)*****")
            varCompartidas["indicadorParada"] = True
        except RuntimeError as error6:
            print(f"1) El error fue: {error6}") # Nos muestra especificamente cuál fue el error que se generó
            time.sleep(2)
            continue # Genera la siguiente iteración del bucle
        except Exception as error7:
            print(f"2) El error fue:{error7}") # Nos muestra especificamente cuál fue la excepción que se generó
            continue

    #--------------- SE FINALIZÓ EL PROGRAMA ---------------
    if (finalizaPorVoltaje == False):
        try:
            dhtDeviceExterior.exit() # Salida segura del sensor
        except Exception as e:
            print(f"Error al liberar DHT Exterior: {e}")
        try:
            dhtDeviceBateria.exit()
        except Exception as e:
            print(f"Error al liberar DHT Batería: {e}")
        try:
            outRelay.value = True # Asegura que el relé esté en estado seguro
        except Exception as e:
            print(f"Error al configurar relé: {e}")
        try:
            i2c.deinit() # Detiene la comunicación I2C
        except Exception as e:
            print(f"Error al detener I2C: {e}")
        try:
            ser.close() # Cierra el puerto serie
        except Exception as e:
            print(f"Error al cerrar puerto serie: {e}")
        time.sleep(1)
        exit(0)

    else:
        try:
            dhtDeviceExterior.exit() # Salida segura del sensor
        except Exception as e:
            print(f"Error al liberar DHT Exterior: {e}")
        try:
            dhtDeviceBateria.exit()
        except Exception as e:
            print(f"Error al liberar DHT Batería: {e}")
        try:
            outRelay.value = True # Asegura que el relé esté en estado seguro
        except Exception as e:
            print(f"Error al configurar relé: {e}")
        try:
            i2c.deinit() # Detiene la comunicación I2C
        except Exception as e:
            print(f"Error al detener I2C: {e}")
        try:
            ser.close() # Cierra el puerto serie
        except Exception as e:
            print(f"Error al cerrar puerto serie: {e}")
        time.sleep(2)
        apagadoExitoso = False
        while (apagadoExitoso == False):
            try:
                subprocess.run(["sudo", "shutdown", "-h", "now"])  # Ejecuta el comando shutdown
                apagadoExitoso = True
                print("Apagando Raspberry Pi...")
            except subprocess.CalledProcessError:
                print(f"Reintentando en 5 segundos...")
                time.sleep(5)
            except FileNotFoundError:
                print("Error: El comando 'sudo' o 'shutdown' no se encontraron. Verifica la instalación.")
                break
            except Exception:
                print(f"Reintentando en 5 segundos...")
                time.sleep(5)
        exit(0)
from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica

#-------------------- Funciones para Valores del Bloque 1 --------------------
def actualizarInterfaz(varCompartidas, dato1, imagen1, dato2, imagen2, dato3, imagen3, dato4, imagen4, dato5, raiz):
    #---------------------------- Actualizar datos de interfaz ----------------------------
    pm25 = varCompartidas["pm25"]
    pm10 = varCompartidas ["pm10"]
    uvIntensity = varCompartidas["uvIntensity"]
    temperaturaCAjustada = varCompartidas["temperaturaCAjustada"]
    temperaturaFAjustada = varCompartidas["temperaturaFAjustada"]
    humedadC = varCompartidas["humedadC"]
    valueHeatIndex = varCompartidas["valueHeatIndex"]

    if (uvIntensity == None):
        uvIntensity =-1
    if (pm10 == None):
        pm10 = -1
    if (pm25==None):
        pm25 = -1
    if (temperaturaCAjustada == None):
        temperaturaCAjustada = -1
    if (temperaturaFAjustada == None):
        temperaturaFAjustada = -1
    if (humedadC == None):
        humedadC = -1
    
    print("************************* Actualización Iniciada *****************************")
    #-------------------- Bloque 1 --------------------
    dato1.config(text="NIVEL: {}\n{}".format(round(uvIntensity), printIUV(round(uvIntensity))), bg=colorIUV(round(uvIntensity)))
    imagen1.config(file=imagenIUV(round(uvIntensity)))

    #-------------------- Bloque 2 --------------------
    dato2.config(text=printCalidadAire(pm25, pm10), bg=colorCalidadAire(pm25, pm10))
    imagen2.config(file=imagenCalidadAire(pm25, pm10))

    #-------------------- Bloque 3 --------------------
    imagen3.config(file=imagenHumedad(humedadC))

    #-------------------- Bloque 4 --------------------
    dato3.config(text="{:.2f} °C".format(temperaturaCAjustada), bg=colorTemperatura(temperaturaCAjustada)) 
    dato4.config(text="{:.1f} °F".format(temperaturaFAjustada), bg=colorTemperatura(temperaturaCAjustada))
    imagen4.config(file=imagenTemperatura(temperaturaCAjustada))

    dato5.config(text=textoIndiceCalor(valueHeatIndex, temperaturaFAjustada, humedadC), bg=colorIndiceCalor(valueHeatIndex, temperaturaFAjustada, humedadC)) #Debo cambiar el 1 por int(uvIntensity) y Bajo por la variable de la función que me dirá si el valor de UV es bajo, alto o medio.

#-------------------- Funciones para Valores del Bloque 1 --------------------
def printIUV(indiceUV): #Indica de forma Textual el valor del Índice UV
    if (indiceUV<=2):
        datoIUV = "BAJO"
    elif (3<=indiceUV<=5):
        datoIUV = "MODERADO"
    elif (6<=indiceUV<=7):
        datoIUV = "ALTO"
    elif (8<=indiceUV<=10):
        datoIUV = "MUY ALTO"
    elif (indiceUV>=11):
        datoIUV = "EXTREMO"
    else:
        datoIUV = "N/A" #Error en la medición
    return datoIUV

def colorIUV(indiceUV): #Establece el color de la etiqueta del valor del índice UV
    if (indiceUV<=1):
        bgIUV="#4eb400"
    elif (indiceUV==2):
        bgIUV="#a0ce00"
    elif (indiceUV==3):
        bgIUV="#f7e400" 
    elif (indiceUV==4):
        bgIUV="#f8b600"
    elif (indiceUV==5):
        bgIUV="#f88700"
    elif (indiceUV==6):
        bgIUV="#f85900"
    elif (indiceUV==7):
        bgIUV="#e82c0e" 
    elif (indiceUV==8):
        bgIUV="#d8001d"
    elif (indiceUV==9):
        bgIUV="#ff0099"
    elif (indiceUV==10):
        bgIUV="#b54cff"
    elif (indiceUV>=11):
        bgIUV="#998cff"
    else:
        bgIUV="#F2F2F2"
    return bgIUV

def imagenIUV(indiceUV): #Indica de forma gráfica el índice UV
    if (indiceUV<=2):
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoUV_1SF.png"
    elif (3<=indiceUV<=5):
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoUV_2SF.png"
    elif (6<=indiceUV<=7):
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoUV_3SF.png"
    elif (8<=indiceUV<=10):
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoUV_4SF.png" 
    elif (indiceUV>=11):
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoUV_5SF.png"
    else:
        imagen1Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoMalaLectura.png"
    return imagen1Funcion

#-------------------- Funciones para Valores del Bloque 2 --------------------
def printCalidadAire(valorPM25, valorPM10): #Indica de forma textual el valor de la calidad del aire.
    if (0<=round(valorPM25)<=25) or (0<=round(valorPM10)<=50):
        datoCalidadAire = "ÓPTIMO"
    elif (26<=round(valorPM25)<=50) or (51<=round(valorPM10)<=100):
        datoCalidadAire = "BUENO"
    elif (51<=round(valorPM25)<=150) or (101<=round(valorPM10)<=250):
        datoCalidadAire = "PRECAUCIÓN"
    elif (151<=round(valorPM25)<=250) or (251<=round(valorPM10)<=400):
        datoCalidadAire = "ALERTA"
    elif (251<=round(valorPM25)<=350) or (401<=round(valorPM10)<=500):
        datoCalidadAire = "ALARMA"
    elif (350<round(valorPM25)) or (500<round(valorPM10)):
        datoCalidadAire = "EMERGENCIA"
    else:
        datoCalidadAire = "N/A" #Error en la medición
    return datoCalidadAire

def colorCalidadAire(valorPM25, valorPM10): #Establece el color de la etiqueta de la calidad del aire
    if (0<=round(valorPM25)<=25) or (0<=round(valorPM10)<=50):
        bgCalidadAire = "#FFFFFF"
    elif (26<=round(valorPM25)<=50) or (51<=round(valorPM10)<=100):
        bgCalidadAire = "#5EFF51"
    elif (51<=round(valorPM25)<=150) or (101<=round(valorPM10)<=250):
        bgCalidadAire = "#C3C3C3"
    elif (151<=round(valorPM25)<=250) or (251<=round(valorPM10)<=400):
        bgCalidadAire = "#FFF83D"
    elif (251<=round(valorPM25)<=350) or (401<=round(valorPM10)<=500):
        bgCalidadAire = "#FFB61B"
    elif (350<round(valorPM25)) or (500<round(valorPM10)):
        bgCalidadAire = "#EB3D3D"
    else:
        bgCalidadAire="#F2F2F2" #Error en la medición
    return bgCalidadAire

def imagenCalidadAire(valorPM25, valorPM10): #Indica de forma gráfica la calidad del aire
    if (0<=round(valorPM25)<=25) or (0<=round(valorPM10)<=50):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire1F.png"
    elif (26<=round(valorPM25)<=50) or (51<=round(valorPM10)<=100):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire2F.png"
    elif (51<=round(valorPM25)<=150) or (101<=round(valorPM10)<=250):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire3F.png"
    elif (151<=round(valorPM25)<=250) or (251<=round(valorPM10)<=400):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire4F.png" 
    elif (251<=round(valorPM25)<=350) or (401<=round(valorPM10)<=500):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire5F.png"
    elif (350<round(valorPM25)) or (500<round(valorPM10)):
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoCalidadAire6F.png"
    else:
        imagen2Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
    return imagen2Funcion

#-------------------- Funciones para Valores del Bloque 3 --------------------
def imagenHumedad(valorHumedad): #Indica de forma gráfica el procentaje de humedad
    if (0<=valorHumedad<=2.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad2,5.png"
    elif (2.5<valorHumedad<=5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad5.png"
    elif (5<valorHumedad<=7.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad7,5.png"
    elif (7.5<valorHumedad<=10):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad10.png" 
    elif (10<valorHumedad<=12.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad12,5.png"
    elif (12.5<valorHumedad<=15):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad15.png"
    elif (15<valorHumedad<=17.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad17,5.png" 
    elif (17.5<valorHumedad<=20):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad20.png" 
    elif (20<valorHumedad<=22.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad22,5.png"  
    elif (22.5<valorHumedad<=25):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad25.png" 
    elif (25<valorHumedad<=27.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad27,5.png"
    elif (27.5<valorHumedad<=30):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad30.png"
    elif (30<valorHumedad<=32.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad32,5.png"
    elif (32.5<valorHumedad<=35):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad35.png" 
    elif (35<valorHumedad<=37.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad37,5.png"
    elif (37.5<valorHumedad<=40):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad40.png"
    elif (40<valorHumedad<=42.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad42,5.png" 
    elif (42.5<valorHumedad<=45):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad45.png" 
    elif (45<valorHumedad<=47.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad47,5.png"  
    elif (47.5<valorHumedad<=50):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad50.png" 
    elif (50<valorHumedad<=52.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad52,5.png"
    elif (52.5<valorHumedad<=55):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad55.png"
    elif (55<valorHumedad<=57.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad57,5.png"
    elif (57.5<valorHumedad<=60):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad60.png" 
    elif (60<valorHumedad<=62.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad62,5.png"
    elif (62.5<valorHumedad<=65):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad65.png"
    elif (65<valorHumedad<=67.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad67,5.png" 
    elif (67.5<valorHumedad<=70):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad70.png" 
    elif (70<valorHumedad<=72.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad72,5.png"  
    elif (72.5<valorHumedad<=75):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad75.png" 
    elif (75<valorHumedad<=77.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad77,5.png"
    elif (77.5<valorHumedad<=80):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad80.png"
    elif (80<valorHumedad<=82.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad82,5.png"
    elif (82.5<valorHumedad<=85):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad85.png" 
    elif (85<valorHumedad<=87.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad87,5.png"
    elif (87.5<valorHumedad<=90):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad90.png"
    elif (90<valorHumedad<=92.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad92,5.png" 
    elif (92.5<valorHumedad<=95):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad95.png" 
    elif (95<valorHumedad<=97.5):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad97,5.png"  
    elif (97.5<valorHumedad<=100):
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad100.png" 
    else:
        imagen3Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad0.png"
    return imagen3Funcion

#-------------------- Funciones para Valores del Bloque 4 --------------------
def colorTemperatura(valorTemperaturaC): #Establece el color de las etiquetas de la temperatura
    if (valorTemperaturaC<=0):
        bgTemperatura = "#0071C1"
    elif (0<valorTemperaturaC<=18):
        bgTemperatura = "#00B1EF"
    elif (18<valorTemperaturaC<=24):
        bgTemperatura = "#FFFF00"
    elif (24<valorTemperaturaC<=35):
        bgTemperatura = "#FFC000"
    else:
        bgTemperatura = "#FE0000"
    return bgTemperatura

def imagenTemperatura(valortemperaturaC): #Establece el ícino en base a la temperatura
    if (valortemperaturaC<=0):
        imagen4Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoTemp1.png"
    elif (0<valortemperaturaC<=18):
        imagen4Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoTemp2.png"
    elif (18<valortemperaturaC<=24):
        imagen4Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoTemp3.png"
    elif (24<valortemperaturaC<=35):
        imagen4Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoTemp4.png"
    else:
        imagen4Funcion="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoTemp5.png"
    return imagen4Funcion

def textoIndiceCalor(valorIndiceCalor, valorTemperaturaF, valorHumedad): #Establece el texto en base al valor del índice de calor
    if (valorIndiceCalor <= 26) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "SEGURO"
    elif (27 <= valorIndiceCalor <= 32) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "PRECAUCIÓN"
    elif (33 <= valorIndiceCalor <= 40) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "PRECAUCIÓN\nEXTREMA"
    elif (41 <= valorIndiceCalor <= 51) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "PELIGRO"
    elif (52 <= valorIndiceCalor <= 92) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "PELIGRO\nEXTREMO"
    elif (93 <= valorIndiceCalor) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        textoIC= "MORTAL"
    else:
        textoIC="---"
    return textoIC

def colorIndiceCalor(valorIndiceCalor, valorTemperaturaF, valorHumedad): #Establece el color de la etiqueta en base al valor del índice de calor
    if (valorIndiceCalor <= 26) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#3CA934"
    elif (27 <= valorIndiceCalor <= 32) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#FDCD01"
    elif (33 <= valorIndiceCalor <= 40) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#F7A92B"
    elif (41 <= valorIndiceCalor <= 51) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#E54E1F"
    elif (52 <= valorIndiceCalor <= 92) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#9D44F4"
    elif (93 <= valorIndiceCalor) and (80 <= valorTemperaturaF <= 110) and (40 <= valorHumedad<= 100):
        colorIC= "#000000"
    else:
        colorIC="#FFFFFF"
    return colorIC
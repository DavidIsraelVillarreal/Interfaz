import requests
from bs4 import BeautifulSoup

temperatura = "" 
humedad = ""
elementoHumedad = []
iUV = ""
pm10 = ""
pm25 = ""

def obtenerNombreArchivo(now):
    #now = datetime.now()
    return "/home/xibernetiq/Documents/Tesis/Interfaz/ArchivosTexto/WebPage2/Dia_{}.txt".format(now.strftime("%Y-%m-%d")) # Poner  %Y-%m-%d

def obtenerDatosClima1(url, marcaTiempo):
    try:
        global temperatura
        global humedad
        global elementoHumedad
        global iUV

        response = requests.get(url) # Realiza una solicitud HTTP GET a la URL especificada
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser') # Analiza y convierte el contenido HTML de una respuesta web en un objeto BeautifulSoup.

        try:
            temperatura = soup.find('span', class_='c-tib-text degrees').text # Extraer el valor de la temperatura de la página web. Este sí
            if not temperatura:
                temperatura = "-1"
        except ValueError:
            temperatura = "-1"

        try:
            elementoHumedad = soup.find_all('p', text=lambda text: text and "%" in text) # Encuentra el elemento <p> que contiene el símbolo "%"
            if elementoHumedad:
                humedad = elementoHumedad[1].text.strip()  # Segundo elemento. Este sí
                if not humedad:
                    humedad = "-1"
            else:
                humedad = "-1"
        except ValueError:
            humedad = "-1"
    
        try:
            iUV = soup.find('p', class_='-cta-text').text #Este sí
            if not iUV:
                iUV = "-1"
        except ValueError:
            iUV = "-1"

        return f"{marcaTiempo} Humedad= {humedad} Temperatura= {temperatura} IUV= {iUV} " #Está en % la humedad y en °C la temperatura.
    except requests.exceptions.RequestException as e:
        if not temperatura:
            temperatura = "-1"
        
        if not elementoHumedad:
            humedad = "-1"

        if not humedad:
            humedad = "-1"

        if not iUV:
            iUV = "-1"

        return f"{marcaTiempo} Humedad= {humedad} Temperatura= {temperatura} IUV= {iUV} " #Está en % la humedad y en °C la temperatura."
    except AttributeError:
        if not temperatura:
            temperatura = "-1"
        
        if not elementoHumedad:
            humedad = "-1"

        if not humedad:
            humedad = "-1"

        if not iUV:
            iUV = "-1"
        return f"{marcaTiempo} Humedad= {humedad} Temperatura= {temperatura} IUV= {iUV} " #Está en % la humedad y en °C la temperatura."


def obtenerDatosClima2(url):
    try:
        global pm10
        global pm25

        response = requests.get(url) # Realiza una solicitud HTTP GET a la URL especificada
        response.raise_for_status() # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser') # Analiza y convierte el contenido HTML de una respuesta web en un objeto BeautifulSoup.

        # Encuentra el elemento <div> con la clase LBnfJ9
        elementoPadrePM = soup.find('div', class_='LBnfJ9')

        if elementoPadrePM:
            # Encuentra todos los elementos <div> con la clase mAEOfF dentro del elemento padre
            segundaClase = elementoPadrePM.find_all('div', class_='mAEOfF')

            if len(segundaClase) >= 2:  # Verifica que haya al menos dos elementos mAEOfF
                # Accede al segundo elemento mAEOfF para PM2.5
                segundaClasePM25 = segundaClase[1]

                # Encuentra el elemento <div> con la clase z3hdyp dentro de mAEOfF
                terceraClasePM25 = segundaClasePM25.find('div', class_='z3hdyp')
            
                if terceraClasePM25:
                    # Encuentra el elemento <span> con el texto "PM2.5" dentro de z3hdyp
                    valorPM25Label = terceraClasePM25.find('span', text="PM25")

                    if valorPM25Label:
                        elementoPM25Valor = valorPM25Label.find_parent().find_next_sibling('div', class_='kJXXQe')

                        if elementoPM25Valor:
                            pm25 = elementoPM25Valor.text.strip()
                        else:
                            pm25="-1"
                    else:
                        pm25="-1"
                else:
                    pm25="-1"
                
                segundaClasePM10 = segundaClase[0]
                # Encuentra el elemento <div> con la clase z3hdyp dentro de mAEOfF
                terceraClasePM10 = segundaClasePM10.find('div', class_='z3hdyp')
            
                if terceraClasePM10:
                    # Encuentra el elemento <span> con el texto "PM2.5" dentro de z3hdyp
                    valorPM10Label = terceraClasePM10.find('span', text="PM10")

                    if valorPM10Label:
                        elementoPM10Valor = valorPM10Label.find_parent().find_next_sibling('div', class_='kJXXQe')

                        if elementoPM10Valor:
                            pm10 = elementoPM10Valor.text.strip()
                        else:
                            pm10 = "-1"
                    else:
                        pm10="-1"
                else:
                    pm10="-1"
            else:
                pm10="-1"
                pm25="-1"
        else:
            pm10="-1"
            pm25="-1"

        return f"PM10= {pm10} PM2,5= {pm25}\n"

    except requests.exceptions.RequestException as e1:
        if not pm10:
            pm10 = "-1"
        
        if not pm25:
            pm25 = "-1"

        return f"PM10(µg/m³)= {pm10} PM2,5(µg/m³)= {pm25}\n"
    except AttributeError:
        if not pm10:
            pm10 = "-1"
        
        if not pm25:
            pm25 = "-1"

        return f"PM10(µg/m³)= {pm10} PM2,5(µg/m³)= {pm25}\n"

def guardarDatos(datos, now):
    nombreArchivo = obtenerNombreArchivo(now)
    with open(nombreArchivo, 'a') as archivo:
        archivo.write(datos)

def main(now, marcaTiempo):
    url1 = "https://www.clima.com/ecuador/imbabura/ibarra"
    url2 = "https://weather.tomorrow.io/es/EC/I/Ibarra/031513/health/"
    datosClima1 = obtenerDatosClima1(url1, marcaTiempo)
    datosClima2 = obtenerDatosClima2(url2)
    guardarDatos(datosClima1, now)
    guardarDatos(datosClima2, now)



import requests
from bs4 import BeautifulSoup

temperatura = "" 
humedad = ""
iUV = ""
pm10 = ""
pm25 = ""

def obtenerNombreArchivo(now):
    return "/home/xibernetiq/Documents/Tesis/Interfaz/ArchivosTexto/WebPage/Dia_{}.txt".format(now.strftime("%Y-%m-%d")) # Poner  %Y-%m-%d

def obtenerDatosClima1(url, marcaTiempo):
    try:
        global temperatura
        global humedad
        global iUV
        response = requests.get(url) # Realiza una solicitud HTTP GET a la URL especificada
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser') # Analiza y convierte el contenido HTML de una respuesta web en un objeto BeautifulSoup.

        try:
            # Encuentra los elementos HTML que contienen la información del clima
            temperatura = soup.find('span', class_='CurrentConditions--tempValue--zUBSz').text # Extraer el valor de la temperatura de la página web
            if not temperatura:
                temperatura = "-1"
        except ValueError:
            temperatura = "-1"
        
        try:
            humedad = soup.find('span', {'data-testid': 'PercentageValue'}).text
            if not humedad:
                humedad = "-1"
        except ValueError:
            humedad = "-1"

        try:
            iUV = soup.find('span', {'data-testid': 'UVIndexValue'}).text
            if not iUV:
                iUV = "-1"
        except ValueError:
            iUV="-1"

        return f"{marcaTiempo} Humedad= {humedad} Temperatura= {temperatura} IUV= {iUV} " #Está en % la humedad y en °C la temperatura.
    except requests.exceptions.RequestException as e:
        if not temperatura:
            temperatura = "-1"

        if not humedad:
            # Encuentra el elemento hermano siguiente que contiene el valor
            humedad = "-1"

        if not iUV:
            # Encuentra el elemento hermano siguiente que contiene el valor
            iUV = "-1"

        return f"{marcaTiempo} Humedad= {humedad} Temperatura= {temperatura} IUV= {iUV} " #Está en % la humedad y en °C la temperatura."
    except AttributeError:
        if not temperatura:
            temperatura = "-1"

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
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser') # Analiza y convierte el contenido HTML de una respuesta web en un objeto BeautifulSoup.

        # Encuentra los elementos HTML que contienen la información del clima
        valoresCalidadAire = soup.find_all('span', {'data-testid': 'AirQualityMeasurement'})
        if valoresCalidadAire:
            pm25 = valoresCalidadAire[0].text.strip()  # Primer elemento
            if not pm25:
                pm25 ="-1"
            pm10 = valoresCalidadAire[4].text.strip()  # Segundo elemento
            if not pm10:
                pm10 ="-1"
        else:
            pm10="-1"
            pm25="-1"

        return f"PM10(µg/m³)= {pm10} PM2,5(µg/m³)= {pm25}\n"

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
    url1 = "https://weather.com/es-HN/tiempo/hoy/l/aa34a634f683251bd3b60e3a4cb03f6ae0b202a5826fd61ef931f3b294323090"
    url2= "https://weather.com/es-HN/forecast/air-quality/l/aa34a634f683251bd3b60e3a4cb03f6ae0b202a5826fd61ef931f3b294323090"
    datosClima1 = obtenerDatosClima1(url1, marcaTiempo)
    datosClima2 = obtenerDatosClima2(url2)
    guardarDatos(datosClima1, now)
    guardarDatos(datosClima2, now)


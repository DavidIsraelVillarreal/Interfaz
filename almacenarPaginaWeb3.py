import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore


humedad = ""

def obtenerNombreArchivo(now):
    #now = datetime.now()
    return "/home/xibernetiq/Documents/Tesis/Interfaz/ArchivosTexto/WebPage3/Dia_{}.txt".format(now.strftime("%Y-%m-%d")) # Poner  %Y-%m-%d

def obtenerDatosClima1(url, marcaTiempo):
    try:
        global humedad

        response = requests.get(url) # Realiza una solicitud HTTP GET a la URL especificada
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        soup = BeautifulSoup(response.content, 'html.parser') # Analiza y convierte el contenido HTML de una respuesta web en un objeto BeautifulSoup.

        humedad = soup.find('div', id='CurrentDetailLineHumidityValue').text

        return f"{marcaTiempo} Humedad(%)= {humedad}\n" #Está en % la humedad.
    
    except requests.exceptions.RequestException as e:
        return f"{marcaTiempo} Humedad(%)= -1\n"
    except AttributeError:
        return f"{marcaTiempo} Humedad(%)= -1\n"
    
def guardarDatos(datos, now):
    nombreArchivo = obtenerNombreArchivo(now)
    with open(nombreArchivo, 'a') as archivo:
        archivo.write(datos)

def main(now, marcaTiempo):
    url = "https://www.msn.com/es-xl/el-tiempo/pronostico/in-Ibarra,Imbabura?loc=eyJsIjoiSWJhcnJhIiwiciI6IkltYmFidXJhIiwicjIiOiJJYmFycmEiLCJjIjoiRWN1YWRvciIsImkiOiJFQyIsInQiOjEwMiwiZyI6ImVzLXhsIiwieCI6Ii03OC4xMiIsInkiOiIwLjM1MiJ9&weadegreetype=C"
    datosClima1 = obtenerDatosClima1(url, marcaTiempo)
    guardarDatos(datosClima1, now)


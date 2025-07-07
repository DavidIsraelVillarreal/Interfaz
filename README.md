# Interfaz
<p>
**¿Qué ejecuta el programa?**
Proyecto de una interfaz gráfica en python usando la librería tkinter, para la lectura de los sensores DHT22, ML8511 y SDS011 a través de una Raspberry Pi 3B.

También se detecta el nivel de voltaje de la batería y su temperatura Al sobrepasar esos umbrales (11 V y 45 °C) el programa finaliza automaticamente, apagando también la Raspberry Pi 3B.
</p>
**Consideracioes:      **
- Al descargar los archivos es necesario crear la carpeta ArchivosTexto en la raiz del programa, la cual debe contener en su interior las carpetas: PruebaFuncionamiento2, Totem, VoltajeBateria, WebPage, WebPage2 y WebPage3
- La contraseña para finalizar el programa se encuentra en el módulo creacionInterfazPrincipal.py, donde se muestra que es 12345.
- El programa envía los datos recopilados a Firestore dentro de la franja horaria de las 10h00 hasta las 14h00, por lo que el usuario debe crear una clave .JSON y colocarla en la raiz para poder ejecuar correctamente el programa

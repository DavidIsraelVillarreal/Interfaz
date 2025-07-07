# Interfaz
**¿Qué ejecuta el programa?**
Proyecto de una interfaz gráfica en Python usando la librería tkinter para la lectura de los sensores DHT22, ML8511 y SDS011 a través de una Raspberry Pi 3B.

También se detecta el nivel de voltaje de la batería y su temperatura. Al sobrepasar esos umbrales (11 V y 45 °C) el programa finaliza automaticamente, apagando también la Raspberry Pi 3B.

**Consideraciones:**
- Al descargar los archivos es necesario crear la carpeta ArchivosTexto en la raiz del programa, la cual debe contener en su interior las carpetas: PruebaFuncionamiento2, VoltajeBateria, WebPage, WebPage2 y WebPage3.
- La contraseña para finalizar el programa se encuentra en el módulo creacionInterfazPrincipal.py, donde se muestra que es 12345.
- El programa envía los datos recopilados a Firestore dentro de la franja horaria de las 10h00 hasta las 14h00, por lo que el usuario debe crear una clave .JSON y colocarla en la raiz para poder ejecuar correctamente el programa.
- Los programas que se deben ejecutar son: programaPrincipal.py, pruebaFuncionamiento1.py, pruebaFuncionamiento2.py o pruebaFuncionamiento3.py, dependiendo de lo que el usuario desee.
- El archivo programaPrincipal.py muestra los valores adquiridos por los sensores en la interfaz, mientras envía los datos a Firestore.
- El archivo pruebaFuncionamiento1.py permite medir la latencia en base a la métrica RTT.
- El archivo pruebaFuncionamiento2.py permite guardar los valores adquiridos por los sensores en un archivo .TEXT en la carpeta PruebaFuncionamiento2. También almacena los datos de varias páginas web en las carpetas: WebPage, WebPage2 y WebPage3.
- El archivo pruebaFuncionamiento1.py permite medir el voltaje y temperatura de la batería para almacenarlo en un archivo .TEXT en la carpeta VoltajeBateria.
- Los datos subidos a Firestore son usados posteriormente por una PWA. El desarrollo de la PWA se puede ver en el siguiente enlace: https://github.com/DavidIsraelVillarreal/Interfaz-PWA.git

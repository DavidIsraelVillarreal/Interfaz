from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica
import time
import creacionVentanaRecomendacionesUV
import creacionVentanaRecomendacionesCalidadAire
import creacionVentanaRecomendacionHI

class interfazConContraseña:
    def __init__(self, raiz, varCompartidas):
        print("Se está creando la interfaz")
        #----------------------------------------  CONFIGURAR RAIZ Y FRAME ---------------------------------------- 
        self.raiz = raiz
        self.raiz.protocol("WM_DELETE_WINDOW", self.cerrarConContrasena) #Define el comportamiento del botón para que llame a la funición "cerrarConContrasena" cuando se lo presione.
        self.raiz.title("TÓTEM MEDIDOR DE CONDICIONES AMBIENTALES") #Pone ese título a la raiz
        self.raiz.grab_set()  # Libera el foco
        self.raiz.resizable(False, False) #Deshabilita la opción de modificar el tamaño de la pantalla de forma manual.
        self.raiz.geometry("1280x800") #Configura el tamaño de la raiz
        self.raiz.config(bg="#808080") #Pone el color del fondo de la raiz
        self.miFrame = Frame(self.raiz, bg="black", width=1270, height= 790)
        self.miFrame.pack(fill="y", expand="True")
        #---------------------------------------- CREACIÓN DE WIDGETS PARA INTERFAZ ---------------------------------------- 
        #-------------------- Bloque 1 --------------------
        titulo1 = Label(self.miFrame, text="RADIACIÓN UV", font=("Asap SemiBold", 38, "bold"), fg="#B1CEF9", bg="black")
        titulo1.place(x=195, y=60)
        self.dato1 = Label(self.miFrame, text="NIVEL: " + "---" + "\n---", font=("Asap SemiBold", 38, "bold"), fg="black", bg="#8ED973", width=10)
        self.dato1.place(x=145, y=150)
        self.imagen1=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/iconoMalaLectura.png")
        Label(self.miFrame, image=self.imagen1, bg="black").place(x=520, y=128)

        #-------------------- Bloque 2 --------------------
        self.imagen2=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura3.png")
        Label(self.miFrame, image=self.imagen2, bg="black").place(x=428, y=370)
        titulo2 = Label(self.miFrame, text="CALIDAD DEL AIRE", font=("Asap SemiBold", 38, "bold"), fg="#B1CEF9", bg="black")
        titulo2.place(x=10, y=315)
        titulo3 = Label(self.miFrame, text="(PM2.5 Y PM10)", font=("Asap SemiBold", 35, "bold"), fg="#B1CEF9", bg="black")
        titulo3.place(x=10, y=385)
        self.dato2 = Label(self.miFrame, text="---", font=("Asap SemiBold", 38, "bold"), fg="black", bg="#EB4141", width=11)
        self.dato2.place(x=20, y=475)

        #-------------------- Bloque 3 --------------------
        self.imagen3=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/Humedad/iconoHumedad0.png")
        Label(self.miFrame, image=self.imagen3, bg="black").place(x=10, y=660)
        titulo4 = Label(self.miFrame, text="HUMEDAD RELATIVA", font=("Asap SemiBold", 38, "bold"), fg="#B1CEF9", bg="black")
        titulo4.place(x=95, y=585)

        #-------------------- Bloque 4 --------------------
        titulo5 = Label(self.miFrame, text="TEMPERATURA", font=("Asap SemiBold", 38, "bold"), fg="#B1CEF9", bg="black")
        titulo5.place(x=830, y=60)
        self.dato3 = Label(self.miFrame, text="---"+" °C", font=("Asap SemiBold", 38, "bold"), fg="black", bg="#EB4141", width=7)
        self.dato3.place(x=924, y=315)
        self.dato4 = Label(self.miFrame, text="---"+" °F", font=("Asap SemiBold", 38, "bold"), fg="black", bg="#EB4141", width=7) 
        self.dato4.place(x=924, y=415)
        self.imagen4=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/Temperatura/iconoMalaLecturaTemp.png")
        Label(self.miFrame, image=self.imagen4, bg="black").place(x=981, y=148)

        titulo6 = Label(self.miFrame, text="ÍNDICE\nDE CALOR", font=("Asap SemiBold", 38, "bold"), fg="#B1CEF9", bg="black")
        titulo6.place(x=895, y=520)
        self.dato5 = Label(self.miFrame, text="---\n ", font=("Asap SemiBold", 38, "bold"), fg="black", bg="#D86ECC", width=11)
        self.dato5.place(x=852, y=660)

        #-------------------- Bordes --------------------
        bordeHorizontal1=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/borde1_4.png")
        Label(self.miFrame, image=bordeHorizontal1, bg="#808080").place(x=-1, y=300)

        bordeHorizontal2=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/borde1_4.png")
        Label(self.miFrame, image=bordeHorizontal2, bg="#808080").place(x=-1, y=570)

        bordeVertical1=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/borde2_1.png")
        Label(self.miFrame, image=bordeVertical1, bg="#808080").place(x=812, y=-1)

        bordeExternoSuperior = PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/titulo.png")
        Label(self.miFrame, image=bordeExternoSuperior, bg="#808080").place(x=0, y=0)
        
        bordeExternoInferior = PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/bordeExterno.png")
        Label(self.miFrame, image=bordeExternoInferior, bg="#808080").place(x=0, y=795)

        bordeTitulo = PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/titulo1.png")
        Label(self.miFrame, image=bordeTitulo, bg="#B2B2B2").place(x=0, y=5)

        #-------------------- Botones para recomendaciones --------------------
        self.imagenBotonRecomendacion = PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/recomendacionBoton.png")
        botonRecomendacionUV = Button(self.miFrame, image=self.imagenBotonRecomendacion, command = lambda:self.abrirVentanaUV(varCompartidas), bg="black",highlightbackground="black",borderwidth=0, activebackground="black" )
        botonRecomendacionUV.place(x=730, y=60)

        botonRecomendacionCalidadAire = Button(self.miFrame, image=self.imagenBotonRecomendacion, command =  lambda:self.abrirVentanaCalidadAire(varCompartidas), bg="black",highlightbackground="black",borderwidth=0, activebackground="black" )
        botonRecomendacionCalidadAire.place(x=730, y=320)

        botonRecomendacionHI = Button(self.miFrame, image=self.imagenBotonRecomendacion, command = lambda:self.abrirVentanaRecomendacionHI(varCompartidas), bg="black",highlightbackground="black",borderwidth=0, activebackground="black" )
        botonRecomendacionHI.place(x=1190, y=525)

        #--------------------  Hora --------------------
        self.etiquetaHora = Label(self.miFrame, text="00:00", font=("Asap SemiBold", 20), fg="black", bg="#B2B2B2")
        self.etiquetaHora.place(x=1080, y=9)
        self.actualizarHora()
        #-------------------- Botón para salir ----------------
        botonSalir = Button(self.miFrame, text= "SALIR", font=("bold"), command = lambda:self.cerrarConContrasena(varCompartidas), bg="#FFFFFF",borderwidth=1)
        botonSalir.place(x=1190, y=10)

        #-------------------- Botón para salir ----------------
        tituloGeneral = Label(self.miFrame, text="TÓTEM MEDIDOR DE CONDICIONES AMBIENTALES", font=("Asap SemiBold", 20, "bold"), fg="#FFFFFF", bg="#B2B2B2")
        tituloGeneral.place(x=263, y=9)

    def abrirVentanaUV(self, varCompartidas):
        creacionVentanaRecomendacionesUV.ventanaRecomendacionUV(self.raiz, varCompartidas)

    def abrirVentanaCalidadAire(self, varCompartidas):
        creacionVentanaRecomendacionesCalidadAire.ventanaRecomendacionCalidadAire(self.raiz, varCompartidas)

    def abrirVentanaRecomendacionHI(self, varCompartidas):
        creacionVentanaRecomendacionHI.ventanaRecomendacionHI(self.raiz, varCompartidas)

    def cerrarConContrasena(self, varCompartidas):
        # Crear ventana para la contraseña
        self.raiz.grab_release()  # Libera el foco
        self.ventanaContrasena = Toplevel(self.raiz) #Crear una ventana de nivel superior.
        self.fondo=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/fondoContrasena.png")
        Label(self.ventanaContrasena, image=self.fondo).place(x=-1, y=-1)
        self.ventanaContrasena.config(bg="")
        self.ventanaContrasena.protocol("WM_DELETE_WINDOW", self.cerrarVentanaEmergenteContrasena)  # Asocia la función al evento de cierre
        self.ventanaContrasena.title("Contraseña")
        self.ventanaContrasena.attributes('-fullscreen', True)
        self.ventanaContrasena.lift()  # Eleva la ventana emergente
        self.raiz.attributes('-fullscreen', False)
        
        self.imagenTituloContrasena=PhotoImage(file="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenTituloContrasenaCF.png")
        self.tituloContrasena = Label(self.ventanaContrasena, image=self.imagenTituloContrasena, borderwidth=0)
        self.tituloContrasena.image = self.imagenTituloContrasena
        self.tituloContrasena.place(x=350, y=115)
        self.ventanaContrasena.update()
             
        # Campo de entrada para la contraseña
        self.contrasena = StringVar() #Se establece que el atributo contrasena tenga la capacidad de "enlazarse" con los widgets.
        self.entradaContrasena = Entry(self.ventanaContrasena, textvariable=self.contrasena, show="*") #Crea un widget que permite al usuario ingresar texto, que se va a ver oculto por *
        self.entradaContrasena.place(x=558, y= 210)

        # Creación de teclado para introducir contraseña
        boton1 = Button(self.ventanaContrasena, text="1", command=lambda num=1: self.agregarNumero(num)) #Crea un botón, y lo asigna a la variable boton1. Se utiliza una función anónima para crear una función que toma un argumento num y llama al método self.agregarNumero(num).
        boton1.place(x=558, y= 260)
        boton2 = Button(self.ventanaContrasena, text="2", command=lambda num=2: self.agregarNumero(num)) 
        boton2.place(x=623, y= 260)
        boton3 = Button(self.ventanaContrasena, text="3", command=lambda num=3: self.agregarNumero(num)) 
        boton3.place(x=688, y= 260)
        boton4 = Button(self.ventanaContrasena, text="4", command=lambda num=4: self.agregarNumero(num)) 
        boton4.place(x=558, y= 311)
        boton5 = Button(self.ventanaContrasena, text="5", command=lambda num=5: self.agregarNumero(num))
        boton5.place(x=623, y= 311)
        boton6 = Button(self.ventanaContrasena, text="6", command=lambda num=6: self.agregarNumero(num)) 
        boton6.place(x=688, y= 311)
        boton7 = Button(self.ventanaContrasena, text="7", command=lambda num=7: self.agregarNumero(num)) 
        boton7.place(x=558, y= 362)
        boton8 = Button(self.ventanaContrasena, text="8", command=lambda num=8: self.agregarNumero(num)) 
        boton8.place(x=623, y= 362)
        boton9 = Button(self.ventanaContrasena, text="9", command=lambda num=9: self.agregarNumero(num))
        boton9.place(x=688, y= 362)

        # Botón de borrar
        botonBorrar = Button(self.ventanaContrasena, text=" Borrar ", command=self.borrarUltimoCaracter)
        botonBorrar.place(x=478, y= 427)

        # Botón de aceptar
        botonAceptar = Button(self.ventanaContrasena, text="Aceptar", command= lambda: self.verificarContrasena(varCompartidas))
        botonAceptar.place(x=603, y= 427)

        # Botón de regresar
        botonRegresar = Button(self.ventanaContrasena, text="Regresar", command=self.cerrarVentanaEmergenteContrasena)
        botonRegresar.place(x=728, y= 427)
        
        self.ventanaContrasena.after(20000, lambda: self.cerrarVentanaEmergenteContrasena()) #Cerrar ventana emergente dentro de 20 segundos para regresar a la interfaz principal

    def cerrarVentanaEmergenteContrasena(self):
        self.contrasena.set("")  # Limpiar el campo de entrada
        self.ventanaContrasena.destroy() # Destruye la ventana emergente
        self.raiz.grab_set()  # Captura el foco
        self.raiz.attributes('-fullscreen', True) # La interfaz ocupa todo el espacio de la pantalla

    def agregarNumero(self, num): #Agrega los números respectivos al atributo contrasena.
        self.contrasena.set(self.contrasena.get() + str(num))

    def borrarUltimoCaracter(self): #Borra los números respectivos al atributo contrasena.
        self.contrasena.set(self.contrasena.get()[:-1])

    def verificarContrasena(self, varCompartidas):
        contrasenaCorrecta = "12345" #Contraseña con la cual se sale de programa. Aquí se puede configurar una nueva contraseña si se desea.
        contrasenaIngresada = self.contrasena.get()

        if contrasenaIngresada == contrasenaCorrecta:
            varCompartidas["interfazActiva"] = False
            self.raiz.destroy() #Cierra la ventana en caso de que la contraseña sea la correcta.
            varCompartidas["indicadorParada"] = True
        else:
            self.errorContrasena = Label(self.ventanaContrasena, text="CONTRASEÑA INCORRECTA\nINTENTE NUEVAMENTE", font=("Asap SemiBold", 20, "bold"), fg="black", bg="#FFFFFF", highlightbackground="black",highlightthickness=2)
            self.errorContrasena.place(x=433, y=482)
            self.contrasena.set("")  # Limpiar el campo de entrada

    def cerrarPorVoltaje(self):
        self.raiz.after(0, lambda: self.raiz.destroy())

    def actualizarHora(self):
        horaActual = time.strftime("%H:%M")
        self.etiquetaHora.config(text=horaActual)
        self.etiquetaHora.lift()  # Eleva la ventana emergente
        self.raiz.after(1000, lambda: self.actualizarHora())  # Actualizar cada segundo la hora que se muestra.   
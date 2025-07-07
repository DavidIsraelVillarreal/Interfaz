from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica
import time

class ventanaRecomendacionUV(Toplevel):
    def __init__(self, raiz, varCompartidas):
        super().__init__(raiz)
        self.attributes('-fullscreen',True)
        self.lift()
        self.raiz = raiz  # Guarda la referencia a la ventana principal
        self.raiz.grab_release()
        self.title("Recomendaciones por Índice UV")
        self.miFrameRecomendacionUV = Frame(self, bg="black", width=1280, height=800)
        self.miFrameRecomendacionUV.pack()
        self.raiz.attributes('-fullscreen', False)
        
        self.botonSalirRecUV = Button(self, text= "REGRESAR", font=("bold"), command = lambda:self.cerrarVentanaRecUV(), bg="#FFFFFF",borderwidth=1)
        self.botonSalirRecUV.place(x=1145, y=20)

        tituloRecomendacion = Label(self.miFrameRecomendacionUV, text="RECOMENDACIONES", font=("Asap SemiBold", 38, "bold"), fg="#F2AA84", bg="black")
        tituloRecomendacion.place(x=351, y=50)
        if (0<=round(varCompartidas["uvIntensity"])<=2):
            textoRecomendacion1 = "NO NECESITA PROTECCIÓN"
            textoRecomendacion2 = " "
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion1.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black")
            self.Recomendacion1.place(x=292, y=195)
            self.Recomendacion2 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=225)
            self.imagenRecomendacionUV1=PhotoImage(file=imagenMostrarRecUV1)
            self.imagenRecomendacionUV2=PhotoImage(file=imagenMostrarRecUV2)
            self.imagenRecomendacionUV3=PhotoImage(file=imagenMostrarRecUV3)
            self.etiquetaImagenRecUV1 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV1, bg="black")
            self.etiquetaImagenRecUV2 =Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV2, bg="black")
            self.etiquetaImagenRecUV3 =Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV3, bg="black")
            self.etiquetaImagenRecUV1.place(x=556, y=390)
            self.etiquetaImagenRecUV2.place(x=10, y=600)
            self.etiquetaImagenRecUV3.place(x=10, y=600)
        elif (3<=round(varCompartidas["uvIntensity"])<=7): 
            textoRecomendacion1 = "NECESITA PROTECCIÓN"
            textoRecomendacion2 = "- Manténgase en la sombra\n- Use camisa\n- Use crema de protección solar\n- Use sombrero"
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion2.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion3.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black")
            self.Recomendacion1.place(x=40, y=155)
            self.Recomendacion2 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=245)
            self.imagenRecomendacionUV1=PhotoImage(file=imagenMostrarRecUV1)
            self.imagenRecomendacionUV2=PhotoImage(file=imagenMostrarRecUV2)
            self.imagenRecomendacionUV3=PhotoImage(file=imagenMostrarRecUV3)
            self.etiquetaImagenRecUV1 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV1, bg="black")
            self.etiquetaImagenRecUV2 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV2, bg="black")
            self.etiquetaImagenRecUV3 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV3, bg="black")
            self.etiquetaImagenRecUV1.place(x=10, y=600)
            self.etiquetaImagenRecUV2.place(x=480, y=520)
            self.etiquetaImagenRecUV3.place(x=650, y=520)
        elif (round(varCompartidas["uvIntensity"])>=8): 
            textoRecomendacion1 = "NECESITA PROTECCIÓN EXTRA"
            textoRecomendacion2 = "- Evite salir de la casa\n- Manténgase en la sombra\n- Imprescindible el uso de camisa\n- Imprescindible el uso de crema de protección solar\n- Imprescindible el uso de sombrero"
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion2.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion3.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion4.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black")
            self.Recomendacion1.place(x=40, y=155)
            self.Recomendacion2 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=245)
            self.imagenRecomendacionUV1=PhotoImage(file=imagenMostrarRecUV1)
            self.imagenRecomendacionUV2=PhotoImage(file=imagenMostrarRecUV2)
            self.imagenRecomendacionUV3=PhotoImage(file=imagenMostrarRecUV3)
            self.etiquetaImagenRecUV1 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV1, bg="black")
            self.etiquetaImagenRecUV2 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV2, bg="black")        
            self.etiquetaImagenRecUV3 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV3, bg="black")        
            self.etiquetaImagenRecUV1.place(x=379, y=545)
            self.etiquetaImagenRecUV2.place(x=567, y=545)
            self.etiquetaImagenRecUV3.place(x=749, y=545)
        else:
            textoRecomendacion1 = "HUBO UN ERROR EN LA LECTURA"
            textoRecomendacion2 = " "
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black")
            self.Recomendacion1.place(x=214, y=195)
            self.Recomendacion2 = Label(self.miFrameRecomendacionUV, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=225)
            self.imagenRecomendacionUV1=PhotoImage(file=imagenMostrarRecUV1)
            self.imagenRecomendacionUV2=PhotoImage(file=imagenMostrarRecUV2)
            self.imagenRecomendacionUV3=PhotoImage(file=imagenMostrarRecUV3)
            self.etiquetaImagenRecUV1 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV1, bg="black")
            self.etiquetaImagenRecUV2 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV2, bg="black")
            self.etiquetaImagenRecUV3 = Label(self.miFrameRecomendacionUV, image=self.imagenRecomendacionUV3, bg="black")
            self.etiquetaImagenRecUV1.place(x=487, y=390)
            self.etiquetaImagenRecUV2.place(x=10, y=600)
            self.etiquetaImagenRecUV3.place(x=10, y=600)
        
        self.tiempoApagarInicioVentanaEmergente = time.time()
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesUV(varCompartidas))

    def actualizarVentanaRecomendacionesUV (self, varCompartidas):
        if (0<=round(varCompartidas["uvIntensity"])<=2):
            textoRecomendacion1 = "NO NECESITA PROTECCIÓN"
            textoRecomendacion2 = " "
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion1.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1=556
            y1=390
            x2=10
            y2=600
            x3=10
            y3=600
            self.Recomendacion1.place(x=292, y=195)
            self.Recomendacion2.place(x=40, y=225)
            
        elif (3<=round(varCompartidas["uvIntensity"])<=7):
            textoRecomendacion1 = "NECESITA PROTECCIÓN"
            textoRecomendacion2 = "- Manténgase en la sombra\n- Use camisa\n- Use crema de protección solar\n- Use sombrero"
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion2.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion3.png"
            x1=10
            y1=600
            x2=480
            y2=520
            x3=650
            y3=520
            self.Recomendacion1.place(x=40, y=155)
            self.Recomendacion2.place(x=40, y=245)
        elif (round(varCompartidas["uvIntensity"])>=8):
            textoRecomendacion1 = "NECESITA PROTECCIÓN EXTRA"
            textoRecomendacion2 = "- Evite salir de la casa\n- Manténgase en la sombra\n- Imprescindible el uso de camisa\n- Imprescindible el uso de crema de protección solar\n- Imprescindible el uso de sombrero"
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion2.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion3.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/IUV/recomendacionesUV/recomendacion4.png"
            x1=379
            y1=545
            x2=567
            y2=545
            x3=749
            y3=545
            self.Recomendacion1.place(x=40, y=155)
            self.Recomendacion2.place(x=40, y=245)
        else:
            textoRecomendacion1 = "HUBO UN ERROR EN LA LECTURA"
            textoRecomendacion2 = " "
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1=487
            y1=390
            x2=10
            y2=600
            x3=10
            y3=600
            self.Recomendacion1.place(x=214, y=195)
            self.Recomendacion2.place(x=40, y=225)
        
        self.Recomendacion1.config(text=textoRecomendacion1)
        self.Recomendacion2.config(text=textoRecomendacion2)
        self.imagenRecomendacionUV1.config(file=imagenMostrarRecUV1)
        self.imagenRecomendacionUV2.config(file=imagenMostrarRecUV2)
        self.imagenRecomendacionUV3.config(file=imagenMostrarRecUV3)
        self.etiquetaImagenRecUV1.place(x=x1, y=y1)
        self.etiquetaImagenRecUV2.place(x=x2, y=y2)
        self.etiquetaImagenRecUV3.place(x=x3, y=y3)

        print("\nEstá abierta ventana recomendaciones UV\n")
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesUV(varCompartidas))
        
        self.tiempoApagarFinVentanaEmergente = time.time()
        if ((self.tiempoApagarFinVentanaEmergente - self.tiempoApagarInicioVentanaEmergente) >= 20):
            self.tiempoApagarFinVentanaEmergente=0
            self.tiempoApagarInicioVentanaEmergente=0
            self.cerrarVentanaRecUV()
            print("Se cerró la ventana Recomendación UV")

    def cerrarVentanaRecUV(self):
        self.tiempoApagarFinVentanaEmergente = 0
        self.tiempoApagarInicioVentanaEmergente=0
        self.after_cancel(self.afterID)  # Cancelar la ejecución de after
        self.raiz.grab_set()
        self.destroy()  # Cerrar la ventana
        self.raiz.attributes('-fullscreen', True)
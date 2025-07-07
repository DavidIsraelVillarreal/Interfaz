from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica
import time

class ventanaRecomendacionCalidadAire(Toplevel):
    def __init__(self, raiz, varCompartidas):
        super().__init__(raiz)
        self.attributes('-fullscreen', True)
        self.lift()
        self.raiz = raiz
        self.raiz.grab_release()
        self.title("Recomendaciones por Calidad del Aire")
        self.miFrameRecomendacionCA = Frame(self, bg="black", width=1280, height=800)
        self.miFrameRecomendacionCA.pack()
        self.raiz.attributes('-fullscreen', False)

        tituloRecomendacion = Label(self.miFrameRecomendacionCA, text="RECOMENDACIONES", font=("Asap SemiBold", 38, "bold"), fg="#F2AA84", bg="black")
        tituloRecomendacion.place(x=351, y=50)
        
        if (0<=round(varCompartidas["pm25"])<=25) or (0<=round(varCompartidas["pm10"])<=50): #Óptimo
            textoRecomendacion1 = "LA CALIDAD DEL AIRE ES ÓPTIMA"
            textoRecomendacion2 = "No es necesaria ninguna protección"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion1.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=210, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=268, y=295)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")
            self.etiquetaImagenRecCA3 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")
            self.etiquetaImagenRecCA5 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")
            self.etiquetaImagenRecCA1.place(x=522, y=440)
            self.etiquetaImagenRecCA2.place(x=10, y=600)
            self.etiquetaImagenRecCA3.place(x=10, y=600)
            self.etiquetaImagenRecCA4.place(x=10, y=600)
            self.etiquetaImagenRecCA5.place(x=10, y=600)

        elif (26<=round(varCompartidas["pm25"])<=50) or (51<=round(varCompartidas["pm10"])<=100): #Bueno
            textoRecomendacion1 = "LA CALIDAD DEL AIRE ESTÁ DENTRO DE LA\nNORMA ECUATORIANA DE CALIDAD DE AIRE"
            textoRecomendacion2 = "- No es necesaria ninguna protección"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion1.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 36), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=335)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")
            self.etiquetaImagenRecCA3 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")
            self.etiquetaImagenRecCA5 =Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")
            self.etiquetaImagenRecCA1.place(x=523, y=450)
            self.etiquetaImagenRecCA2.place(x=10, y=600)
            self.etiquetaImagenRecCA3.place(x=10, y=600)
            self.etiquetaImagenRecCA4.place(x=10, y=600)
            self.etiquetaImagenRecCA5.place(x=10, y=600)

        elif (51<=round(varCompartidas["pm25"])<=150) or (101<=round(varCompartidas["pm10"])<=250): #Precaución
            textoRecomendacion1 = "RIESGO PARA INDIVIDUOS EXTREMADAMENTE SENSIBLES\n(ENFERMOS CRÓNICOS Y CONVALECIENTES)"
            textoRecomendacion2 = "- Individuos extremadamente sensibles deben evitar el\n  ejercicio intenso\n- Individuos extremadamente sensibles usen mascarilla\n- Hidrátese continuamente (1.5 litros de agua al día)"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=300)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")        
            self.etiquetaImagenRecCA3 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")        
            self.etiquetaImagenRecCA5 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")          
            self.etiquetaImagenRecCA1.place(x=292, y=540)
            self.etiquetaImagenRecCA3.place(x=540, y=540)
            self.etiquetaImagenRecCA2.place(x=788, y=540)
            self.etiquetaImagenRecCA4.place(x=10, y=600)
            self.etiquetaImagenRecCA5.place(x=10, y=600)

        elif (151<=round(varCompartidas["pm25"])<=250) or (251<=round(varCompartidas["pm10"])<=400): #Alerta
            textoRecomendacion1 = "RIESGO PARA INDIVIDUOS SENSIBLES (ENFERMOS)"
            textoRecomendacion2 = "- Evite el ejercicio intenso\n- Individuos sensibles deben usar mascarilla\n- Hidrátese continuamente (1.5 litros de agua al día)"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=290)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")        
            self.etiquetaImagenRecCA3 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")     
            self.etiquetaImagenRecCA4 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")        
            self.etiquetaImagenRecCA5 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")        
            self.etiquetaImagenRecCA1.place(x=292, y=520)
            self.etiquetaImagenRecCA3.place(x=540, y=520)
            self.etiquetaImagenRecCA2.place(x=788, y=520)
            self.etiquetaImagenRecCA4.place(x=10, y=600)
            self.etiquetaImagenRecCA5.place(x=10, y=600)
        
        elif (251<=round(varCompartidas["pm25"])<=350) or (401<=round(varCompartidas["pm10"])<=500): #Alarma
            textoRecomendacion1 = "RIESGO PARA LA MAYORÍA DE LA POBLACIÓN Y PELIGROSO\nPARA INDIVIDUOS SENSIBLES (ENFERMOS)"
            textoRecomendacion2 = "- No realice ejercicio intenso\n- No realice actividades al aire libre\n- Hidrátese continuamente (1.5 litros de agua al día)\n- Evite el uso de lentes de contacto\n- Use mascarilla "
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion5.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion6.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=100+20+30-15+20+20-15)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=100+20+30+50+15+10+10+10+20+30+20+20-15-15-10-5)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")        
            self.etiquetaImagenRecCA3 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")        
            self.etiquetaImagenRecCA5 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")       
            self.etiquetaImagenRecCA1.place(x=40, y=570)
            self.etiquetaImagenRecCA4.place(x=292, y=570)
            self.etiquetaImagenRecCA2.place(x=540, y=570)
            self.etiquetaImagenRecCA3.place(x=1042, y=570)
            self.etiquetaImagenRecCA5.place(x=788, y=570)

        elif (350<round(varCompartidas["pm25"])) or (500<round(varCompartidas["pm10"])): #Emergencia
            textoRecomendacion1 = "RIESGO PARA TODA LA POBLACIÓN"
            textoRecomendacion2 = "- No realice ejercicio\n- No realice actividades al aire libre\n- Hidrátese continuamente (1.5 litros de agua al día)\n- Evite el uso de lentes de contacto\n- Use mascarilla "
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion5.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion6.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=100+20+30-15+20+20)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=100+20+30+50+15+10+50+25-30+20-20-5)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecCA1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecCA2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecCA3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")        
            self.etiquetaImagenRecCA3 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")        
            self.etiquetaImagenRecCA5 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black")       
            self.etiquetaImagenRecCA1.place(x=40, y=565)
            self.etiquetaImagenRecCA4.place(x=292, y=565)
            self.etiquetaImagenRecCA2.place(x=540, y=565)
            self.etiquetaImagenRecCA3.place(x=1042, y=565)
            self.etiquetaImagenRecCA5.place(x=788, y=565)
        else:
            textoRecomendacion1 = "HUBO UN ERROR EN LA LECTURA"
            textoRecomendacion2 = " "
            imagenMostrarRecUV1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecUV2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecUV3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black")
            self.Recomendacion1.place(x=214, y=195)
            self.Recomendacion2 = Label(self.miFrameRecomendacionCA, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=225)
            self.imagenRecomendacionCA1=PhotoImage(file=imagenMostrarRecUV1)
            self.imagenRecomendacionCA2=PhotoImage(file=imagenMostrarRecUV2)
            self.imagenRecomendacionCA3=PhotoImage(file=imagenMostrarRecUV3)
            self.imagenRecomendacionCA4=PhotoImage(file=imagenMostrarRecCA4)
            self.imagenRecomendacionCA5=PhotoImage(file=imagenMostrarRecCA5)
            self.etiquetaImagenRecCA1 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA1, bg="black")
            self.etiquetaImagenRecCA2 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA2, bg="black")
            self.etiquetaImagenRecCA3 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA3, bg="black")
            self.etiquetaImagenRecCA4 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA4, bg="black")        
            self.etiquetaImagenRecCA5 = Label(self.miFrameRecomendacionCA, image=self.imagenRecomendacionCA5, bg="black") 
            self.etiquetaImagenRecCA1.place(x=487, y=390)
            self.etiquetaImagenRecCA2.place(x=10, y=600)
            self.etiquetaImagenRecCA3.place(x=10, y=600)
            self.etiquetaImagenRecCA4.place(x=10, y=600)
            self.etiquetaImagenRecCA5.place(x=10, y=600)

        self.tiempoApagarInicioVentanaEmergente = time.time()
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesCA(varCompartidas))
        self.botonSalirRecCA = Button(self, text= "REGRESAR", font=("bold"), command = lambda:self.cerrarVentanaRecCA(), bg="#FFFFFF",borderwidth=1)
        self.botonSalirRecCA.place(x=1145, y=20)

    def actualizarVentanaRecomendacionesCA (self, varCompartidas):
        if (0<=round(varCompartidas["pm25"])<=25) or (0<=round(varCompartidas["pm10"])<=50): #Óptimo
            textoRecomendacion1 = "LA CALIDAD DEL AIRE ES ÓPTIMA"
            textoRecomendacion2 = "No es necesaria ninguna protección"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion1.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 522
            y1= 440
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 210
            y6= 175
            x7= 268
            y7= 295
            letra1= 38
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"

        elif (26<=round(varCompartidas["pm25"])<=50) or (51<=round(varCompartidas["pm10"])<=100): #Bueno
            textoRecomendacion1 = "LA CALIDAD DEL AIRE ESTÁ DENTRO DE LA\nNORMA ECUATORIANA DE CALIDAD DE AIRE"
            textoRecomendacion2 = "- No es necesaria ninguna protección"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion1.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 523
            y1= 450
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 40
            y6= 175
            x7= 40
            y7= 335
            letra1= 36
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"

        elif (51<=round(varCompartidas["pm25"])<=150) or (101<=round(varCompartidas["pm10"])<=250): #Precaución
            textoRecomendacion1 = "RIESGO PARA INDIVIDUOS EXTREMADAMENTE SENSIBLES\n(ENFERMOS CRÓNICOS Y CONVALECIENTES)"
            textoRecomendacion2 = "- Individuos extremadamente sensibles deben evitar el\n  ejercicio intenso\n- Individuos extremadamente sensibles usen mascarilla\n- Hidrátese continuamente (1.5 litros de agua al día)"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 292
            y1= 540
            x3= 540
            y3= 540
            x2= 788
            y2= 540
            x4= 10
            y4= 600
            x5= 10
            y5= 600     
            x6= 40
            y6= 175
            x7= 40
            y7= 300
            letra1= 31
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"
        elif (151<=round(varCompartidas["pm25"])<=250) or (251<=round(varCompartidas["pm10"])<=400): #Alerta
            textoRecomendacion1 = "RIESGO PARA INDIVIDUOS SENSIBLES (ENFERMOS)"
            textoRecomendacion2 = "- Evite el ejercicio intenso\n- Individuos sensibles deben usar mascarilla\n- Hidrátese continuamente (1.5 litros de agua al día)"
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 292
            y1= 520
            x3= 540
            y3= 520
            x2= 788
            y2= 520
            x4= 10
            y4= 600
            x5= 10
            y5= 600     
            x6= 40
            y6= 175
            x7= 40
            y7= 290
            letra1= 31
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"
        elif (251<=round(varCompartidas["pm25"])<=350) or (401<=round(varCompartidas["pm10"])<=500): #Alarma
            textoRecomendacion1 = "RIESGO PARA LA MAYORÍA DE LA POBLACIÓN Y PELIGROSO\nPARA INDIVIDUOS SENSIBLES (ENFERMOS)"
            textoRecomendacion2 = "- No realice ejercicio intenso\n- No realice actividades al aire libre\n- Hidrátese continuamente (1.5 litros de agua al día)\n- Evite el uso de lentes de contacto\n- Use mascarilla "
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion5.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion6.png"
            x1= 40
            y1= 570
            x3= 1042
            y3= 570
            x2= 540
            y2= 570
            x4= 292
            y4= 570
            x5= 788
            y5= 570
            x6= 40
            y6= 160
            x7= 40
            y7= 290
            letra1= 31
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"
        elif (350<round(varCompartidas["pm25"])) or (500<round(varCompartidas["pm10"])): #Emergencia
            textoRecomendacion1 = "RIESGO PARA TODA LA POBLACIÓN"
            textoRecomendacion2 = "- No realice ejercicio\n- No realice actividades al aire libre\n- Hidrátese continuamente (1.5 litros de agua al día)\n- Evite el uso de lentes de contacto\n- Use mascarilla "
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion3.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion4.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion5.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/recomendaciones/recomendacion6.png"
            x1= 40
            y1= 565
            x3= 1042
            y3= 565
            x2= 540
            y2= 565
            x4= 292
            y4= 565
            x5= 788
            y5= 565
            x6= 40
            y6= 175
            x7= 40
            y7= 265
            letra1= 31
            letra2= 31
            centrado1 = "left"
            centrado2 = "left"
        else:
            textoRecomendacion1 = "HUBO UN ERROR EN LA LECTURA"
            textoRecomendacion2 = " "
            imagenMostrarRecCA1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecCA2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecCA5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 487
            y1= 390
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 214
            y6= 195
            x7= 40
            y7= 225
            letra1= 38
            letra2= 31
            centrado1 = "center"
            centrado2 = "left"
            
        self.Recomendacion1.config(text=textoRecomendacion1, font=("Asap SemiBold", letra1), justify=centrado1)
        self.Recomendacion2.config(text=textoRecomendacion2, font=("Asap SemiBold", letra2), justify=centrado2)
        self.Recomendacion1.place(x=x6, y=y6)
        self.Recomendacion2.place(x=x7, y=y7)
        self.imagenRecomendacionCA1.config(file=imagenMostrarRecCA1)
        self.imagenRecomendacionCA2.config(file=imagenMostrarRecCA2)
        self.imagenRecomendacionCA3.config(file=imagenMostrarRecCA3)
        self.imagenRecomendacionCA4.config(file=imagenMostrarRecCA4)
        self.imagenRecomendacionCA5.config(file=imagenMostrarRecCA5)
        self.etiquetaImagenRecCA1.place(x=x1, y=y1)
        self.etiquetaImagenRecCA2.place(x=x2, y=y2)
        self.etiquetaImagenRecCA3.place(x=x3, y=y3)
        self.etiquetaImagenRecCA4.place(x=x4, y=y4)
        self.etiquetaImagenRecCA5.place(x=x5, y=y5)
    
        print("\nEstá abierta ventana recomendaciones Calidad del Aire\n")
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesCA(varCompartidas))
        self.tiempoApagarFinVentanaEmergente = time.time()
        if ((self.tiempoApagarFinVentanaEmergente - self.tiempoApagarInicioVentanaEmergente) >= 20):
            self.tiempoApagarFinVentanaEmergente=0
            self.tiempoApagarInicioVentanaEmergente=0
            self.cerrarVentanaRecCA()
            print("Se cerró la ventana Recomendación Calidad del Aire")    

    def cerrarVentanaRecCA(self):
        self.tiempoApagarFinVentanaEmergente = 0
        self.tiempoApagarInicioVentanaEmergente=0
        self.after_cancel(self.afterID)  # Cancelar la ejecución de after
        self.raiz.grab_set()
        self.destroy()  # Cerrar la ventana
        self.raiz.attributes('-fullscreen', True)

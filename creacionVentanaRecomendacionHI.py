from __future__ import print_function
from tkinter import * #Nos permite realizar la interfaz gráfica
import time

class ventanaRecomendacionHI(Toplevel):
    def __init__(self, raiz, varCompartidas):
        super().__init__(raiz)
        self.attributes('-fullscreen', True)
        self.lift()
        self.raiz = raiz
        self.raiz.grab_release()
        self.title("Recomendaciones")
        self.miFrameRecomendacionHI = Frame(self, bg="black", width=1280, height=800)
        self.miFrameRecomendacionHI.pack()
        self.raiz.attributes('-fullscreen', False)

        tituloRecomendacion = Label(self.miFrameRecomendacionHI, text="RECOMENDACIONES", font=("Asap SemiBold", 38, "bold"), fg="#F2AA84", bg="black")
        tituloRecomendacion.place(x=351, y=50)

        if (varCompartidas["valueHeatIndex"] <= 26) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Seguro
            textoRecomendacion1 = "EL AMBIENTE ES SEGURO"
            textoRecomendacion2 = "No es necesaria ninguna protección"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionSeguro.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=312, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=268, y=295)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=522, y=440)
            self.etiquetaImagenRecHI2.place(x=10, y=600)
            self.etiquetaImagenRecHI3.place(x=10, y=600)
            self.etiquetaImagenRecHI4.place(x=10, y=600)
            self.etiquetaImagenRecHI5.place(x=10, y=600)
            self.etiquetaImagenRecHI6.place(x=10, y=600)
            self.etiquetaImagenRecHI7.place(x=10, y=600)
            self.etiquetaImagenRecHI8.place(x=10, y=600)
            self.etiquetaImagenRecHI9.place(x=10, y=600)
            self.etiquetaImagenRecHI10.place(x=10, y=600)

        elif (27 <= varCompartidas["valueHeatIndex"] <= 32) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Precaución
            textoRecomendacion1 = "EXISTE RIESGO DE FATIGA"
            textoRecomendacion2 = "- Evite realizar actividad física\n- Evite una exposición prolongada en el ambiente"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionActividadFisica.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionTiempo.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=300, y=175)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=290)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=408, y=495)
            self.etiquetaImagenRecHI2.place(x=675, y=495)
            self.etiquetaImagenRecHI3.place(x=10, y=600)
            self.etiquetaImagenRecHI4.place(x=10, y=600)
            self.etiquetaImagenRecHI5.place(x=10, y=600)
            self.etiquetaImagenRecHI6.place(x=10, y=600)
            self.etiquetaImagenRecHI7.place(x=10, y=600)
            self.etiquetaImagenRecHI8.place(x=10, y=600)
            self.etiquetaImagenRecHI9.place(x=10, y=600)
            self.etiquetaImagenRecHI10.place(x=10, y=600)
        elif (33 <= varCompartidas["valueHeatIndex"] <= 40) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Precaución extrema
            textoRecomendacion1 = "POSIBLE GOLPE DE CALOR PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- Evite realizar actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionSombrilla.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 26), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=150)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 25), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=300)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=40, y=555)
            self.etiquetaImagenRecHI4.place(x=292, y=555)
            self.etiquetaImagenRecHI2.place(x=540, y=555)
            self.etiquetaImagenRecHI3.place(x=1042, y=555)
            self.etiquetaImagenRecHI5.place(x=788, y=555)
            self.etiquetaImagenRecHI6.place(x=1, y=1)
            self.etiquetaImagenRecHI7.place(x=1, y=1)
            self.etiquetaImagenRecHI8.place(x=1, y=1)
            self.etiquetaImagenRecHI9.place(x=1, y=1)
            self.etiquetaImagenRecHI10.place(x=1, y=1)

        elif (41 <= varCompartidas["valueHeatIndex"] <= 51) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Peligro 
            textoRecomendacion1 = "PROBABLE GOLPE DE CALOR PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- No realice actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Refrésquese con agua fría cuando sea necesario\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionDucha.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionSombrilla.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 26), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=150)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 25), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=300)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=40, y=565)
            self.etiquetaImagenRecHI4.place(x=242, y=565)
            self.etiquetaImagenRecHI2.place(x=444, y=565)
            self.etiquetaImagenRecHI3.place(x=1050, y=565)
            self.etiquetaImagenRecHI5.place(x=848, y=565)
            self.etiquetaImagenRecHI6.place(x=646, y=565)
            self.etiquetaImagenRecHI7.place(x=1, y=1)
            self.etiquetaImagenRecHI8.place(x=1, y=1)
            self.etiquetaImagenRecHI9.place(x=1, y=1)
            self.etiquetaImagenRecHI10.place(x=1, y=1)

        elif (52 <= varCompartidas["valueHeatIndex"] <= 92) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Peligro Extremo
            textoRecomendacion1 = "GOLPE DE CALOR ALTAMENTE PROBABLE PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- No realice actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Refrésquese con agua fría cuando sea necesario\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionDucha.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionSombrilla.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 26), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=40, y=150)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 25), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=300)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=40, y=565)
            self.etiquetaImagenRecHI4.place(x=242, y=565)
            self.etiquetaImagenRecHI2.place(x=444, y=565)
            self.etiquetaImagenRecHI3.place(x=1050, y=565)
            self.etiquetaImagenRecHI5.place(x=848, y=565)
            self.etiquetaImagenRecHI6.place(x=646, y=565)
            self.etiquetaImagenRecHI7.place(x=1, y=1)
            self.etiquetaImagenRecHI8.place(x=1, y=1)
            self.etiquetaImagenRecHI9.place(x=1, y=1)
            self.etiquetaImagenRecHI10.place(x=1, y=1)
        elif (93 <= varCompartidas["valueHeatIndex"]) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Mortal
            textoRecomendacion1 = "VALORES MORTALES PARA EL SER HUMANO"
            textoRecomendacion2 = ""
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionPeligro.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=79, y=205)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=225)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=537, y=390)
            self.etiquetaImagenRecHI2.place(x=10, y=600)
            self.etiquetaImagenRecHI3.place(x=10, y=600)
            self.etiquetaImagenRecHI4.place(x=10, y=600)
            self.etiquetaImagenRecHI5.place(x=10, y=600)
            self.etiquetaImagenRecHI6.place(x=10, y=600)
            self.etiquetaImagenRecHI7.place(x=10, y=600)
            self.etiquetaImagenRecHI8.place(x=10, y=600)
            self.etiquetaImagenRecHI9.place(x=10, y=600)
            self.etiquetaImagenRecHI10.place(x=10, y=600)
        else:
            textoRecomendacion1 = "EL RANGO DE VALORES NO ES ADECUADO"
            textoRecomendacion2 = "- Debido a los rangos de temperatura y humedad no se\n  puede determinar el índice de humedad"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            self.Recomendacion1 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion1, font=("Asap SemiBold", 38), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion1.place(x=98, y=195)
            self.Recomendacion2 = Label(self.miFrameRecomendacionHI, text=textoRecomendacion2, font=("Asap SemiBold", 31), fg="#FFFFFF", bg="black", justify="left")
            self.Recomendacion2.place(x=40, y=310)
            self.imagenRecomendacionHI1=PhotoImage(file=imagenMostrarRecHI1)
            self.imagenRecomendacionHI2=PhotoImage(file=imagenMostrarRecHI2)
            self.imagenRecomendacionHI3=PhotoImage(file=imagenMostrarRecHI3)
            self.imagenRecomendacionHI4=PhotoImage(file=imagenMostrarRecHI4)
            self.imagenRecomendacionHI5=PhotoImage(file=imagenMostrarRecHI5)
            self.imagenRecomendacionHI6=PhotoImage(file=imagenMostrarRecHI6)
            self.imagenRecomendacionHI7=PhotoImage(file=imagenMostrarRecHI7)
            self.imagenRecomendacionHI8=PhotoImage(file=imagenMostrarRecHI8)
            self.imagenRecomendacionHI9=PhotoImage(file=imagenMostrarRecHI9)
            self.imagenRecomendacionHI10=PhotoImage(file=imagenMostrarRecHI10)
            self.etiquetaImagenRecHI1 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI1, bg="black")
            self.etiquetaImagenRecHI2 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI2, bg="black")
            self.etiquetaImagenRecHI3 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI3, bg="black")
            self.etiquetaImagenRecHI4 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI4, bg="black")
            self.etiquetaImagenRecHI5 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI5, bg="black")
            self.etiquetaImagenRecHI6 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI6, bg="black")
            self.etiquetaImagenRecHI7 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI7, bg="black")
            self.etiquetaImagenRecHI8 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI8, bg="black")
            self.etiquetaImagenRecHI9 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI9, bg="black")
            self.etiquetaImagenRecHI10 =Label(self.miFrameRecomendacionHI, image=self.imagenRecomendacionHI10, bg="black")
            self.etiquetaImagenRecHI1.place(x=487, y=430)
            self.etiquetaImagenRecHI2.place(x=10, y=600)
            self.etiquetaImagenRecHI3.place(x=10, y=600)
            self.etiquetaImagenRecHI4.place(x=10, y=600)
            self.etiquetaImagenRecHI5.place(x=10, y=600)
            self.etiquetaImagenRecHI6.place(x=10, y=600)
            self.etiquetaImagenRecHI7.place(x=10, y=600)
            self.etiquetaImagenRecHI8.place(x=10, y=600)
            self.etiquetaImagenRecHI9.place(x=10, y=600)
            self.etiquetaImagenRecHI10.place(x=10, y=600)

        self.tiempoApagarInicioVentanaEmergente = time.time()
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesHI(varCompartidas))
        #self.actualizarVentanaRecomendacionesCA()
        self.botonSalirRecHI = Button(self, text= "REGRESAR", font=("bold"), command = lambda:self.cerrarVentanaRecHI(), bg="#FFFFFF",borderwidth=1)
        self.botonSalirRecHI.place(x=1145, y=20)
    
    def actualizarVentanaRecomendacionesHI(self, varCompartidas):
        if (varCompartidas["valueHeatIndex"] <= 26) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Seguro
            textoRecomendacion1 = "EL AMBIENTE ES SEGURO"
            textoRecomendacion2 = "No es necesaria ninguna protección"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionSeguro.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 400+120+5+2+25+4-30-3-1
            y1= 150+150+40+20+30+20+10+20
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 10
            y6= 600
            x7= 10
            y7= 600
            x8= 10
            y8= 600
            x9= 10
            y9= 600
            x10= 10
            y10= 600
            x11= 40+100+50+20+50+30+40-10-6-2
            y11= 100+20+30-15+20+20
            x12= 40+100+50+20+20+35+3
            y12= 100+20+30+50+15+10+20+10+20+20
            letra1= 38
            letra2= 31

        elif (27 <= varCompartidas["valueHeatIndex"] <= 32) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Precaución
            textoRecomendacion1 = "EXISTE RIESGO DE FATIGA"
            textoRecomendacion2 = "- Evite realizar actividad física\n- Evite una exposición prolongada en el ambiente"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionActividadFisica.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionTiempo.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 400+120+5+2-50-30-15-100-40+50+100-15-5-10-4
            y1= 150+150+150+40+50-30+10-15-10
            x2= 400+120+5+2-50-30-15+25+25+40-2+10+10+50+100-15
            y2= 150+150+150+40+50-30+10-15-10
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 10
            y6= 600
            x7= 10
            y7= 600
            x8= 10
            y8= 600
            x9= 10
            y9= 600
            x10= 10
            y10= 600
            x11= 40+100+50+20-2+100-3-3-2
            y11= 100+20+30-15+20+20
            x12= 40
            y12= 100+20+30+50+15+10+50+25-30+20
            letra1= 38
            letra2= 31

        elif (33 <= varCompartidas["valueHeatIndex"] <= 40) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Precaución extrema
            textoRecomendacion1 = "POSIBLE GOLPE DE CALOR PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- Evite realizar actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionSombrilla.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 40
            y1= 150+150+150+40+50-30+10+50-5-10
            x2= 400+120+5+2-50-30-15+25+25+40-2+10+10
            y2= 150+150+150+40+50-30+10+50-5-10
            x3= 400+120+5+2-50-30-15-100-40+100+300+400-80+30
            y3= 150+150+150+40+50-30+10+50-5-10
            x4= 400+120+5+2-50-30-15-100-40
            y4= 150+150+150+40+50-30+10+50-5-10
            x5= 400+120+5+2+100-10-15+25+30+40+5+40+26+20
            y5= 150+150+150+40+50-30+10+50-5-10
            x6= 1
            y6= 1
            x7= 1
            y7= 1
            x8= 1
            y8= 1
            x9= 1
            y9= 1
            x10= 1
            y10= 1
            x11= 40
            y11= 100+20+30-15+20+20-20-5
            x12= 40
            y12= 100+20+30+50+15+10+20+10+20+20+30-10-5-10
            letra1= 26
            letra2= 25

        elif (41 <= varCompartidas["valueHeatIndex"] <= 51) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Peligro 
            textoRecomendacion1 = "PROBABLE GOLPE DE CALOR PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- No realice actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Refrésquese con agua fría cuando sea necesario\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionDucha.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionSombrilla.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 40
            y1= 150+150+150+40+50-30+10+50-5
            x2= 444
            y2= 150+150+150+40+50-30+10+50-5
            x3= 444+180+22+180+22+180+22
            y3= 150+150+150+40+50-30+10+50-5
            x4= 400+120+5+2-50-30-15-100-40-5-15-10-40+20
            y4= 150+150+150+40+50-30+10+50-5
            x5= 444+180+22+180+22
            y5= 150+150+150+40+50-30+10+50-5
            x6= 444+180+22
            y6= 150+150+150+40+50-30+10+50-5
            x7= 1
            y7= 1
            x8= 1
            y8= 1
            x9= 1
            y9= 1
            x10= 1
            y10= 1
            x11= 40
            y11= 100+20+30-15+20+20-20-5
            x12= 40
            y12= 100+20+30+50+15+10+20+10+20+20+30-10-5-10
            letra1= 26
            letra2= 25

        elif (52 <= varCompartidas["valueHeatIndex"] <= 92) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Peligro Extremo
            textoRecomendacion1 = "GOLPE DE CALOR ALTAMENTE PROBABLE PARA TODA LA POBLACIÓN.\nRIESGOS MAYORES PARA NIÑOS, PERSONAS DE LA TERCERA EDAD,\nENFERMOS CRÓNICOS O PERSONAS QUE TOMAN MEDICAMENTOS"
            textoRecomendacion2 = "- No realice actividad física\n- Use ropa ligera y transpirable\n- Hidrátese lo suficiente\n- Busque zonas donde pueda mantenerse fresco\n- Refrésquese con agua fría cuando sea necesario\n- Evite el café y las bebidas muy dulces (favorecen la deshidratación)"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionActividadFisica.png" 
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionBotella.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionCafe.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionRopa.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionDucha.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionesPequenas/recomendacionSombrilla.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 40
            y1= 150+150+150+40+50-30+10+50-5
            x2= 444
            y2= 150+150+150+40+50-30+10+50-5
            x3= 444+180+22+180+22+180+22
            y3= 150+150+150+40+50-30+10+50-5
            x4= 400+120+5+2-50-30-15-100-40-5-15-10-40+20
            y4= 150+150+150+40+50-30+10+50-5
            x5= 444+180+22+180+22
            y5= 150+150+150+40+50-30+10+50-5
            x6= 444+180+22
            y6= 150+150+150+40+50-30+10+50-5
            x7= 1
            y7= 1
            x8= 1
            y8= 1
            x9= 1
            y9= 1
            x10= 1
            y10= 1
            x11= 40
            y11= 100+20+30-15+20+20-20-5
            x12= 40
            y12= 100+20+30+50+15+10+20+10+20+20+30-10-5-10
            letra1= 26
            letra2= 25

        elif (93 <= varCompartidas["valueHeatIndex"]) and (80 <= varCompartidas["temperaturaFAjustada"] <= 110) and (40 <= varCompartidas["humedadC"] <= 100): #Mortal
            textoRecomendacion1 = "VALORES MORTALES PARA EL SER HUMANO"
            textoRecomendacion2 = ""
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/recomendacionesHI/recomendacionPeligro.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 400+120+5+2-30-20-35+45+20+50-10-10
            y1= 150+150+40+20+30
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 10
            y6= 600
            x7= 10
            y7= 600
            x8= 10
            y8= 600
            x9= 10
            y9= 600
            x10= 10
            y10= 600
            x11= 25+120+50+25+30+30-10-5-50-30-5-6-5+45-80-40-10-5
            y11= 100+20+30-15+40+20+10
            x12= 40
            y12= 100+20+30+50+15+10
            letra1= 38
            letra2= 31

        else:
            textoRecomendacion1 = "EL RANGO DE VALORES NO ES ADECUADO"
            textoRecomendacion2 = "- Debido a los rangos de temperatura y humedad no se\n  puede determinar el índice de humedad"
            imagenMostrarRecHI1="/home/xibernetiq/Documents/Tesis/Interfaz/CalidadAire/iconoMalaLectura2.png"
            imagenMostrarRecHI2="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI3="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI4="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI5="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI6="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI7="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI8="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI9="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            imagenMostrarRecHI10="/home/xibernetiq/Documents/Tesis/Interfaz/DisenoInterfaz/imagenColorNegro.png"
            x1= 400+120+5+2-30-20-35+45
            y1= 150+150+40+20+30+20+10+10
            x2= 10
            y2= 600
            x3= 10
            y3= 600
            x4= 10
            y4= 600
            x5= 10
            y5= 600
            x6= 10
            y6= 600
            x7= 10
            y7= 600
            x8= 10
            y8= 600
            x9= 10
            y9= 600
            x10= 10
            y10= 600
            x11= 25+120+50+25+30+30-10-5-50-30-5-6-5+45-80-40-10-5+19
            y11= 100+20+30-15+40+20+10-10
            x12= 40
            y12= 100+20+30+50+15+10+20+10+20+20+15-5+5
            letra1= 38
            letra2= 31
        
        self.Recomendacion1.config(text=textoRecomendacion1, font=("Asap SemiBold", letra1), justify="left")
        self.Recomendacion2.config(text=textoRecomendacion2, font=("Asap SemiBold", letra2), justify="left")
        self.Recomendacion1.place(x=x11, y=y11)
        self.Recomendacion2.place(x=x12, y=y12)
        self.imagenRecomendacionHI1.config(file=imagenMostrarRecHI1)
        self.imagenRecomendacionHI2.config(file=imagenMostrarRecHI2)
        self.imagenRecomendacionHI3.config(file=imagenMostrarRecHI3)
        self.imagenRecomendacionHI4.config(file=imagenMostrarRecHI4)
        self.imagenRecomendacionHI5.config(file=imagenMostrarRecHI5)
        self.imagenRecomendacionHI6.config(file=imagenMostrarRecHI6)
        self.imagenRecomendacionHI7.config(file=imagenMostrarRecHI7)
        self.imagenRecomendacionHI8.config(file=imagenMostrarRecHI8)
        self.imagenRecomendacionHI9.config(file=imagenMostrarRecHI9)
        self.imagenRecomendacionHI10.config(file=imagenMostrarRecHI10)
        self.etiquetaImagenRecHI1.place(x=x1, y=y1)
        self.etiquetaImagenRecHI2.place(x=x2, y=y2)
        self.etiquetaImagenRecHI3.place(x=x3, y=y3)
        self.etiquetaImagenRecHI4.place(x=x4, y=y4)
        self.etiquetaImagenRecHI5.place(x=x5, y=y5)
        self.etiquetaImagenRecHI6.place(x=x6, y=y6)
        self.etiquetaImagenRecHI7.place(x=x7, y=y7)
        self.etiquetaImagenRecHI8.place(x=x8, y=y8)
        self.etiquetaImagenRecHI9.place(x=x9, y=y9)
        self.etiquetaImagenRecHI10.place(x=x10, y=y10)
        
        print("\nEstá abierta ventana recomendaciones del Índice de Calor\n")
        self.afterID = self.after(2000, lambda: self.actualizarVentanaRecomendacionesHI(varCompartidas))
        
        self.tiempoApagarFinVentanaEmergente = time.time()
        if ((self.tiempoApagarFinVentanaEmergente - self.tiempoApagarInicioVentanaEmergente) >= 20):
            self.tiempoApagarFinVentanaEmergente=0
            self.tiempoApagarInicioVentanaEmergente=0
            self.cerrarVentanaRecHI()
            print("Se cerró la ventana Recomendación del Índice de Calor")    


    def cerrarVentanaRecHI(self):
        self.tiempoApagarFinVentanaEmergente=0
        self.tiempoApagarInicioVentanaEmergente=0
        self.after_cancel(self.afterID)  # Cancelar la ejecución de after
        self.raiz.grab_set()
        self.destroy()  # Cerrar la ventana
        self.raiz.attributes('-fullscreen', True)
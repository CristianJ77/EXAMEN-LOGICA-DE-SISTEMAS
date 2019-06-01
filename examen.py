from tkinter import*
raiz= Tk()

#Curso: Logica de Sistemas
#Semestre: ciclo 1
#Nombre: Cristian Jose Figueroa Estrada
#carne: 0907-29-22929

miFrame=Frame(raiz,width=500,height=300)
miFrame.pack()

#Caja de texto en la que el usario ingresara datos
Cajadetex=Entry(miFrame)
Cajadetex.place(x="15", y="100")
LabelPre=Label(miFrame,text="                                                                                                                                                                                       ")
LabelPre.place(x="10", y="25")




raiz.mainloop()

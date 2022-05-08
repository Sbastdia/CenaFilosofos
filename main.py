import tkinter as tk
from filosofos_beta import *



class Ventana():
    def __init__(self):
        self.window= tk.Tk()
        self.window.title("Bienvenidos a la cena")
        #self.window.configure(background="light steel blue")
        self.texto=tk.Text(self.window, height=30,width=80)
        self.scroll= tk.Scrollbar(self.window)
        self.lista=[]
        self.lista2= []
        self.lista3= []
        self.entradasFilosofos()
        self.texto.configure(yscrollcommand= self.scroll.set)
        self.texto.pack(side= tk.LEFT)
        self.scroll.config(command= self.texto.yview)
        self.scroll.pack(side= tk.RIGHT,fill= tk.Y)
      # Posicionarla en la ventana.
        
    
        
    def entradasFilosofos(self):        
        for i in range(N):
          entry = tk.Entry(self.window)
          entry.place(x=450, y=50+i*20)
          self.lista.append(entry)
          etiqueta= tk.Label(self.window, text= "Filósofo " + str(i) + ":")
          etiqueta.place(x=350, y=50+i*20)
          etiqueta2= tk.Label(self.window, text= "Tenedor " + str(i))
          etiqueta2.place(x=350, y=200+i*20)

          
          self.lista2.append(etiqueta)
          self.lista3.append(etiqueta2)
          
        tk.Label(self.window, text= "¿Cuántas veces han comido?").place(x=450, y= 20)

              
    def visualización(self,texto):
        self.texto.insert(tk.END, str(texto)+"\n")
    def ocultar(self):
        self.withdraw()
    def mostrar(self):
        self.deiconify()
    def run(self):
      self.window.mainloop()
if __name__=="__main__":
    ventana= Ventana()
    
    lista=[]
    for i in range(N):
        lista.append(filosofo(ventana)) #AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()
    ventana.run()
    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD


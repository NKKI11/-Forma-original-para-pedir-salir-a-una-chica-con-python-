import tkinter as tk
import random

def mover_boton_no(event=None):
    nuevo_x = random.randint(0, ventana.winfo_width() - boton_no.winfo_width())
    nuevo_y = random.randint(0, ventana.winfo_height() - boton_no.winfo_height())
    boton_no.place(x=nuevo_x, y=nuevo_y)

def mostrar_mensaje():
    ventana.title("<3")
    etiqueta.config(text="Perfecto, sabía que dirias que si 😘")

    
# Crear la ventana
ventana = tk.Tk()
ventana.title("<3")
ventana.geometry("600x400")  

# Etiqueta con la pregunta
etiqueta = tk.Label(ventana, text="¿Quieres salir conmigo?", font=("Arial", 24))  
etiqueta.pack(pady=40)

# Botón "Sí"
boton_si = tk.Button(ventana, text="Sí", bg="green", fg="white", font=("Arial", 18), command=mostrar_mensaje, width=10, height=2)
boton_si.place(x=140, y=140)

# Botón "No"
boton_no = tk.Button(ventana, text="No", bg="red", fg="white", font=("Arial", 18), width=10, height=2, command=mover_boton_no)
boton_no.place(x=340, y=140)

ventana.mainloop()



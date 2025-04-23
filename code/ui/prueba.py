import tkinter as tk
from PIL import Image, ImageTk
import os

def mi_funcion():
    print("¡Botón presionado!")

ventana = tk.Tk()
ventana.title("Ejemplo de Botones con Fondo")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Ruta de la imagen de fondo
ruta_base = os.path.dirname(__file__)
ruta_imagen = os.path.join(ruta_base, "..", "..", "graphics", "fsc_3.jpg")
ruta_imagen = os.path.abspath(ruta_imagen)  # Convierte a ruta absoluta

# Cargar imagen
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((400, 300))  # Ajustar al tamaño de la ventana
fondo = ImageTk.PhotoImage(imagen)

# Fondo
label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Botón normal
boton_normal = tk.Button(ventana, text="Botón Normal", command=mi_funcion, font=("Arial", 14), bg="blue", fg="white")
boton_normal.pack(pady=20)

# Botón con bordes redondeados (estilo tradicional)
boton_redondeado = tk.Button(ventana, text="Botón Redondeado", command=mi_funcion, font=("Arial", 14), bg="green", fg="white", relief="solid", bd=5)
boton_redondeado.pack(pady=20)

# Botón con cambio de color al pasar el ratón
def on_enter(boton):
    boton.config(bg="red")

def on_leave(boton):
    boton.config(bg="blue")

boton_hover = tk.Button(ventana, text="Botón Hover", command=mi_funcion, font=("Arial", 14), bg="blue", fg="white")
boton_hover.bind("<Enter>", lambda e: on_enter(boton_hover))
boton_hover.bind("<Leave>", lambda e: on_leave(boton_hover))
boton_hover.pack(pady=20)

ventana.mainloop()

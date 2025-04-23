import tkinter as tk
from PIL import Image, ImageTk
import random

# Función para generar y mostrar un número aleatorio
def show_random_number():
    random_number = random.randint(10, 45)
    label.config(text=str(random_number), fg="red")

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con Número Aleatorio")
root.geometry("1000x600")
root.resizable(False, False)

# Cargar la imagen de fondo
background_image = Image.open("/Users/erickcorona/Documents/TT_2025_A171_SC/graphics/fsc_4.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Crear una etiqueta para la imagen de fondo
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear una etiqueta para mostrar el número aleatorio con fondo transparente
label = tk.Label(root, text="", font=("Helvetica", 48), fg="red", bg="SystemTransparent")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear un botón para generar el número aleatorio
button = tk.Button(root, text="Generar Número Aleatorio", command=show_random_number, font=("Helvetica", 24))
button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Ejecutar la aplicación
root.mainloop()

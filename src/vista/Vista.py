import customtkinter as ctk
import tkinter as tk
from tkinter import Canvas
#class Vista:
#    def __init__(self, root):
 #       self.root = root
  #      self.root.title("Aplicación MVC")
   #     
    #    # Configura la ventana principal
     #   self.root.geometry("300x200")
      #  
        # Etiqueta
       # self.label = ctk.CTkLabel(master=self.root, text="Hola", font=("Arial", 16))
        #self.label.pack(pady=20)
        
        # Botón
        #self.boton = ctk.CTkButton(master=self.root, text="Actualizar", command=self.actualizar)
        #self.boton.pack(pady=20)

    #def actualizar(self):
     #   self.label.config(text="Actualizado")

# Función para crear un botón redondeado con eventos de hover
def create_rounded_button(canvas, x, y, width, height, text, command):
    radius = 50
    color_interior = "#729020"
    color_borde = "#2d3e06"
    color_hover = "#88a838"

    # Dibujar el fondo redondeado del botón
    border_rects = [
        canvas.create_oval(x, y, x + radius, y + radius, fill=color_borde, outline=""),
        canvas.create_oval(x + width - radius, y, x + width, y + radius, fill=color_borde, outline=""),
        canvas.create_oval(x, y + height - radius, x + radius, y + height, fill=color_borde, outline=""),
        canvas.create_oval(x + width - radius, y + height - radius, x + width, y + height, fill=color_borde, outline=""),
        canvas.create_rectangle(x + radius // 2, y, x + width - radius // 2, y + height, fill=color_borde, outline=""),
        canvas.create_rectangle(x, y + radius // 2, x + width, y + height - radius // 2, fill=color_borde, outline=""),
    ]
    inner_rects = [
        canvas.create_oval(x + 5, y + 5, x + radius - 5, y + radius - 5, fill=color_interior, outline=""),
        canvas.create_oval(x + width - radius + 5, y + 5, x + width - 5, y + radius - 5, fill=color_interior, outline=""),
        canvas.create_oval(x + 5, y + height - radius + 5, x + radius - 5, y + height - 5, fill=color_interior, outline=""),
        canvas.create_oval(x + width - radius + 5, y + height - radius + 5, x + width - 5, y + height - 5, fill=color_interior, outline=""),
        canvas.create_rectangle(x + radius // 2 + 5, y + 5, x + width - radius // 2 - 5, y + height - 5, fill=color_interior, outline=""),
        canvas.create_rectangle(x + 5, y + radius // 2 + 5, x + width - 5, y + height - radius // 2 - 5, fill=color_interior, outline=""),
    ]
    button_text = canvas.create_text(x + width // 2, y + height // 2, text=text, fill="black", font=("Helvetica", 16, "bold"))

    def on_click(event):
        command()

    def on_enter(event):
        for shape in inner_rects:
            canvas.itemconfig(shape, fill=color_hover)

    def on_leave(event):
        for shape in inner_rects:
            canvas.itemconfig(shape, fill=color_interior)

    # Asociar eventos al botón
    canvas.tag_bind(button_text, "<Button-1>", on_click)
    for shape in inner_rects:
        canvas.tag_bind(shape, "<Button-1>", on_click)
        canvas.tag_bind(shape, "<Enter>", on_enter)
        canvas.tag_bind(shape, "<Leave>", on_leave)
    canvas.tag_bind(button_text, "<Enter>", on_enter)
    canvas.tag_bind(button_text, "<Leave>", on_leave)

# Crear ventana principal
root = tk.Tk()
root.title("Interfaz con botones redondeados")
root.geometry("1000x1000")  # Tamaño de la ventana 1080x1080
root.config(bg="white")  # Fondo de la ventana blanco

# Crear frame para contener los botones y centrarlo
frame = tk.Frame(root, bg="white")
frame.pack(expand=True)

# Crear canvas dentro del frame
canvas = Canvas(frame, width=400, height=500, bg="white", highlightthickness=0)
canvas.pack()

# Funciones de comando para los botones
def mostrar_arbol():
    print("Mostrar árbol")

def busqueda():
    print("Búsqueda")

def busqueda_especializada():
    print("Búsqueda especializada")

def insertar():
    print("Insertar")

def eliminar():
    print("Eliminar")

def recorrido_por_niveles():
    print("Recorrido por niveles")

def salir():
    root.quit()

# Crear botones
create_rounded_button(canvas, 10, 10, 330, 50, "MOSTRAR ÁRBOL", mostrar_arbol)
create_rounded_button(canvas, 10, 70, 330, 50, "BÚSQUEDA", busqueda)
create_rounded_button(canvas, 10, 130, 330, 50, "BÚSQUEDA ESPECIALIZADA", busqueda_especializada)
create_rounded_button(canvas, 10, 190, 330, 50, "INSERTAR", insertar)
create_rounded_button(canvas, 10, 250, 330, 50, "ELIMINAR", eliminar)
create_rounded_button(canvas, 10, 310, 330, 50, "RECORRIDO POR NIVELES", recorrido_por_niveles)
create_rounded_button(canvas, 10, 370, 330, 50, "SALIR", salir)

# Ejecutar la aplicación
root.mainloop()


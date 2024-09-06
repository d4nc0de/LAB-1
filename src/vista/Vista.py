import customtkinter as ctk
import tkinter as tk
from tkinter import Canvas

def actualizar_derecha(titulo, texto_central, con_input=False, input_text1=None, input_text2=None, boton_accion="Buscar"):
    # Limpiar el frame derecho
    for widget in right_frame.winfo_children():
        widget.destroy()

    # Mostrar el título y el texto central con el mismo estilo y formato que los botones
    label_titulo = ctk.CTkLabel(master=right_frame, text=titulo, font=("Arial", 28, "bold"), text_color="black")
    label_titulo.pack(pady=40)

    label_central = ctk.CTkLabel(master=right_frame, text=texto_central, font=("Arial", 28, "bold"), text_color="black")
    label_central.pack(pady=40)

    if con_input:
        label_input1 = ctk.CTkLabel(master=right_frame, text=input_text1, font=("Arial", 28, "bold"), text_color="black")
        label_input1.pack(pady=20)
        input1 = ctk.CTkEntry(master=right_frame, width=200)
        input1.pack(pady=10)

        if input_text2:
            label_input2 = ctk.CTkLabel(master=right_frame, text=input_text2, font=("Arial", 28, "bold"), text_color="black")
            label_input2.pack(pady=20)
            input2 = ctk.CTkEntry(master=right_frame, width=200)
            input2.pack(pady=10)

        # Botón con el mismo estilo y texto dinámico
        boton_accion = ctk.CTkButton(master=right_frame, text=boton_accion, font=("Arial", 28, "bold"), fg_color="#be2332", hover_color="#5b081c", text_color="black")
        boton_accion.pack(pady=20)

# Funciones para actualizar el lado derecho con el texto adecuado del botón
def mostrar_arbol():
    actualizar_derecha("Mostrar Árbol", "Aún no implementado")

def busqueda():
    actualizar_derecha("Búsqueda", "Ingrese un nodo:", con_input=True, input_text1="Nodo", boton_accion="Buscar")

def busqueda_especializada():
    actualizar_derecha("Búsqueda Especializada", "Ingresos mínimos internacionales:", con_input=True, input_text1="Monto", input_text2="Ingrese un año", boton_accion="Buscar")

def insertar():
    actualizar_derecha("Insertar Nodo", "Inserte nodo", con_input=True, input_text1="Nombre del nodo", boton_accion="Agregar")

def eliminar():
    actualizar_derecha("Eliminar Nodo", "Elimine nodo", con_input=True, input_text1="Nombre del nodo", boton_accion="Eliminar")

def recorrido_por_niveles():
    actualizar_derecha("Recorrido por Niveles", "Muy pronto")

# Función para crear un botón redondeado con eventos de hover
def create_rounded_button(canvas, x, y, width, height, text, command):
    radius = 50
    color_interior = "#be2332"
    color_borde = "#1d1f2d"
    color_hover = "#5b081c"

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
    button_text = canvas.create_text(x + width // 2, y + height // 2, text=text, fill="black", font=("Arial", 18, "bold"))

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
root.geometry("1500x1000")  # Tamaño de la ventana
root.config(bg="white")  # Fondo de la ventana blanco

# Crear frame para contener los botones y centrarlo
frame = tk.Frame(root, bg="white")
frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)  # Alineación a la izquierda

# Crear frame derecho para mostrar el contenido dinámico
right_frame = tk.Frame(root, bg="white")
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Crear canvas dentro del frame izquierdo
canvas = Canvas(frame, width=500, height=1000, bg="white", highlightthickness=0)
canvas.pack()

# Crear botones
create_rounded_button(canvas, 50, 80, 380, 50, "MOSTRAR ÁRBOL", mostrar_arbol)
create_rounded_button(canvas, 50, 140, 380, 50, "BÚSQUEDA", busqueda)
create_rounded_button(canvas, 50, 200, 380, 50, "BÚSQUEDA ESPECIALIZADA", busqueda_especializada)
create_rounded_button(canvas, 50, 260, 380, 50, "INSERTAR", insertar)
create_rounded_button(canvas, 50, 320, 380, 50, "ELIMINAR", eliminar)
create_rounded_button(canvas, 50, 380, 380, 50, "RECORRIDO POR NIVELES", recorrido_por_niveles)
create_rounded_button(canvas, 50, 440, 380, 50, "SALIR", root.quit)

# Ejecutar la aplicación
root.mainloop()

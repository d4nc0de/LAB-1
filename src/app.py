import customtkinter as ctk
from tkinter import PhotoImage, messagebox
import pandas as pd
import random
from avl_tree import AVLTree
from visualize import visualize_tree
import tkinter as tk
from tkinter import Canvas
import sys

sys.setrecursionlimit(1500)

class AVLApp:
    def __init__(self, root):
        self.tree = AVLTree()
        self.root = None
        self.right_frame = tk.Frame(root, bg="white")
        self.right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Crear la ventana principal
        root.title("ARBOL AVL PELICULAS")
        root.geometry("1500x1000")
        root.config(bg="white")

        # Crear frame para botones y centrarlo
        frame = tk.Frame(root, bg="white")
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Crear canvas dentro del frame
        canvas = Canvas(frame, width=1500, height=1000, bg="white", highlightthickness=0)
        canvas.pack(anchor='w')

        # Cargar y redimensionar la imagen
        image_path = "data/inicio.png"
        original_image = PhotoImage(file=image_path)
        resized_image = self.resize_image(original_image, 700, 600)
        canvas.create_image(1000, 400, anchor=tk.CENTER, image=resized_image)

        # Botones del menú principal
        self.create_rounded_button(canvas, 100, 90, 380, 50, "MOSTRAR ÁRBOL", self.visualize_tree)
        self.create_rounded_button(canvas, 100, 150, 380, 50, "BÚSQUEDA", self.search_node)
        self.create_rounded_button(canvas, 100, 210, 380, 50, "BÚSQUEDA ESPECIALIZADA", self.search_specific)
        self.create_rounded_button(canvas, 100, 270, 380, 50, "INSERTAR", self.insert_node)
        self.create_rounded_button(canvas, 100, 330, 380, 50, "ELIMINAR", self.delete_node)
        self.create_rounded_button(canvas, 100, 390, 380, 50, "RECORRIDO POR NIVELES", self.level_order_traversal)
        self.create_rounded_button(canvas, 100, 450, 380, 50, "SALIR", root.quit)

        self.load_csv_and_insert_nodes()
        root.mainloop()

    def resize_image(self, image, new_width, new_height):
        return image.subsample(int(image.width() / new_width), int(image.height() / new_height))

    def create_rounded_button(self, canvas, x, y, width, height, text, command):
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

    def load_csv_and_insert_nodes(self):
        # Leer el archivo CSV
        df = pd.read_csv('data/dataset_movies.csv')
        # Seleccionar títulos aleatorios
        titles = random.sample(list(df['Title']), 30)
        titles = [title for title in titles if ':' not in title]

        for title in titles:
            self.root = self.tree.insert(self.root, title)
        messagebox.showinfo("Info", f"Inserted titles: {', '.join(titles)}")

    def actualizar_derecha(self, titulo, texto_central, con_input=False, input_text1=None, input_text2=None, boton_accion="Buscar"):
        for widget in self.right_frame.winfo_children():
            widget.destroy()  # Limpiar el contenido anterior del frame

        # Dibujar fondo blanco
        fondo = tk.Frame(self.right_frame, bg="white", bd=2, relief=tk.RIDGE)
        fondo.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Crear título y texto central
        label_titulo = ctk.CTkLabel(master=fondo, text=titulo, font=("Arial", 30, "bold"), text_color="black")
        label_titulo.pack(pady=20)

        label_central = ctk.CTkLabel(master=fondo, text=texto_central, font=("Arial", 30, "bold"), text_color="black")
        label_central.pack(pady=20)

        # Añadir entradas y botones según la acción
        if con_input:
            label_input1 = ctk.CTkLabel(master=fondo, text=input_text1, font=("Arial", 20, "bold"), text_color="black")
            label_input1.pack(pady=10)
            self.input1 = ctk.CTkEntry(master=fondo, width=380)
            self.input1.pack(pady=10)
            self.input1.configure(state='normal')  # Asegurarse de que el widget esté habilitado

            if input_text2:
                label_input2 = ctk.CTkLabel(master=fondo, text=input_text2, font=("Arial", 20, "bold"), text_color="black")
                label_input2.pack(pady=10)
                self.input2 = ctk.CTkEntry(master=fondo, width=380)
                self.input2.pack(pady=10)
                self.input2.configure(state='normal')  # Asegurarse de que el widget esté habilitado

        self.boton_accion = ctk.CTkButton(master=fondo, text=boton_accion, font=("Arial", 20, "bold"),
                                        fg_color="#be2332", hover_color="#5b081c", text_color="black")
        self.boton_accion.pack(pady=20)

    def visualize_tree(self):
        visualize_tree(self.root)

    def search_node(self):
        self.actualizar_derecha("BÚSQUEDA", "Ingrese el nodo a buscar", con_input=True, input_text1="Nombre del nodo", boton_accion="Buscar")
        self.boton_accion.configure(command=self.execute_search)

    def execute_search(self):
        title = self.input1.get()
        node = self.tree.search(self.root, title)
        if node:
            messagebox.showinfo("Info", f"Found {title}")
        else:
            messagebox.showinfo("Info", f"{title} not found")

    def insert_node(self):
        self.actualizar_derecha("INSERTAR", "Ingrese el nodo a insertar", con_input=True, input_text1="Nombre del nodo", boton_accion="Agregar")
        self.boton_accion.configure(command=self.execute_insert)

    def execute_insert(self):
        title = self.input1.get()
        self.root = self.tree.insert(self.root, title)
        messagebox.showinfo("Info", f"Inserted {title}")

    def delete_node(self):
        self.actualizar_derecha("ELIMINAR", "Ingrese el nodo a eliminar", con_input=True, input_text1="Nombre del nodo", boton_accion="Eliminar")
        self.boton_accion.configure(command=self.execute_delete)

    def execute_delete(self):
        title = self.input1.get()
        self.root = self.tree.delete(self.root, title)
        messagebox.showinfo("Info", f"Deleted {title}")

    def search_specific(self):
        self.actualizar_derecha("BÚSQUEDA ESPECIALIZADA", "Ingrese los criterios", con_input=True, input_text1="Año", input_text2="Ingresos (Foreign)", boton_accion="Buscar")
        self.boton_accion.configure(command=self.execute_specific_search)

    def execute_specific_search(self):
        year = int(self.input1.get())
        foreign_earnings = float(self.input2.get())
        # Leer el archivo CSV y buscar las películas que cumplen con los criterios
        df = pd.read_csv('data/dataset_movies.csv')
        filtered_movies = df[(df['Year'] == year) & 
                             (df['Domestic Percent Earnings'] < df['Foreign Percent Earnings']) & 
                             (df['Foreign Percent Earnings'] >= foreign_earnings)]
        
        if not filtered_movies.empty:
            movies_list = ", ".join(filtered_movies['Title'].tolist())
            messagebox.showinfo("Películas encontradas", f"Películas: {movies_list}")
        else:
            messagebox.showinfo("Búsqueda", "No se encontraron películas con los criterios especificados.")

    def level_order_traversal(self):
        self.tree.level_order_traversal(self.root)

    def visualize_tree(self):
        visualize_tree(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    AVLApp(root)

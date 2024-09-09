import customtkinter as ctk
from tkinter import PhotoImage, messagebox
import pandas as pd
import random
from avl_tree import AVLTree
from visualize import visualize_tree
import tkinter as tk
from tkinter import Canvas

# Función para crear un botón redondeado con eventos de hover
class AVLApp:
    def __init__(self, root):
        self.tree = AVLTree()
        self.root = None
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

        def resize_image(image, new_width, new_height):
            return image.subsample(int(image.width() / new_width), int(image.height() / new_height))

        # Crear ventana principal
        root = tk.Tk()
        root.title("Interfaz con botones redondeados")
        root.geometry("1500x1000")  # Tamaño de la ventana ajustado
        root.config(bg="white")  # Fondo de la ventana blanco

        # Crear frame para contener los botones y centrarlo
        frame = tk.Frame(root, bg="white")
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)  # Alineación a la izquierda

        # Crear canvas dentro del frame
        canvas = Canvas(frame, width=1500, height=1000, bg="white", highlightthickness=0)
        canvas.pack(anchor='w')  # Alinear el canvas a la izquierda

        # Cargar y redimensionar la imagen
        image_path = "data/inicio.png"
        original_image = PhotoImage(file=image_path)
        resized_image = resize_image(original_image, 700, 600)  # Redimensiona la imagen

        # Agregar la imagen al canvas en la nueva posición
        canvas.create_image(1000, 400, anchor=tk.CENTER, image=resized_image)  # Ajustar la posición

        def salir():
            root.quit()
            visualize_tree.quit()


        # Crear botones con las nuevas coordenadas ajustadas
        create_rounded_button(canvas, 100, 90, 380, 50, "MOSTRAR ÁRBOL", self.visualize_tree)
        create_rounded_button(canvas, 100, 150, 380, 50, "BÚSQUEDA", self.search_node)
        create_rounded_button(canvas, 100, 210, 380, 50, "BÚSQUEDA ESPECIALIZADA", self.search_node)
        create_rounded_button(canvas, 100, 270, 380, 50, "INSERTAR", self.insert_node)
        create_rounded_button(canvas, 100, 330, 380, 50, "ELIMINAR", self.delete_node)
        create_rounded_button(canvas, 100, 390, 380, 50, "RECORRIDO POR NIVELES", self.level_order_traversal)
        create_rounded_button(canvas, 100, 450, 380, 50, "SALIR", salir)
        self.load_csv_and_insert_nodes()
        # Ejecutar la aplicación
        root.mainloop()

    def load_csv_and_insert_nodes(self):
                # Leer el archivo CSV
                df = pd.read_csv('data/dataset_movies.csv')
                # Seleccionar 3 títulos aleatorios
                titles = random.sample(list(df['Title']), 30)
                # quitar los titulos que tengan dos puntos
                titles = [title for title in titles if ':' not in title]

                for title in titles:
                    self.root = self.tree.insert(self.root, title)
                messagebox.showinfo("Info", f"Inserted titles: {', '.join(titles)}")

    def insert_node(self):
            title = self.title_entry.get()
            self.root = self.tree.insert(self.root, title)
            messagebox.showinfo("Info", f"Inserted {title}")

    def delete_node(self):
            title = self.title_entry.get()
            self.root = self.tree.delete(self.root, title)
            messagebox.showinfo("Info", f"Deleted {title}")

    def search_node(self):
            title = self.title_entry.get()
            node = self.tree.search(self.root, title)
            if node:
                messagebox.showinfo("Info", f"Found {title}")
            else:
                messagebox.showinfo("Info", f"{title} not found")

    def level_order_traversal(self):
            self.tree.level_order_traversal(self.root)

    def visualize_tree(self):
            visualize_tree(self.root)

if __name__ == "__main__":
    AVLApp(None)

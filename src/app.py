import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
import random
from avl_tree import AVLTree
from visualize import visualize_tree

class AVLApp:
    def __init__(self, root):
        self.tree = AVLTree()
        self.root = None
        self.window = ctk.CTk()
        self.window.title("AVL Tree Application")
        self.window.size(1280,720)

        self.title_entry = ctk.CTkEntry(self.window, placeholder_text="Title")
        self.title_entry.pack()

        self.insert_button = ctk.CTkButton(self.window, text="Insert", command=self.insert_node)
        self.insert_button.pack()

        self.delete_button = ctk.CTkButton(self.window, text="Delete", command=self.delete_node)
        self.delete_button.pack()

        self.search_button = ctk.CTkButton(self.window, text="Search", command=self.search_node)
        self.search_button.pack()

        self.level_order_button = ctk.CTkButton(self.window, text="Level Order Traversal", command=self.level_order_traversal)
        self.level_order_button.pack()

        self.visualize_button = ctk.CTkButton(self.window, text="Visualize Tree", command=self.visualize_tree)
        self.visualize_button.pack()

        self.load_csv_and_insert_nodes()

        self.window.mainloop()


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

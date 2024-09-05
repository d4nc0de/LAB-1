import customtkinter as ctk

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación MVC")
        
        # Configura la ventana principal
        self.root.geometry("1080x1080")
        
        # Etiqueta
        self.label = ctk.CTkLabel(master=self.root, text="Hola", font=("Arial", 16))
        self.label.pack(pady=20)
        
        # Botón
        self.boton = ctk.CTkButton(master=self.root, text="Actualizar", command=self.actualizar)
        self.boton.pack(pady=20)

    def actualizar(self):
        self.label.config(text="Actualizado")

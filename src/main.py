import customtkinter as ctk
#from modelo.modelo import Modelo
from vista.Vista import Vista
#from controlador.controlador import Controlador

def main():
    root = ctk.CTk()
   # modelo = Modelo()
    vista = Vista(root)
    #controlador = Controlador(modelo, vista)
    root.mainloop()

if __name__ == "__main__":
    main()

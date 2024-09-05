import customtkinter as ctk
#from modelo.modelo import Modelo
from controlador.Controlador_peliculas import ControladorPeliculas
from modelo.arbol_avl import AVLTree
from vista.Vista import Vista
#from controlador.controlador import Controlador

def main():
    root = ctk.CTk()
    modelo_arbol = AVLTree()
    vista = Vista(root)
    controlador = ControladorPeliculas(modelo_arbol, vista,'src/static/csv/dataset_movies.csv',limite=3)
    controlador.cargar_peliculas()
    controlador.mostrar_peliculas()
    controlador.preorden(controlador.crear_arbol.raiz)
    #controlador = Controlador(modelo, vista)
    root.mainloop()

if __name__ == "__main__":
    main()

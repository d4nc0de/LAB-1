import customtkinter as ctk
#from modelo.modelo import Modelo
from controlador.Controlador_peliculas import ControladorPeliculas
from vista.Vista import Vista
#from controlador.controlador import Controlador

def main():
    root = ctk.CTk()
   # modelo = Modelo()
    vista = Vista(root)
    controlador = ControladorPeliculas('src/static/csv/dataset_movies.csv', limite=7)
    controlador.cargar_peliculas()
    controlador.mostrar_peliculas()
    #controlador = Controlador(modelo, vista)
    root.mainloop()

if __name__ == "__main__":
    main()

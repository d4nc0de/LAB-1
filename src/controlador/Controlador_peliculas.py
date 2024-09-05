import csv
import random
from modelo.pelicula import Pelicula

class ControladorPeliculas:
    def __init__(self, archivo_csv, limite=7):
        self.archivo_csv = archivo_csv
        self.limite = limite
        self.peliculas = []

    def cargar_peliculas(self):
        with open(self.archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            filas = list(lector_csv)  # Lee todas las filas del archivo CSV

            # Selecciona una muestra aleatoria de filas
            muestra_filas = random.sample(filas, min(self.limite, len(filas)))

            for fila in muestra_filas:
                titulo = fila['Title']
                ano = int(fila['Year'])
                ingresos_mundiales = float(fila['Worldwide Earnings'].replace('$', '').replace(',', ''))
                ingresos_nacionales = float(fila['Domestic Earnings'].replace('$', '').replace(',', ''))
                ingresos_internacionales = float(fila['Foreign Earnings'].replace('$', '').replace(',', ''))

                porcentaje_ingresos_nacionales = float(fila['Domestic Percent Earnings'].replace('%', ''))
                porcentaje_ingresos_internacionales = float(fila['Foreign Percent Earnings'].replace('%', ''))

                pelicula = Pelicula(
                    titulo=titulo,
                    ano=ano,
                    ingresos_mundiales=ingresos_mundiales,
                    ingresos_nacionales=ingresos_nacionales,
                    ingresos_internacionales=ingresos_internacionales,
                    porcentaje_ingresos_nacionales=porcentaje_ingresos_nacionales,
                    porcentaje_ingresos_internacionales=porcentaje_ingresos_internacionales
                )

                self.peliculas.append(pelicula)

    def mostrar_peliculas(self):
        for pelicula in self.peliculas:
            print(pelicula.titulo)
            print(pelicula.ano)
            print(pelicula.ingresos_mundiales)
            print(pelicula.ingresos_nacionales)

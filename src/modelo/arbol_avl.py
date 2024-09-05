class AVLTree:
    def __init__(self):
        self.raiz = None

    def balance_factor(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        self.actualizar_altura(y)
        self.actualizar_altura(x)
        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda
        y.izquierda = x
        x.derecha = T2
        self.actualizar_altura(x)
        self.actualizar_altura(y)
        return y

    def insertar(self, nodo, clave, valor):
        if not nodo:
            return nodo(clave, valor)
        if clave < nodo.clave:
            nodo.izquierda = self.insertar(nodo.izquierda, clave, valor)
        else:
            nodo.derecha = self.insertar(nodo.derecha, clave, valor)

        self.actualizar_altura(nodo)
        balance = self.balance_factor(nodo)

        if balance > 1 and clave < nodo.izquierda.clave:
            return self.rotar_derecha(nodo)
        if balance < -1 and clave > nodo.derecha.clave:
            return self.rotar_izquierda(nodo)
        if balance > 1 and clave > nodo.izquierda.clave:
            nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
            return self.rotar_derecha(nodo)
        if balance < -1 and clave < nodo.derecha.clave:
            nodo.derecha = self.rotar_derecha(nodo.derecha)
            return self.rotar_izquierda(nodo)

        return nodo

    def insertar_pelicula(self, titulo):
        clave = len(titulo)  # Clave es la longitud del título
        self.raiz = self.insertar(self.raiz, clave, titulo)
from node import Node

class AVLTree:
    def insert(self, root, title):
        if not root:
            return Node(title)
        if len(title) < len(root.title):
            root.left = self.insert(root.left, title)
        else:
            root.right = self.insert(root.right, title)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and len(title) < len(root.left.title):
            return self.right_rotate(root)
        if balance < -1 and len(title) > len(root.right.title):
            return self.left_rotate(root)
        if balance > 1 and len(title) > len(root.left.title):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and len(title) < len(root.right.title):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, title):
        if not root:
            return root
        if len(title) < len(root.title):
            root.left = self.delete(root.left, title)
        elif len(title) > len(root.title):
            root.right = self.delete(root.right, title)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.title = temp.title
            root.right = self.delete(root.right, temp.title)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, title):
        if not root or root.title == title:
            return root
        if len(title) < len(root.title):
            return self.search(root.left, title)
        return self.search(root.right, title)

    def level_order_traversal(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        order = ""
        while queue:
            node = queue.pop(0)
            order += node.title + ", "
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(order, end=".")
        return order

    def get_titles(self, root):
        # Inicializar la lista de resultados
        result = []

        # Si el árbol está vacío, devolver la lista vacía
        if not root:
            return result

        # Inicializar la cola para recorrer el árbol por niveles
        queue = []
        queue.append(root)

        # Recorrer el árbol en anchura (nivel por nivel)
        while queue:
            node = queue.pop(0)
            result.append(node.title)  # Agregar el título del nodo a la lista
            #print(node.title, end=" ")  # Imprimir el título del nodo (opcional)

            # Agregar los hijos del nodo actual a la cola
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Devolver la lista de títulos}
        
        return result


    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

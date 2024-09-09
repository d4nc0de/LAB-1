import graphviz

def visualize_tree(root):
    dot = graphviz.Digraph()

    def add_nodes_edges(root):
        if root:
            if root.left or root.right:  # Verifica si el nodo tiene hijos
                dot.node(root.title)
                if root.left:
                    dot.edge(root.title, root.left.title)
                    add_nodes_edges(root.left)
                if root.right:
                    dot.edge(root.title, root.right.title)
                    add_nodes_edges(root.right)
                
    add_nodes_edges(root)
    dot.render('avl_tree', format='png', view=True)

from typing import Any, Optional, Tuple


def insert(self, data: Any) -> bool:
        to_insert = Node(data)
        if self.root is None:
            self.root = to_insert
            return True
        else:
            p, pad = self.search(data)
            if p is not None:
                return False
            else:
                if data < pad.data:
                    pad.left = to_insert
                else:
                    pad.right = to_insert
                return True
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        height_diff = self.get_balance(root)

        if height_diff > 1:
            if self.get_balance(root.left) >= 0:
                return self.simple_left_rotation(root)

        if height_diff <= 0:
           if self.get_balance(root.left) <= 0:
                return self.simple_right_rotation(root)

        if height_diff > 1:
            if self.get_balance(root.right) < 0:
                return self.right_left_rotation(root)


        if height_diff < -1:
            if self.get_balance(root.left) > 0:
                return self.left_right_rotation(root)
        return root


def delete(self, data: Any, mode: bool = True) -> bool:
        p, pad = self.search(data)
        if p is not None:
            if p.left is None and p.right is None:
                if p == pad.left:
                    pad.left = None
                else:
                    pad.right = None
                del p
            elif p.left is None and p.right is not None:
                if p == pad.left:
                    pad.left = p.right
                else:
                    pad.right = p.right
                del p
            elif p.left is not None and p.right is None:
                if p == pad.left:
                    pad.left = p.left
                else:
                    pad.right = p.left
                del p
            else:
                if mode:
                    pred, pad_pred, son_pred = self.__pred(p)
                    p.data = pred.data
                    if p == pad_pred:
                        pad_pred.left = son_pred
                    else:
                        pad_pred.right = son_pred
                    del pred
                else:
                    sus, pad_sus, son_sus = self.__sus(p)
                    p.data = sus.data
                    if p == pad_sus:
                        pad_sus.right = son_sus
                    else:
                        pad_sus.left = son_sus
                    del sus
            return True
        return False


        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        height_diff = self.get_balance(root)

        if height_diff > 1:
            if self.get_balance(root.left) >= 0:
                return self.simple_left_rotation(root)

        if height_diff <= 0:
           if self.get_balance(root.left) <= 0:
                return self.simple_right_rotation(root)

        if height_diff > 1:
            if self.get_balance(root.right) < 0:
                return self.right_left_rotation(root)


        if height_diff < -1:
            if self.get_balance(root.left) > 0:
                return self.left_right_rotation(root)
        return root




def get_balance(self, node):
    if not node:
            return 0
    return self.get_height(node.left) - self.get_height(node.right)

def simple_left_rotation(self, node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root

def simple_right_rotation(self, node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root


def left_right_rotation(self, node):
    node.left = self.simple_right_rotation(node.left)
    return self.simple_left_rotation(node)


def right_left_rotation(self, node):
    node.right = self.simple_left_rotation(node.right)
    return self.simple_right_rotation(node)



def search(self, data: Any) :
        p = self.root
        while p is not None:
            if data == p.data:
                return p
            else:
                if data < p.data:
                    p = p.left
                else:
                    p = p.right
        return p

def preorder(self) -> None:
        self.__preorder_r(self.root)

def __preorder_r(self, node: Optional["Node"]) -> None:
        if node is not None:
            self.__preorder_r(node.left)
            self.__preorder_r(node.right)



def search_list(self, data: Any, year, f_e) :
        lista_pelis = []
        p = self.root
        self.search_list_r(p.left, data, year, f_e, lista_pelis)

        if p.year == year & p.f_p > p.d_p & p.f_e > f_e:
                lista_pelis.append(p)

        self.search_list_r(p.right, data, year, f_e, lista_pelis)

        return lista_pelis

def __pred(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.left, node
        while p.right is not None:
            p, pad = p.right, p
        return p, pad, p.left

def __sus(self, node: "Node") -> Tuple["Node", "Node", Optional["Node"]]:
        p, pad = node.right, node
        while p.left is not None:
            p, pad = p.left, p
        return p, pad, p.right
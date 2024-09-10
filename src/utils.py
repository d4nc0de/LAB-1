def find_level(root, title, level=0):
    if not root:
        return -1
    if root.title == title:
        return level
    downlevel = find_level(root.left, title, level + 1)
    if downlevel != -1:
        return downlevel
    return find_level(root.right, title, level + 1)

def find_parent(root, title, parent=None):
    if not root:
        return None
    if root.title == title:
        return parent
    parent = root
    if title < root.title:
        return find_parent(root.left, title, parent)
    return find_parent(root.right, title, parent)

def find_grandparent(root, title):
    parent = find_parent(root, title)
    if parent:
        return find_parent(root, parent.title)
    return None

def find_uncle(root, title):
    parent = find_parent(root, title)
    grandparent = find_grandparent(root, title)
    if grandparent:
        if grandparent.left and grandparent.left.title == parent.title:
            return grandparent.right
        if grandparent.right and grandparent.right.title == parent.title:
            return grandparent.left
    return None

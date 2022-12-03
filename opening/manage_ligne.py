import opening.tree as tree

def get_node_ligne(ligne, parent):
    """
    input:
        -ligne : chess.Move list
        -parent : Node
    output:
        -Node
    Transform the chess.Move list into a tree
    """
    if len(ligne) == 1:
        return tree.Node(ligne[0], [parent], [])
    else:
        node_ligne = tree.Node(ligne[0], [parent], [])
        next_node = get_node_ligne(ligne[1:], node_ligne)
        node_ligne.childrens.append(next_node)
        return node_ligne

def add_ligne(tree, ligne):
    """
    input:
        -tree : Node
        -ligne : chess.Move list
    output:
        -node_ligne = Node
    add a ligne to the tree. Returns the part of the ligne
    that was really added -> the part that wasn't already
    in the tree
    """
    if len(ligne) > 0:
        flag = True
        for child in tree.childrens:
            if ligne[0] == child.move:
                flag = False
                add_ligne(child, ligne[1:])
                break
        if flag:
            node_ligne = get_node_ligne(ligne, tree)
            tree.childrens.append(node_ligne)
            return node_ligne

def clean_ligne(node):
    """
    input:
        -node : Node
    output:
        -None
    """
    similar_nodes = tree.get_similar_nodes(node)
    tree.link_nodes(similar_nodes)
    for child in node.childrens:
        clean_ligne(child)
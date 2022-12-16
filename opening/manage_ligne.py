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

def find_node(node, ligne):
    """
    input:
        -tree : Node class
        -ligne : chess.Move list
    output:
        -final_node : Node class or None
    return the last node corresponding to the ligne. If None
    the ligne is not in the tree
    """
    if node.move is None:
        for start_node in node.childrens:
            final_node = find_node(start_node, ligne[1:])
            if final_node is not None:
                return final_node
    else:
        if len(ligne) == 0:
            return node
        else:
            for next_node in node.childrens:
                if next_node.move == ligne[0]:
                    return find_node(next_node, ligne[1:])

def deleat_ligne(op_tree, ligne):
    end_node = find_node(op_tree, ligne)
    def aux(node):
        if node.parents is None:
            return None
        if len(node.parents) == 1 and len(node.childrens) == 0:
            node.parents[0].childrens.remove(node)
            aux(node.parents[0])
    aux(end_node)

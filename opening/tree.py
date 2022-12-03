import chess

class Node:

    def __init__(self, move, parents, childrens):
        self.move = move
        self.parents = parents
        self.childrens = childrens
    
    def add(self, move):
        """
        input:
            -self : opening.Node
            -move : chess.Move
        output:
            -None
        Add a children to the node and check if the position
        is already reach in another branch, if it is it links
        the children of the nodes together
        """
        next_node = Node(move, [self], [])
        self.childrens.append(next_node)
    
    def __repr__(self):
        if self.move is None:
            uci = None
        else:
            uci = self.move.uci()
        return f"{uci} : {self.childrens}"

def same_position(fen1, fen2):
    """
    input:
        -fen1 : str
        -fen2 : str
    output:
        -bool
    Check if two represent the same position
    """
    fen1 = "".join(fen1.split()[:-3])
    fen2 = "".join(fen2.split()[:-3])
    return fen1 == fen2

def get_root(node):
    """
    input:
        -node : opening.Node
    output:
        -node : opening.Node
    Gives the top Node of the tree
    """
    if node.parents is None:
        return node
    else:
        return get_root(node.parents[0])

def get_board(node):
    """
    input:
        -node : opening.Node
    output:
        -board : chess.Board
    """
    moves = []
    def aux(_node):
        if _node.move is not None:
            moves.append(_node.move)
            aux(_node.parents[0])
    aux(node)
    board = chess.Board()
    moves.reverse()
    for move in moves:
        board.push(move)
    return board

def get_similar_nodes(node):
    """
    input:
        -node : opening.Node
    output:
        - : Node list
    return the list of nodes which have the same position as
    node
    """
    fen = get_board(node).fen()
    root = get_root(node)
    similar_nodes = []
    def aux(_node, board):
        if _node.move is not None:
            board.push(_node.move)
        if same_position(board.fen(), fen):
            similar_nodes.append(_node)
        for child in _node.childrens:
            aux(child, chess.Board(fen=board.fen()))
    aux(root, chess.Board())
    return similar_nodes

def link_nodes(similar_nodes):
    """
    inputs:
        -similar_nodes : Node list
    output:
        -None
    Sum childrens and parents of the nodes in similar_nodes
    into two list and then assign those childrens and parents
    to each node
    """
    childrens = []
    parents = []
    for node in similar_nodes:
        for child in node.childrens:
            if child not in childrens:
                childrens.append(child)

        for parent in node.parents:
            if parent not in parents:
                parents.append(parent)
    
    for node in similar_nodes:
        node.childrens = childrens
        node.parents = parents

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
        return Node(ligne[0], [parent], [])
    else:
        node_ligne = Node(ligne[0], [parent], [])
        next_node = get_node_ligne(ligne[1:], node_ligne)
        node_ligne.childrens.append(next_node)
        return node_ligne

def add_ligne(tree, ligne):
    """
    input:
        -tree : Node
        -ligne : chess.Move list
    output:
        -None
    add a ligne to the tree
    """
    if len(ligne) > 0:
        flag = True
        for child in tree.childrens:
            if ligne[0] == child.move:
                flag = False
                add_ligne(child, ligne[1:])
        if flag:
            node_ligne = get_node_ligne(ligne, tree)
            tree.childrens.append(node_ligne)
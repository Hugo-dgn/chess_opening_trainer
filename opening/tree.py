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
    Sum childrens the nodes in similar_nodes
    into a list and then assign those childrens
    to each node
    """
    childrens = []
    for node in similar_nodes:
        for child in node.childrens:
            if child not in childrens:
                childrens.append(child)
    
    for node in similar_nodes:
        node.childrens = childrens
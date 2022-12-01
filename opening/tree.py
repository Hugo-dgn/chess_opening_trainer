import chess


def same_position(fen1, fen2):
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
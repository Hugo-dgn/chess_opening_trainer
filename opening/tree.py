import chess

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
        if board.move is not None:
            board.push(_node.move)
        if board.fen == fen:
            similar_nodes.append(node)
        else:
            for child in _node.children:
                aux(child, chess.Board(fen=board.fen))
    aux(root, chess.Board)
    return similar_nodes
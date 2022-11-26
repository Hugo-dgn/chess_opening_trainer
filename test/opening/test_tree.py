from opening import tree
import opening
import chess

def test_get_root():
    board = chess.Board()
    op_tree = opening.Node(None, None, [])


    moves = board.generate_legal_moves()
    op_tree.add(moves.__next__())
    op_tree.add(moves.__next__())

    move = moves.__next__()
    board.push(move)
    op_tree.add(move)

    op_tree.childrens[-1].add(moves.__next__())
    op_tree.childrens[-1].add(moves.__next__())
    op_tree.childrens[-1].add(moves.__next__())

    _op_tree = tree.get_root(op_tree.childrens[-1].childrens[0])

    assert _op_tree is op_tree

def test_get_board():
    board = chess.Board()
    op_tree = opening.Node(None, None, [])


    moves = board.generate_legal_moves()
    op_tree.add(moves.__next__())
    op_tree.add(moves.__next__())

    move_1 = moves.__next__()
    board.push(move_1)
    op_tree.add(move_1)

    moves = board.generate_legal_moves()
    op_tree.childrens[-1].add(moves.__next__())
    op_tree.childrens[-1].add(moves.__next__())

    move_2 = moves.__next__()
    board.push(move_2)
    op_tree.childrens[-1].add(move_2)

    _board = tree.get_board(op_tree.childrens[-1].childrens[-1])

    assert board.fen() == _board.fen()

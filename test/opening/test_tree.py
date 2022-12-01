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

def test_same_positon():
    fen1 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    fen2 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 2"
    fen3 = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 12 2"
    assert tree.same_position(fen1, fen2)
    assert tree.same_position(fen1, fen3)

def test_get_similar_nodes():
    board = chess.Board()
    op_tree = opening.Node(None, None, [])

    move_1_w_1 = chess.Move.from_uci("e2e4")
    move_2_w_1 = chess.Move.from_uci("e7e5")

    op_tree.add(move_1_w_1)
    op_tree.childrens[0].add(move_2_w_1)

    move_1_w_2 = chess.Move.from_uci("e2e3")
    move_2_w_2 = chess.Move.from_uci("e7e6")
    move_3_w_2 = chess.Move.from_uci("e3e4")
    move_4_w_2 = chess.Move.from_uci("e6e5")

    op_tree.add(move_1_w_2)
    op_tree.childrens[1].add(move_2_w_2)
    op_tree.childrens[1].childrens[0].add(move_3_w_2)
    op_tree.childrens[1].childrens[0].childrens[0].add(move_4_w_2)

    node = op_tree.childrens[1].childrens[0].childrens[0].childrens[0]

    similar_node = tree.get_similar_nodes(node)

    assert len(similar_node) == 2

    assertion_1_1 = similar_node[0] is op_tree.childrens[0].childrens[0]
    assertion_1_2 = similar_node[1] is op_tree.childrens[0].childrens[0]

    assertion_2_1 = similar_node[0] is op_tree.childrens[1].childrens[0].childrens[0].childrens[0]
    assertion_2_2 = similar_node[1] is op_tree.childrens[1].childrens[0].childrens[0].childrens[0]

    assert (assertion_1_1 or assertion_1_2)
    assert (assertion_2_1 or assertion_2_2)

def test_link_nodes():
    board = chess.Board()
    op_tree = opening.Node(None, None, [])

    move_1_w_1 = chess.Move.from_uci("e2e4")
    move_2_w_1 = chess.Move.from_uci("e7e5")
    move_3_w_1 = chess.Move.from_uci("a2e4")

    op_tree.add(move_1_w_1)
    op_tree.childrens[0].add(move_2_w_1)
    op_tree.childrens[0].childrens[0].add(move_3_w_1)

    move_1_w_2 = chess.Move.from_uci("e2e3")
    move_2_w_2 = chess.Move.from_uci("e7e6")
    move_3_w_2 = chess.Move.from_uci("e3e4")
    move_4_w_2 = chess.Move.from_uci("e6e5")

    op_tree.add(move_1_w_2)
    op_tree.childrens[1].add(move_2_w_2)
    op_tree.childrens[1].childrens[0].add(move_3_w_2)
    op_tree.childrens[1].childrens[0].childrens[0].add(move_4_w_2)

    node = op_tree.childrens[1].childrens[0].childrens[0].childrens[0]

    similar_nodes = tree.get_similar_nodes(node)

    assert len(op_tree.childrens[1].childrens[0].childrens[0].childrens[0].childrens) == 0
    tree.link_nodes(similar_nodes)
    assert len(op_tree.childrens[1].childrens[0].childrens[0].childrens[0].childrens) == 1
    assert op_tree.childrens[1].childrens[0].childrens[0].childrens[0].childrens is op_tree.childrens[0].childrens[0].childrens
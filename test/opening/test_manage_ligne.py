import opening
import opening.manage_ligne as ma_ligne
import chess

def test_get_node_ligne():
    op_tree = ma_ligne.get_node_ligne([chess.Move.from_uci("e2e4"),
                                    chess.Move.from_uci("e7e5")],
                                    None)
    assert op_tree.move.uci() == "e2e4"
    assert len(op_tree.childrens) == 1
    assert op_tree.childrens[0].move.uci() == "e7e5"
    assert len(op_tree.childrens[0].childrens) == 0

def test_add_ligne():
    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    node = ma_ligne.add_ligne(op.tree, moves)

    assert node.move.uci() == "e2e4"
    assert node.childrens[0].move.uci() == "e7e5"

    op_tree = op.tree.childrens[0]

    assert op_tree.move.uci() == "e2e4"
    assert len(op_tree.childrens) == 1
    assert op_tree.childrens[0].move.uci() == "e7e5"
    assert len(op_tree.childrens[0].childrens) == 0

def test_clean_ligne():
    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    ma_ligne.add_ligne(op.tree, moves)

    moves = [chess.Move.from_uci("e2e3"),
            chess.Move.from_uci("e7e6"),
            chess.Move.from_uci("e3e4"),
            chess.Move.from_uci("e6e5"),
            chess.Move.from_uci("a2a3")]
    
    node = ma_ligne.add_ligne(op.tree, moves)
    ma_ligne.clean_ligne(node)

    assert len(op.tree.childrens) == 2

    node_1 = op.tree.childrens[0].childrens[0]
    node_2 = op.tree.childrens[1].childrens[0].childrens[0].childrens[0]

    assert node_1.childrens is node_2.childrens

    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5"),
            chess.Move.from_uci("a2a3")]
    ma_ligne.add_ligne(op.tree, moves)

    moves = [chess.Move.from_uci("e2e3"),
            chess.Move.from_uci("e7e6"),
            chess.Move.from_uci("e3e4"),
            chess.Move.from_uci("e6e5"),
            ]
    
    node = ma_ligne.add_ligne(op.tree, moves)
    ma_ligne.clean_ligne(node)

    assert len(op.tree.childrens) == 2

    node_1 = op.tree.childrens[0].childrens[0]
    node_2 = op.tree.childrens[1].childrens[0].childrens[0].childrens[0]

    assert node_1.childrens is node_2.childrens

def test_find_node():
    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
                chess.Move.from_uci("e7e5")]
    op.add(moves)

    node = ma_ligne.find_node(op.tree, moves)

    assert node is op.tree.childrens[0].childrens[0]

def test_deleat_ligne():
    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    op.add(moves)

    ma_ligne.deleat_ligne(op.tree, moves)
    assert len(op.tree.childrens) == 0

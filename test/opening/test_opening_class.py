import opening
import chess

def test_add():
    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    op.add(moves)

    op_tree = op.tree.childrens[0]

    assert op_tree.move.uci() == "e2e4"
    assert len(op_tree.childrens) == 1
    assert op_tree.childrens[0].move.uci() == "e7e5"
    assert len(op_tree.childrens[0].childrens) == 0
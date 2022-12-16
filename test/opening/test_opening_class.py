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

    op = opening.Opening("caro", chess.BLACK)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    op.add(moves)

    moves = [chess.Move.from_uci("e2e3"),
            chess.Move.from_uci("e7e6"),
            chess.Move.from_uci("e3e4"),
            chess.Move.from_uci("e6e5"),
            chess.Move.from_uci("a2a3")]
    
    op.add(moves)

    assert len(op.tree.childrens) == 2

    node_1 = op.tree.childrens[0].childrens[0]
    node_2 = op.tree.childrens[1].childrens[0].childrens[0].childrens[0]

    assert node_1.childrens is node_2.childrens

def test_deleat():
	op = opening.Opening("caro", chess.BLACK)
	moves = [chess.Move.from_uci("e2e4"),
			chess.Move.from_uci("e7e5")]
	op.add(moves)

	op.deleat(moves)
	assert len(op.tree.childrens) == 0

	op = opening.Opening("caro", chess.BLACK)
	moves = [chess.Move.from_uci("e2e4"),
			chess.Move.from_uci("e7e5")]
	op.add(moves)

	moves = [chess.Move.from_uci("e2e4"),
			chess.Move.from_uci("e7e6"),
			chess.Move.from_uci("a2a4")]
	
	op.add(moves)

	op.deleat(moves)

	assert len(op.tree.childrens) == 1

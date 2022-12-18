import os

import chess

import manage
import opening

def test_delete_op():
    op = opening.Opening("test", True)
    opening.save(op)
    manage.delete_op("test")

    assert "test.op" not in os.listdir("data/")

def test_delete_ligne():
    op = opening.Opening("test", True)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    op.add(moves)

    manage.delete_ligne(op, moves)

    op_delete = opening.load("test")
    assert len(op_delete.tree.childrens) == 0

    os.remove("data/test.op")

def test_delete_last_move():
    op = opening.Opening("test", True)
    moves = [chess.Move.from_uci("e2e4"),
            chess.Move.from_uci("e7e5")]
    op.add(moves)

    manage.delete_last_move(op, moves)

    op_delete = opening.load("test")

    assert len(op_delete.tree.childrens) == 1
    assert op_delete.tree.childrens[0].move == chess.Move.from_uci("e2e4")
    assert len(op_delete.tree.childrens[0].childrens) == 0

    os.remove("data/test.op")
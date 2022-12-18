import opening
import os

def delete_op(name : str):
    os.remove(f"data/{name}.op")

def delete_ligne(op : opening.Opening, ligne : list):
    """
    input:
        -op : opening.Opening
        -ligne : chess.Move list
    output:
        -None
    delete an entire ligne from the opening
    """
    op.delete(ligne)
    opening.save(op)

def delete_last_move(op : opening.Opening, ligne : list):
    """
    input:
        -op : opening.Opening
        -ligne : chess.Move list
    output:
        -None
    delete an the last move of the ligne from the opening
    """
    op.delete(ligne)
    op.add(ligne[:-1])
    opening.save(op)
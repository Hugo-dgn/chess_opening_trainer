import explore
import os

def test_get_op():
    op_w = explore.get_op(True)
    op_b = explore.get_op(False)
    list_names = op_b + op_w
    list_names = [op.name+".op" for op in list_names]
    assert set(list_names) == set(os.listdir("data"))
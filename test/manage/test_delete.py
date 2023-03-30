import os

import manage
import opening

def test_delete_op():
    op = opening.Opening("test", True)
    opening.save(op)
    manage.delete_op("test")

    assert "test.op" not in os.listdir("data/")
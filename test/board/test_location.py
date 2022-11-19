from board.location import get_case_pos

def test_get_case_pos():
    x, y = get_case_pos(0, 1)
    assert (x, y) == (0.5, 7.5)

    x, y = get_case_pos(7, 1)
    assert (x, y) == (7.5, 7.5)

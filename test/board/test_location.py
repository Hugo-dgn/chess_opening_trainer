from board.location import get_case_pos, get_case_number

def test_get_case_pos():
    x, y = get_case_pos(0, 1)
    assert (x, y) == (0.5, 7.5)

    x, y = get_case_pos(7, 1)
    assert (x, y) == (7.5, 7.5)

def test_get_case_number():
    n = get_case_number(2, 31, 4)
    assert n == 0

    n = get_case_number(7, 31, 4)
    assert n == 1

import board.image as image

def test_get_rect_pieces():
    _path = "assets/"
    _pieces_rect = image.get_rect_pieces(_path+"pieces_rec.yaml")
    assert _pieces_rect["b"] == [400, 200, 600, 400]
import myfile

def test_large():
    assert myfile.calculate_area(10) > 50

def test_small():
    assert myfile.calculate_area(1) > 50

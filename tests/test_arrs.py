from utils import arrs

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"  # Вероятно, ожидается "test", если индекс -1 и за границами массива
    assert arrs.get([1, 2, 3], 5, "test") == "test"
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([], 0, "test") == "test"

def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -2, 4) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 1, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([1, 2, 3], 5) == []
    assert arrs.my_slice([1, 2, 3], 0, 5) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 5, 8) == []

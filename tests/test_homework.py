"""Test cases are important."""


from fun import homework


def test_greatest_number():
    assert homework.find_greatest_number([1, 2, 3, 4, 5, 6, 7, 8]) == 8
    assert homework.find_greatest_number([7, 3, 21, 4, 1, 6]) == 21


def test_least_number():
    assert homework.find_least_number([1, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert homework.find_least_number([8, 7, 3, 2, 4, 1, 6]) == 1


def test_sum_of_list():
    assert homework.add_list_numbers([1, 2, 3, 4]) == 10

def test_key_with_the_longest_value():
    assert homework.get_key_with_longest_value("dog": "cat", "a": "asdfasdfasdfasdfasdf") == "a"

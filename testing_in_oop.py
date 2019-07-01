class ToBeTested:

    def add(self, a, b):
        return a + b

    def make_string_upper(self, string):
        return string.upper()

# tbt = ToBeTested()

def test_add_both_positive():
    tbt = ToBeTested()
    assert tbt.add(1,2) == 3

def test_make_string_upper_take_lowercase_string():
    tbt = ToBeTested()
    assert tbt.make_string_upper('heja') == 'HEJA'

#ex59_testing_oop.py

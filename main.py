import pytest

values = {'I': 1,'V':5,'X':10,'L':50,'C':100}
special_value = {'IV':4}
# Source Code:

def from_roman(roman: str) -> int:
  if roman in special_value:
    number = special_value[roman]
  else:
    number = sum(values[ch] for ch in roman)
  return number



# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('V', 5),
  ('IV', 4),
  L
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman


# Good thing
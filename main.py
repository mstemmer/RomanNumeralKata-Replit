import pytest

values = {'I': 1}

# Source Code:

def from_roman(roman: str) -> int:
  number = sum(values[ch] for ch in roman)
  return number



# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman

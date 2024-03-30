import pytest 
from pytest import approx
from example import miles_per_gallon
def test_miles_per_gallon():
    assert miles_per_gallon(1030, 2010, 30) == approx(32.67,abs=0.01)
pytest.main(["-v", "--tb=line", "-rN",__file__])
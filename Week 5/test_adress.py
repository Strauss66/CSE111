from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("6778 Berula Cir,West Jordan, Utah 84081") == "West Jordan"

def test_extract_state():
    assert extract_state("6778 Berula Cir,West Jordan, Utah 84081") == "Utah"

def test_extract_zipcode():
    assert extract_zipcode("6778 Berula Cir,West Jordan, Utah 84081") == "84081"
pytest.main(["-v", "--tb=line", "-rN", __file__])
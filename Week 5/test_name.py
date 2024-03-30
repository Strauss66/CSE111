from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest
def test_make_full():
    assert make_full_name("", "") == ";"
    assert make_full_name("Jorge", "Uganda") == "Uganda;Jorge"
    assert make_full_name("Johan", "Guerrero") == "Guerrero;Johan"
    assert make_full_name("Roy","Garcia") == "Garcia;Roy"
def test_extract_family_name():
    assert extract_family_name("Garcia; Roy") == "Garcia"
    assert extract_family_name("Guerrero; Johan") == "Guerrero"
    assert extract_family_name("Uganda; Jorge") == "Uganda"
def test_extract_given_name():
    assert extract_given_name("Garcia/ Roy") == "Roy"
    assert extract_given_name("Guerrero/ Johan") == "Johan"
    assert extract_given_name("Uganda/ Jorge") == "Jorge"
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
import Date
import pytest

def test_isvalid():
    d1=Date.Date(5,12,2020)
    assert d1.isvalid()!=0
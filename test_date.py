import Date
import pytest
d1=Date.Date(5,12,2020)
d2=Date.Date(6,12,2020)
def test_isvalid():
    assert d1.isvalid()!=0
def test_getNextDay():
    bool=True
    if ((d1._day + 1) != d2._day) and (d1._month!=d2._month) and (d1._year!=d2._year):
        bool==False
    else: bool=True
    assert  bool==True

daysToAdd=5
@pytest.fixture
def getNextDays(daysToAdd):
    return d1.getNextDays(daysToAdd)

def test_getNextDays(d1,getNextDays):
    assert d1._day+daysToAdd==getNextDays
@pytest.fixture
def _eq(d2):
    if d1.__eq__(d2)==True:
        return 1
def test_eq():
    assert _eq==1





import dict
import pytest
import numpy

data_set = {
    "1232": {"sex": "female", "age": 57, "ID": 17681, "name": "ziad"}
}
def test_split_male_female():
    for details in data_set.values():
     assert details["sex"]=='female'
def test_find_median_average():
    for details in data_set.values():
        age=details["age"]
    assert  numpy.mean(age)==57
def test_print_values_above():
    dict.print_values_above(7)
    for k in data_set.keys():
        age=k["age"]
    assert age>7




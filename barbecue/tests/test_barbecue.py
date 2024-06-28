import pytest

from barbecue import sample_function
from barbecue import Barbecue

@pytest.fixture
def Barbecue_object():
    obj = Barbecue()
    return obj

def test_Barbecue_instance_has_sample_method(Barbecue_object):
    assert hasattr(Barbecue_object, "sample_method")

def test_barbecue_has_sample_function():
    assert sample_function() is None  # no return value

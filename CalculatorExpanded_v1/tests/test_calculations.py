from webbrowser import Opera

import pytest
from calculations import Operations

@pytest.fixture()
def setup_operations():
    oper = Operations()
    yield oper

def test_add_positive(setup_operations):
    assert 5 == setup_operations.add(2,3)

def test_add_positive_negative(setup_operations):
    assert -1 == setup_operations.add(2,-3)

def test_add_negative(setup_operations):
    assert -5 == setup_operations.add(-2,-3)

def test_add_fractions(setup_operations):
    assert 1 == setup_operations.add(1/2, 1/2)

def test_sub_positive(setup_operations):
    assert 5 == setup_operations.sub(10,5)

def test_sub_positive_negative(setup_operations):
    assert 15 == setup_operations.sub(10,-5)

def test_sub_negative(setup_operations):
    assert -5 == setup_operations.sub(-10,-5)

def test_sub_fractions(setup_operations):
    assert -1/10 == setup_operations.sub(1/10,1/5)

def test_mul_positive(setup_operations):
    assert 25 == setup_operations.mul(5,5)

def test_mul_positive_negative(setup_operations):
    assert -25 == setup_operations.mul(5,-5)

def test_mul_negative(setup_operations):
    assert 25 == setup_operations.mul(-5,-5)

@pytest.mark.xfail
def test_mul_fractions(setup_operations):
    assert 1/25 == setup_operations.mul(1/5,1/5)


def test_div_zero(setup_operations):
    with pytest.raises(ZeroDivisionError):
        setup_operations.div(5,0)

def test_div_positive(setup_operations):
    assert 5 == setup_operations.div(10,2)

def test_div_positive_negative(setup_operations):
    assert -5 == setup_operations.div(10,-2)

def test_div_negative(setup_operations):
    assert 5 == setup_operations.div(-10,-2)

def test_div_fractions(setup_operations):
    assert 1/5 == setup_operations.div(1/10,1/2)


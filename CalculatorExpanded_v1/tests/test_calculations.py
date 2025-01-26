import pytest
from calculations import Operations

def test_add_positive():
    oper = Operations()
    assert 5 == oper.add(2,3)

def test_add_positive_negative():
    oper = Operations()
    assert -1 == oper.add(2,-3)

def test_add_negative():
    oper = Operations()
    assert -5 == oper.add(-2,-3)

def test_add_fractions():
    oper = Operations()
    assert 1 == oper.add(1/2, 1/2)

def test_sub_positive():
    oper = Operations()
    assert 5 == oper.sub(10,5)

def test_sub_positive_negative():
    oper = Operations()
    assert 15 == oper.sub(10,-5)

def test_sub_negative():
    oper = Operations()
    assert -5 == oper.sub(-10,-5)

def test_sub_fractions():
    oper = Operations()
    assert -1/10 == oper.sub(1/10,1/5)

def test_mul_positive():
    oper = Operations()
    assert 25 == oper.mul(5,5)

def test_mul_positive_negative():
    oper = Operations()
    assert -25 == oper.mul(5,-5)

def test_mul_negative():
    oper = Operations()
    assert 25 == oper.mul(-5,-5)

@pytest.mark.xfail
def test_mul_fractions():
    oper = Operations()
    assert 1/25 == oper.mul(1/5,1/5)


def test_div_zero():
    oper = Operations()
    with pytest.raises(ZeroDivisionError):
        oper.div(5/0)

def test_div_positive():
    oper = Operations()
    assert 5 == oper.div(10,2)

def test_div_positive_negative():
    oper = Operations()
    assert -5 == oper.div(10,-2)

def test_div_negative():
    oper = Operations()
    assert 5 == oper.div(-10,-2)

def test_div_fractions():
    oper = Operations()
    assert 1/5 == oper.div(1/10,1/2)


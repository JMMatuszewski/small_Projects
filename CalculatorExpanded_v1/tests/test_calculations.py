from webbrowser import Opera

import pytest
from calculations import Operations
from main import Calculator


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


@pytest.mark.parametrize("data_str,result", [([5,'+',5],10),([5,'-',5],0),([1,'+',2,'-',3,'+',4,'-',5,'+',6],5) ] )
def test_calc_str(data_str,result):
    oper = Operations()
    assert result == oper.calc_str(data_str)

@pytest.mark.parametrize("data_str,result", [
    ([1,'+',2,'*',3],[1,'+',6]),
    ([1,'+',4,'/',2],[1,'+',2]),
    ([6,'/',3,'-',2,'*',3,'-',5,'+',6],[2,'-',6,'-',5,'+',6]),
    ([2,'/',2,'+',2,'/',2,'+',2,'/',2,'+',2,'/',2,'+',2,'/',2],[1,'+',1,'+',1,'+',1,'+',1])
    ])
def test_order(data_str,result):
    oper = Operations()
    assert result == oper.order(data_str)


# @pytest.mark.xfail
@pytest.mark.parametrize("data_str,result", [
    ([5,'*','(',5,'+',5,')'],50),
    (['(',6,'/','(',2,'+',1,')','+',1,')'],3),
    (['(','(','(',5,'+',5,')','*',4,')','/',2,')'],20)
    ])
def test_parenthesis(data_str,result):
    oper = Operations()
    res,skip = oper.parenthesis(data_str)
    assert result == res
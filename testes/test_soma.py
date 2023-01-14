from src.classes import Ops, Error
import pytest

@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 2), (3, 2, 5)])

def test_soma(op1, op2, res_esp):
    somador = Ops()
    result = somador.soma(op1, op2)
    assert result == res_esp

def test_somaDecimal():
    somador = Ops()
    with pytest.raises(Error):
        somador.soma(4.3,1)

def test_somaString():
    somador = Ops()
    with pytest.raises(Error):
        somador.soma("4", 1)


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 0), (3, 2, 1)])

def test_sub(op1, op2, res_esp):
    sub = Ops()
    result = sub.sub(op1, op2)
    assert result == res_esp


@pytest.mark.parametrize("op1, op2, res_esp", [(1, 1, 1), (3, 2, 6)])

def test_multi(op1,op2,res_esp):
    mult = Ops()
    result = mult.multi(op1,op2)
    assert result == res_esp

def test_multiZero():
    multi = Ops()
    with pytest.raises(Error):
        multi.multi(0,1)


@pytest.mark.parametrize("op1, op2, res_esp", [(10, 2, 5), (4, 2, 2)])

def test_div(op1, op2, res_esp):
    div = Ops()
    result = div.div(op1, op2)
    assert result == res_esp

def test_divZero():
    div = Ops()
    with pytest.raises(Error):
        div.div(3,0)




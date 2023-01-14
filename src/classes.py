import numbers

class Error(Exception):
    pass


class Ops:
    def soma(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 + op2

    def sub(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        return op1 - op2

    def div(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        self._check_div_(op1)
        self._check_div_(op2)
        return op1/op2

    def multi(self, op1, op2):
        self._check_int_(op1)
        self._check_int_(op2)
        self._check_div_(op1)
        self._check_div_(op2)
        return op1*op2

    def _check_int_(self, op):
        if not isinstance(op, numbers.Integral) or op < 0:
            raise Error(f"{op} n eh inteiro!!!!")

    def _check_div_(self, op):
        if op == 0:
            raise Error(f"{op} n pode fazer essas ops por 0!!!!")



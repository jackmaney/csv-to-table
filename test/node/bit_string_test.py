from node.bit_string import VarBitNode, BitNode
from nose.tools import ok_, eq_


def test_varbit_node():

    v = VarBitNode('vb', n=8)

    eq_(v.n, 8, "Length checks out")

    short = "b'1001'"
    at_length = "B'00110101'"
    too_big = "B'1111001111'"
    wtf = "asdfasdfa"

    fn = v.indicator_function

    ok_(fn(short), "Bit strings shorter than 'n' work")
    ok_(fn(at_length), "Bit strings of length 'n' work")
    ok_(not fn(too_big), "Bit strings that are too big fail")
    ok_(not fn(wtf), "Non-bitstrings fail")

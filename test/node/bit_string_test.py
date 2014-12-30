from nose.tools import eq_, ok_

from node.bit_string_node import BitNode, VarBitNode


def test_varbit_node():

    v = VarBitNode('vb', n=8)

    eq_(v.n, 8, "Length checks out")

    short = "b'1001'"
    at_length = "B'00110101'"
    too_big = "B'1111001111'"
    wtf = "asdfasdfa"

    ok_(v.indicator_function(short), "Bit strings shorter than 'n' work")
    ok_(v.indicator_function(at_length), "Bit strings of length 'n' work")
    ok_(not v.indicator_function(too_big), "Bit strings that are too big fail")
    ok_(not v.indicator_function(wtf), "Non-bitstrings fail")


def test_bit_node():

    b = BitNode('b', n=12)

    eq_(b.n, 12, "Length checks out")

    short = "b'1001'"
    at_length = "B'001101011100'"
    too_big = "B'1111001111111111'"
    wtf = "asdfasdfa"

    ok_(not b.indicator_function(short), "Bit strings shorter than 'n' fail")
    ok_(b.indicator_function(at_length), "Bit strings of length 'n' work")
    ok_(not b.indicator_function(too_big), "Big strings that are too big fail")
    ok_(not b.indicator_function(wtf), "Non-bitstrings fail")

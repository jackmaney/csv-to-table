from nose.tools import ok_, eq_

from node.text_node import VarCharNode, CharNode

n = 8
too_short = "abcdef"
too_long = "banana banana banana"
just_right = "pendulum"
number = 2.71818

v = VarCharNode(n=n)
c = CharNode(n=n)


def test_varchar_node_basic():

    ok_(v.n == n, "n checks out")
    ok_(v.indicator_function(too_short), "Shorter than n is okay")
    ok_(v.indicator_function(just_right), "At length is okay")
    ok_(not v.indicator_function(too_long),
        "Rejects strings that are too long")
    ok_(not v.indicator_function(number), "Rejects numbers")


def test_varchar_change_n():

    v.n = 7
    eq_(v.name, "varchar(7)", "Varchar name changed")
    ok_(v.indicator_function(too_short), "still short enough...")
    ok_(not v.indicator_function(just_right), "8 is too big for new n")


def test_char_node():

    ok_(c.n == n, "n checks out")
    ok_(not c.indicator_function(too_short), "Rejects too short")
    ok_(c.indicator_function(just_right), "At length is okay")
    ok_(not c.indicator_function(too_long),
        "Rejects strings that are too long")
    ok_(not c.indicator_function(number), "Rejects numbers")


def test_char_change_n():

    c.n = 6

    eq_(c.name, "char(6)", "Char name changed")
    ok_(c.indicator_function(too_short), "too_short is now just right")
    ok_(not c.indicator_function(just_right), "8 is now too big")
    ok_(not c.indicator_function("abc"), "3 is too small")

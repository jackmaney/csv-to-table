from nose.tools import ok_
from nose import with_setup

from node.text_node import VarCharNode, CharNode

n = 8
too_short = "abcdef"
too_long = "banana banana banana"
just_right = "pendulum"
number = 2.71818


def test_varchar_node():

    v = VarCharNode("varchar", n=n)

    ok_(v.n == n, "n checks out")
    ok_(v.indicator_function(too_short), "Shorter than n is okay")
    ok_(v.indicator_function(just_right), "At length is okay")
    ok_(not v.indicator_function(too_long),
        "Rejects strings that are too long")
    ok_(not v.indicator_function(number), "Rejects numbers")


def test_char_node():

    c = CharNode("char", n=n)

    ok_(c.n == n, "n checks out")
    ok_(not c.indicator_function(too_short), "Rejects too short")
    ok_(c.indicator_function(just_right), "At length is okay")
    ok_(not c.indicator_function(too_long),
        "Rejects strings that are too long")
    ok_(not c.indicator_function(number), "Rejects numbers")

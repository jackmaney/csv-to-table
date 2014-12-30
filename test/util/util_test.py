from nose.tools import ok_

from node.node import Node
from util import is_int, is_numeric, is_string


def test_is_string():

    ok_(is_string("some string"), "Strings are okay")
    ok_(not is_string(1), "Numbers are not okay")
    ok_(not is_string(Node("node_name")), "Non-string objects are not okay")


def test_is_numeric():

    ok_(is_numeric(123.45), "Numbers are okay")
    ok_(is_numeric(-21), "Integers are okay")
    ok_(is_numeric("345.17"), "String representations of numbers are okay")
    ok_(is_numeric("6"), "String representations of ints are okay")
    ok_(not is_numeric("abc"),
        "Strings that don't cast to numbers are not okay")
    ok_(not is_numeric(Node("butters")),
        "Non-number, non-string objects are not okay")


def test_is_int():

    ok_(is_int(221), "Integers are okay")
    ok_(not is_int(2.71828), "Non-int numbers are not okay")
    ok_(is_int("11"), "String representations of ints are okay")
    ok_(not is_int("1.24"),
        "String representations of non-int numbers are not okay")
    ok_(not is_int(Node("blarg")),
        "Non-number, non-string objects are not okay")

from nose.tools import eq_, ok_

from node.numeric_node import IntRangeNode, NumericRangeNode


def test_bad_nodes():

    bad_numeric = False
    bad_int = False

    try:
        NumericRangeNode('numeric', lower=1.23, upper=-2.001)
    except:
        bad_numeric = True

    ok_(bad_numeric, "Can't create NumericRangeNodes with lower > upper")

    try:
        IntRangeNode('int', lower=1, upper=-2)
    except:
        bad_int = True

    ok_(bad_int, "Can't create IntRangeNodes with lower > upper")



def test_int_range_node():

    int_range_node = IntRangeNode('int_range', lower=0, upper=10)

    too_low = -1
    too_high = 15
    just_right = 5
    wtf = 'hurr durr!'

    eq_(int_range_node.lower, 0, "Lower checks out")
    eq_(int_range_node.upper, 10, "Upper checks out")

    ok_(not int_range_node.indicator_function(too_low),
        "Kept out numbers that are too low")
    ok_(not int_range_node.indicator_function(too_high),
        "Kept out numbers that are too high")
    ok_(int_range_node.indicator_function(just_right),
        "Keep in numbers between the range")
    ok_(not int_range_node.indicator_function(wtf),
        "Reject things that aren't numbers")


def test_numeric_range_node():

    num_range_node = NumericRangeNode('nrange', lower=-3.1, upper=2.71828)

    too_low = -4.5
    too_high = 3
    just_right = 1 + 1e-5
    wtf = "blarg"

    eq_(num_range_node.lower, -3.1, "Lower checks out")
    eq_(num_range_node.upper, 2.71828, "Upper checks out")

    ok_(not num_range_node.indicator_function(too_low),
        "Kept out numbers that are too low")
    ok_(not num_range_node.indicator_function(too_high),
        "Kept out numbers that are too high")
    ok_(num_range_node.indicator_function(just_right),
        "Keep in numbers between the range")
    ok_(not num_range_node.indicator_function(wtf),
        "Reject things that aren't numbers")

from nose.tools import eq_, ok_

from node.boolean_node import BooleanNode


def test_boolean_node():

    node = BooleanNode('boolean')

    eq_(set(node.values), set(["TRUE", "FALSE"]), "Values are okay")
    ok_(node.indicator_function("TRUE") and
        node.indicator_function("FALSE"), "The given values are okay")
    ok_(not node.indicator_function("true"), "Case sensitive!")
    ok_(not node.indicator_function("foo"),
        "Things not in `values` are not okay")

from nose.tools import ok_

from node.json_node import JSONNode


def test_json_node():

    j = JSONNode(name="json")

    ok_(not j.indicator_function(2), "Non-strings are not okay")
    ok_(j.indicator_function("3.1415926"),
        "String representations of numbers are okay")
    ok_(not j.indicator_function("I like bananas"),
        "Bare strings are not okay")
    ok_(j.indicator_function("[2.718, \"foobar\"]"), "Arrays are okay")

    obj_str = "{\"a\":3, \"b\":{\"c\":7, \"d\":\"blarg\"}}"
    ok_(j.indicator_function(obj_str), "Objects are okay")

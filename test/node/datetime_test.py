from nose.tools import ok_

from node.datetime_node import DateNode, DateTimeNode, TimeNode


def test_date_node():

    d = DateNode("date")

    ok_(not d.indicator_function(0), "Numbers not okay")
    ok_(not d.indicator_function("foobar"), "Non-date strings not okay")
    ok_(d.indicator_function("2014-12-30"), "YYYY-MM-DD okay")
    ok_(d.indicator_function("11/23/1984"), "MM/DD/YYYY okay")
    ok_(not d.indicator_function("2014-08-12 11:52:31"),
        "Timestamps that are not dates are not okay")


def test_datetime_node():

    dt = DateTimeNode("timestamp without time zone")

    ok_(not dt.indicator_function(0), "Numbers not okay")
    ok_(not dt.indicator_function("foobar"), "Non-timestamp strings not okay")
    ok_(dt.indicator_function("2014-12-30"), "YYYY-MM-DD dates okay")
    ok_(dt.indicator_function("11/23/1984"), "MM/DD/YYYY dates okay")
    ok_(dt.indicator_function("2014-08-12 11:52:31"),
        "Timestamps that are not dates are okay")


def test_time_node_basic():

    t = TimeNode()

    ok_(not t.indicator_function(0), "Numbers not okay")
    ok_(not t.indicator_function("blarg"), "Non-time strings not okay")
    ok_(t.indicator_function("22:12:59"), "Time string okay")
    ok_(not t.indicator_function("22:38:72"), "Fails if seconds are too big")


def test_time_node_min_max():

    t = TimeNode(minimum="00:00:00", maximum="24:00:00")

    ok_(t.indicator_function("10:22:43"), "Regular time string okay")
    ok_(not t.indicator_function("25:12:23"), "Too big fails")
    ok_(not t.indicator_function("-5:12:02"), "Too small fails")


def test_time_node_multiple_separators():

    t = TimeNode(separator=[":", "."])

    ok_(t.indicator_function("13:22:29"), "Colons okay")
    ok_(t.indicator_function("18.22.59"), "Periods okay")

from nose.tools import ok_

from node.datetime_node import DateNode, DateTimeNode


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

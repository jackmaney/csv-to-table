from nose.tools import ok_

from node.uuid_node import UUIDNode


def test_uuid_node():

    uuid = "123e4567-e89b-12d3-a456-426655440000"
    also_ok = "123e4567e89b12d3a456426655440000"
    not_hex = "123e4567-e89b-12d3-a456-42q65544g000"
    too_short = "123e4567-e89b-12d3-a46-426655440"
    too_long = "123e4567e89b12d3a456426655440000deadbeef"

    n = UUIDNode("uuid")

    ok_(n.indicator_function(uuid), "Accepts normal UUID")
    ok_(n.indicator_function(also_ok), "Dashes are optional")
    ok_(not n.indicator_function(not_hex), "Rejects non-hex strings")
    ok_(not n.indicator_function(too_short),
        "Rejects UUIDs that are too short")
    ok_(not n.indicator_function(too_long),
        "Rejects strings that are too long")

from nose.tools import ok_

from node.network_node import InetNode, CidrNode, MacAddressNode


def test_inet_node():

    good_range = "191.1.0.0/8"
    ip = "123.221.0.201"
    bad_ip = "256.1.12.29"
    wtf = "banana banana banana"
    ipv6_range = "fd0d:ff3f:6cf7:2f70::/64"
    ipv6 = "fd0d:ff3f:6cf7:2f70:dead:beef:1123:4567"

    n = InetNode("inet")

    ok_(n.indicator_function(good_range), "Ranges okay")
    ok_(n.indicator_function(ip), "IP addresses okay")
    ok_(not n.indicator_function(bad_ip), "Picks up bad IPs")
    ok_(not n.indicator_function(wtf), "Rejects bad strings")
    ok_(n.indicator_function(ipv6_range), "IPv6 ranges okay")
    ok_(n.indicator_function(ipv6), "IPv6 addresses okay")


def test_cidr_node():

    good_range = "191.0.0.0/8"
    bad_range = "191.1.0.0/8"
    bad_ip = "1.2.3.256"
    wtf = "asdf"
    ipv6_range = "fd0d:ff3f:6cf7:2f70:dead:beef::/96"

    n = CidrNode("cidr")

    ok_(n.indicator_function(good_range), "Correct range checks out")
    ok_(not n.indicator_function(bad_range), "Bad range fails")
    ok_(not n.indicator_function(bad_ip), "Bad IP fails")
    ok_(not n.indicator_function(wtf), "Rejects bad strings")
    ok_(n.indicator_function(ipv6_range), "IPv6 ranges okay")


def test_mac_address_node():

    good_mac = "01:23:45:67:89:ab"
    bad_mac = "01:23:45:67:89:ag"
    wtf = "blarg"

    n = MacAddressNode("mac")

    ok_(n.indicator_function(good_mac), "Good MAC addresses accepted")
    ok_(not n.indicator_function(bad_mac), "Bad MAC addresses rejected")
    ok_(not n.indicator_function(wtf), "Bad strings rejected")

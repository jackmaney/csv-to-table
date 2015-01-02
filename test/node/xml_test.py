from nose.tools import ok_

from node.xml_node import XMLNode


def test_xml_node():
    xml = '<root><a>3</a><b class="asdf">17</b></root>'
    not_xml = "banana banana banana"
    number = 2

    x = XMLNode("xml")

    ok_(x.indicator_function(xml), "XML is okay")
    ok_(not x.indicator_function(not_xml), "Non-XML is not okay")
    ok_(not x.indicator_function(number), "Numbers are not okay")

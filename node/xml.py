from node import Node
from util import is_string
import xml.etree.ElementTree as ET


def is_xml(x):

    if not is_string(x):
        return False

    try:
        ET.fromstring(x)
        return True
    except:
        return False


class XMLNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(XMLNode, self).__init__(
            name, indicator_function=is_xml, parent=parent, children=children
        )

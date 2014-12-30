import xml.etree.ElementTree as ET

from node import Node
from util import is_string


class XMLNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            ET.fromstring(field)
            return True
        except:
            return False

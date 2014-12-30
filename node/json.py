from json import loads

from node import Node
from util import is_string


class JSONNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            loads(field)
            return True
        except:
            return False

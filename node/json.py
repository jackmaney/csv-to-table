from node import Node
from json import loads
from util import is_string


def is_json(x):

    if not is_string(x):
        return False

    try:
        loads(x)
        return True
    except:
        return False


class JSONNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(JSONNode, self).__init__(
            name, indicator_function=is_json, parent=parent, children=children
        )

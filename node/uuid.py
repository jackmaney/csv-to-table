from node import Node
from util import is_string
from uuid import UUID


def is_uuid(x):

    if not is_string(x):
        return False

    try:
        UUID(x)
        return True
    except:
        return False


class UUIDNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(InetNode, self).__init__(
            name, indicator_function=is_uuid, parent=parent, children=children
        )

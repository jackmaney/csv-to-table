from node import Node
from util import is_string
from netaddr import IPNetwork, EUI


def is_inet(x):

    if not is_string(x):
        return False

    try:
        IPNetwork(x)
        return True
    except:
        return False


def is_cidr(x):

    if not is_string(x):
        return False

    try:
        return x == str(IPNetwork(x).cidr)
    except:
        return False


def is_mac_address(x):

    if not is_string(x):
        return False

    try:
        EUI(x)
        return True
    except:
        return False


# TODO: I think this can all be refactored with metaclasses. Look into that...

class InetNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(InetNode, self).__init__(
            name, indicator_function=is_inet, parent=parent, children=children
        )


class CidrNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(CidrNode, self).__init__(
            name, indicator_function=is_cidr, parent=parent, children=children
        )


class MacAddressNode(Node):

    def __init__(self, name, parent=None, children=[]):

        super(MacAddressNode, self).__init__(
            name, indicator_function=is_mac_address, parent=parent,
            children=children
        )

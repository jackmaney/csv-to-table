from netaddr import EUI, IPNetwork
from node import Node
from util import is_string


class InetNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            IPNetwork(field)
            return True
        except:
            return False


class CidrNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            return field == str(IPNetwork(field).cidr)
        except:
            return False


class MacAddressNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            EUI(field)
            return True
        except:
            return False

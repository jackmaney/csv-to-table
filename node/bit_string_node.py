import re

from node import Node
from util import is_int


class VarBitNode(Node):

    def __init__(self, name, n, parent=None, children=[]):

        self.n = n

        super(VarBitNode, self).__init__(name, parent=parent,
                                         children=children)

    def _validate_params(self):

        super(VarBitNode, self)._validate_params()

        if not is_int(self.n) or self.n <= 0:
            raise ValueError("The 'n' parameter must be a positive integer")

    def indicator_function(self, field):

        pattern = "^[bB]'([01]+)'$"
        # TODO: Take account of bit strings in hex form
        # This requires converting to a string of 0's and 1's.
        # Not seeing any convenient method to do that, so I'll
        # roll my own

        # pattern = "^B'([01]+)'$|^X'([0-9a-fA-F]+)'$"

        match = re.match(pattern, field)

        return match and match.groups() and len(match.groups()[0]) <= self.n

    def __eq__(self, other):

        return super(VarBitNode, self).__eq__(other) and self.n == other.n

    def __ne__(self, other):

        return not self.__eq__(other)


class BitNode(VarBitNode):

    def indicator_function(self, field):

        pattern = "^[bB]'([01]+)'$"
        # TODO: Take account of bit strings in hex form
        # This requires converting to a string of 0's and 1's.
        # Not seeing any convenient method to do that, so I'll
        # roll my own

        # pattern = "^B'([01]+)'$|^X'([0-9a-fA-F]+)'$"

        match = re.match(pattern, field)

        return match and match.groups() and len(match.groups()[0]) == self.n

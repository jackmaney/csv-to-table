from node import Node
from util import is_int, is_string


class VarCharNode(Node):

    def __init__(self, name, n, parent=None, children=[]):

        self.n = n
        super(VarCharNode, self).__init__(name, parent=parent,
                                          children=children)

    def _validate_params(self, name, parent, children, n):
        super(VarCharNode, self)._validate_params(name, parent, children)

        if not is_int(self.n) or self.n <= 0:
            raise ValueError("The 'n' parameter must be a positive integer")

    def indicator_function(self, field):

        return is_string(field) and len(field) <= self.n

    def __eq__(self, other):

        return super(VarCharNode, self).__eq__(other) and self.n == other.n

    def __ne__(self, other):

        return not self.__eq__(other)


class CharNode(VarCharNode):

    def __init__(self, name, n, parent=None, children=[]):

        self.n = n

        super(VarCharNode, self).__init__(name, parent=parent,
                                          children=children)

    def indicator_function(self, field):

        return is_string(field) and len(field) == self.n

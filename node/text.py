from node import Node
from util import is_int, is_string


class VarCharNode(Node):

    def __init__(self, name, n, parent=None, children=[]):

        indicator_function = lambda x: is_string(x) and len(x) <= n

        super(VarCharNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

        self.n = n

    def _validate_params(self, name, indicator_function, parent, children, n):
        super(VarCharNode, self)._validate_params(
            name, indicator_function, parent, children
        )

        if not is_int(n) or n <= 0:
            raise ValueError("The 'n' parameter must be a positive integer")

    def __eq__(self, other):

        return super(VarCharNode, self).__eq__(other) and self.n == other.n

    def __ne__(self, other):
        return not self.__eq__(other)


class CharNode(VarCharNode):

    def __init__(self, name, n, parent=None, children=[]):

        indicator_function = lambda x: is_string(x) and len(x) == n

        super(VarCharNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

        self.n = n

from node import Node
from util import is_string


class BooleanNode(Node):

    def __init__(self, name, values=["TRUE", "FALSE"],
                 parent=None, children=[]):

        self.values = values

        super(BooleanNode, self).__init__(name, parent=parent,
                                          children=children)

    def _validate_params(self, name, parent, children):

        super(BooleanNode, self)._validate_params(name, parent, children)

        if not isinstance(self.values, list):
            raise ValueError("The 'values' parameter must be a list!")

        for value in self.values:
            if not is_string(value):
                raise ValueError(
                    "The 'values' list contains a non-string element: %s" %
                    str(value))

    def indicator_function(self, field):

        return is_string(field) and field in self.values

    def __eq__(self, other):

        return super(BooleanNode, self).__eq__(other) and \
            set(self.values) == set(other.values)

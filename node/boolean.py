from node import Node
from util import is_string


class BooleanNode(Node):

    def __init__(self, name, values=["TRUE", "FALSE"],
                 parent=None, children=[]):

        indicator_function = lambda x: x in values

        super(BooleanNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children
        )

        self.values = values

    def _validate_params(self, name, indicator_function, parent,
                         children, values):

        super(BooleanNode, self)._validate_params(
            name, indicator_function, parent, children
        )

        if not isinstance(values, list):
            raise ValueError("The 'values' parameter must be a list!")

        for value in values:
            if not is_string(value):
                raise ValueError(
                    "The 'values' list contains a non-string element: %s" %
                    str(value))

    def __eq__(self, other):

        return super(BooleanNode, self).__eq__(other) and \
            set(self.values) == set(other.values)

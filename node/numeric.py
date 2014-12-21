from node import Node
from util import is_int, is_numeric


def range_indicator_function(f, lower, upper):
    return lambda x: f(x) and lower <= x and x <= upper


class NumericRangeNode(Node):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        indicator_function = range_indicator_function(is_numeric, lower, upper)

        self.lower = lower
        self.upper = upper

        super(NumericRangeNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

    def _validate_params(self, name, indicator_function, parent, children):
        super(NumericRangeNode, self)._validate_params(
            name, indicator_function, parent, children)

        if not is_numeric(self.lower) or not is_numeric(self.upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if self.lower >= self.upper:
            raise ValueError("'lower' must be less than 'upper'")

    def __eq__(self, other):

        return super(NumericRangeNode, self).__eq__(other) and \
            self.lower == other.lower and self.upper == other.upper

    def __ne__(self, other):
        return not self.__eq__(other)


class IntRangeNode(NumericRangeNode):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        indicator_function = range_indicator_function(is_int, lower, upper)

        self.lower = lower
        self.upper = upper

        super(NumericRangeNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

    def _validate_params(self, name, indicator_function, parent, children):
        super(NumericRangeNode, self)._validate_params(
            name, indicator_function, parent, children)

        if not is_int(self.lower) or not is_int(self.upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if self.lower >= self.upper:
            raise ValueError("'lower' must be less than 'upper'")

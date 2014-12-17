from node import Node
from util import is_int, is_numeric, range_indicator_function


class NumericRangeNode(Node):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        indicator_function = range_indicator_function(is_numeric, lower, upper)

        super(NumericRangeNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

        self.lower = lower
        self.upper = upper

    def _validate_params(self, name, indicator_function, parent, children,
                         lower, upper):
        super(self.__class__, self)._validate_params(
            name, indicator_function, parent, children)

        if not is_numeric(lower) or not is_numeric(upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if lower >= upper:
            raise ValueError("'lower' must be less than 'upper'")

    def __eq__(self, other):

        return super(NumericRangeNode, self).__eq__(other) and \
            self.lower == other.lower and self.upper == other.upper

    def __ne__(self, other):
        return not self.__eq__(other)


class IntRangeNode(NumericRangeNode):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        indicator_function = range_indicator_function(is_int, lower, upper)

        super(NumericRangeNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

        self.lower = lower
        self.upper = upper

    def _validate_params(self, name, indicator_function, parent, children,
                         lower, upper):
        super(self.__class__, self)._validate_params(
            name, indicator_function, parent, children)

        if not is_int(lower) or not is_int(upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if lower >= upper:
            raise ValueError("'lower' must be less than 'upper'")

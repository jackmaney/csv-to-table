from node import Node
from util import is_int, is_numeric


def range_indicator_function(f, lower, upper):
    return lambda x: f(x) and lower <= x and x <= upper


class NumericRangeNode(Node):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        self.lower = lower
        self.upper = upper

        super(NumericRangeNode, self).__init__(name, parent=parent,
                                               children=children)

    def _validate_params(self):
        super(NumericRangeNode, self)._validate_params()

        if not is_numeric(self.lower) or not is_numeric(self.upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if self.lower >= self.upper:
            raise ValueError("'lower' must be less than 'upper'")

    def indicator_function(self, field):
        return range_indicator_function(is_numeric,
                                        self.lower, self.upper)(field)

    def __eq__(self, other):

        return super(NumericRangeNode, self).__eq__(other) and \
            self.lower == other.lower and self.upper == other.upper

    def __ne__(self, other):
        return not self.__eq__(other)


class IntRangeNode(NumericRangeNode):

    def __init__(self, name, lower, upper, parent=None, children=[]):

        self.lower = lower
        self.upper = upper

        super(NumericRangeNode, self).__init__(
            name, parent=parent, children=children)

    def _validate_params(self):
        super(NumericRangeNode, self)._validate_params()

        if not is_int(self.lower) or not is_int(self.upper):
            raise ValueError(
                "The 'lower' and 'upper' parameters must be numeric")

        if self.lower >= self.upper:
            raise ValueError("'lower' must be less than 'upper'")

    def indicator_function(self, field):
        return range_indicator_function(is_int, self.lower, self.upper)(field)


class SmallIntNode(IntRangeNode):

    def __init__(self, name="smallint", lower=-32768, upper=32767,
                 parent=None, children=[]):

        super(SmallIntNode, self).__init__(name, lower=lower, upper=upper,
                                           parent=parent, children=children)


class IntegerNode(IntRangeNode):

    def __init__(self, name="int", lower=-2147483648, upper=2147483647,
                 parent=None, children=[]):

        super(IntegerNode, self).__init__(name, lower=lower, upper=upper,
                                          parent=parent, children=children)


class BigIntNode(IntRangeNode):

    def __init__(self, name="bigint", lower=-9223372036854775808,
                 upper=9223372036854775807, parent=None, children=[]):

        super(BigIntNode, self).__init__(name, lower=lower, upper=upper,
                                         parent=parent, children=children)

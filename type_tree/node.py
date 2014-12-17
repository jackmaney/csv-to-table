import numbers

import six


def is_int(n):
    return isinstance(n, numbers.Integral)


def is_numeric(x):
    return isinstance(x, numbers.Real)


def is_string(x):
    return isinstance(x, six.string_types)


def range_indicator_function(f, lower, upper):
    return lambda x: f(x) and lower <= x and x <= upper


class Node(object):

    def __init__(self, name, indicator_function=None,
                 parent=None, children=[]):

        self._validate_params(name, indicator_function, parent, children)

        self.name = name
        self.indicator_function = indicator_function
        self.parent = parent
        self.children = children

    def _validate_params(self, name, indicator_function, parent, children):

        if not name or not is_string(name):
            raise ValueError("The 'name' parameter must be a non-empty string")

        if indicator_function is not None and \
                not hasattr(indicator_function, "__call__"):
            raise ValueError(
                """The 'indicator_function' must either be None or a function"""
                )

        if parent is not None and not isinstance(parent, Node):
            raise ValueError("The 'parent' must be None or a Node")

        if isinstance(children, list):
            for child in children:
                if not isinstance(child, Node):
                    raise ValueError("Every child must be a Node!")
        else:
            raise ValueError("'children' must be a list of Nodes!")

    def __eq__(self, other):
        """
        Since these nodes are supposed to represent data types, we will
        consider two nodes to be the same iff their names are the same.
        """
        if not isinstance(other, self.__class__):
            return False

        return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)


class NumericRangeNode(Node):

    def __init__(self, name, lower, upper, indicator_function=None,
                 parent=None, children=[]):

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

    def __init__(self, name, lower, upper, indicator_function=None,
                 parent=None, children=[]):

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

        return super(VarCharNode, self).__eq__(other) and \
            self.n == other.n

    def __ne__(self, other):
        return not self.__eq__(other)


class CharNode(VarCharNode):

    def __init__(self, name, n, parent=None, children=[]):

        indicator_function = lambda x: is_string(x) and len(x) == n

        super(VarCharNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children)

        self.n = n

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

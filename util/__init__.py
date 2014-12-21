import numbers
import six


def is_string(x):
    return isinstance(x, six.string_types)


def is_int(n):

    if is_string(n):
        try:
            n = int(n)
        except:
            return False

    return isinstance(n, numbers.Integral)


def is_numeric(x):

    if is_string(x):
        try:
            x = float(x)
        except:
            return False

    return isinstance(x, numbers.Real)

from node import Node
from util import is_int, is_string


class VarCharNode(Node):

    def __init__(self, n=None, name="varchar",
                 prefix="varchar", parent=None, children=[],
                 use_prefix_in_name=True):

        self.use_prefix_in_name = use_prefix_in_name
        self.prefix = prefix
        self.n = n

        if n is None:
            use_prefix_in_name = False

        if self.use_prefix_in_name:
            name = prefix + "(" + str(n) + ")"

        super(VarCharNode, self).__init__(name, parent=parent,
                                          children=children)

    def _validate_params(self, name, parent, children):
        super(VarCharNode, self)._validate_params(name, parent, children)

        if self.n is not None and not is_int(self.n) or self.n <= 0:
            raise ValueError(
                "The 'n' parameter, if given, must be a positive integer")

    def __setattr__(self, name, value):

        if name == "n":
            if value is not None and self.use_prefix_in_name:
                if not is_int(value) or value <= 0:
                    msg = "The 'n' parameter, if given,"
                    msg += " must be a positive integer"
                    raise ValueError(msg)
                self.name = "%s(%s)" % (self.prefix, str(value))

        object.__setattr__(self, name, value)

    def indicator_function(self, field):

        if self.n is not None:
            return is_string(field) and len(field) <= self.n
        else:
            return is_string(field)

    def __eq__(self, other):

        return super(VarCharNode, self).__eq__(other) and self.n == other.n

    def __ne__(self, other):

        return not self.__eq__(other)


class CharNode(VarCharNode):

    def __init__(self, n, name="char",
                 prefix="char", parent=None, children=[]):

        super(CharNode, self).__init__(n=n, name=name, prefix=prefix,
                                       parent=parent, children=children,
                                       use_prefix_in_name=True)

    def indicator_function(self, field):

        return is_string(field) and len(field) == self.n

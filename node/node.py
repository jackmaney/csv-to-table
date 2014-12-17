from util import is_string


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

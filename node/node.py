from util import is_string


class Node(object):

    def __init__(self, name, parent=None, children=[]):

        self.name = name
        self.parent = parent
        self.children = children

        self._validate_params()


    def _validate_params(self):

        if not self.name or not is_string(self.name):
            raise ValueError("The 'name' parameter must be a non-empty string")

        if self.parent is not None and not isinstance(self.parent, Node):
            raise ValueError("The 'parent' must be None or a Node")

        if isinstance(self.children, list):
            for child in self.children:
                if not isinstance(child, Node):
                    raise ValueError("Every child must be a Node!")
        else:
            raise ValueError("'children' must be a list of Nodes!")

    def indicator_function(self, field):
        return True

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

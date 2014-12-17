from dateutil.parser import parse

from node import Node


# TODO: Add more functionality around time zones.


class DateTimeNode(Node):

    def __init__(self, name, parent=None, children=[]):

        def indicator_function(dt):
            try:
                parse(dt)
                return True
            except:
                return False

        super(DateTimeNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children
        )


class DateNode(Node):

    def __init__(self, name, parent=None, children=[]):

        def indicator_function(dt):
            try:
                parsed = parse(dt)
                return (parsed.hour, parsed.minute, parsed.second) == (0, 0, 0)
            except:
                return False

        super(DateNode, self).__init__(
            name, indicator_function=indicator_function, parent=parent,
            children=children
        )

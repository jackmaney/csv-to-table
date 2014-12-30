from dateutil.parser import parse

from node import Node
from util import is_string


# TODO: Add more functionality around time zones.


class DateTimeNode(Node):

    def indicator_function(self, field):
        if not is_string(field):
            return False

        try:
            parse(field)
            return True
        except:
            return False


class DateNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            parsed = parse(field)
            return (parsed.hour, parsed.minute, parsed.second) == (0, 0, 0)
        except:
                return False

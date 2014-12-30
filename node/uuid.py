from uuid import UUID

from node import Node
from util import is_string


class UUIDNode(Node):

    def indicator_function(self, field):

        if not is_string(field):
            return False

        try:
            UUID(field)
            return True
        except:
            return False

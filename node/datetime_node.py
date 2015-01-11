from dateutil.parser import parse

from node import Node
from util import is_string

import re

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


class TimeNode(Node):

    def __init__(self, name="time",
                 separator=":",
                 minimum=None, maximum=None,
                 parent=None, children=[]):

        self.minimum = minimum
        self.maximum = maximum
        self.separator = separator

        super(TimeNode, self).__init__(name, parent=parent, children=children)

    def _time_str_to_list(self, field):

        if is_string(self.separator):
            sep_pattern = re.escape(self.separator)
        else:
            sep_pattern = "|".join([re.escape(x) for x in self.separator])

        # Now, re.escape isn't perfect...it escapes colons. Which is bad.
        sep_pattern.replace("\\:", ":")

        return [int(x) for x in re.split(sep_pattern, field)]

    def _validate_params(self):

        super(TimeNode, self)._validate_params()

        if not is_string(self.separator):
            if not isinstance(self.separator, list):
                raise ValueError(
                    "The separator parameter must be a string or list of strings!")
            else:
                for sep in self.separator:
                    if not is_string(sep):
                        raise ValueError(
                            "Non-string found in separator list: %s" % sep)

        for i, param in enumerate([self.minimum, self.maximum]):

            if param is None:
                continue

            name = "minimum"

            if i == 1:
                name = "maximum"

            if not is_string(param):
                msg = "The %s parameter must be a string (got %s)" % (
                    name, param)
                raise ValueError(msg)

            if not self._check_time_string(param):
                msg = "Cannot parse the %s parameter: '%s'" % (name, param)
                raise ValueError(msg)

        if self.minimum is not None and self.maximum is not None:
            if self._time_str_to_list(self.minimum) > \
                    self._time_str_to_list(self.maximum):

                raise ValueError(
                    "Minimum (%s) is larger than maximum (%s)" % (
                        self.minimum, self.maximum))

    def _check_time_string(self, field):
        # Refactoring this out of both the _validate_params and
        # indicator_function methods, since it's needed in both
        # places.
        # Since I'm trying to figure out if the minimum and maximum
        # parameters are okay in _validate_params, I can't use
        # indicator_function for that, since that depends on
        # maximum and minimum.

        try:
            split = self._time_str_to_list(field)

            if len(split) != 3:
                return False

            if split[1] not in range(60) or split[2] not in range(60):
                return False
        except:
            return False

        return True

    def indicator_function(self, field):
        if not is_string(field):
            return False

        if not self._check_time_string(field):
            return False

        split = self._time_str_to_list(field)

        if self.minimum is not None:
            if split < self._time_str_to_list(self.minimum):
                return False

        if self.maximum is not None:
            if split > self._time_str_to_list(self.maximum):
                return False

        return True

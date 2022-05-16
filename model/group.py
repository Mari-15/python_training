from sys import maxsize


class Group:

    def __init__(self, number_of_group=None, name=None, header=None, footer=None):
        self.number_of_group = number_of_group
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "%s:%s" % (self.number_of_group, self.name)

    def __eq__(self, other):
        return (self.number_of_group is None or other.number_of_group is None
                or self.number_of_group == other.number_of_group) \
               and self.name == other.name

    def id_or_max(self):
        if self.number_of_group:
            return int(self.number_of_group)
        else:
            return maxsize

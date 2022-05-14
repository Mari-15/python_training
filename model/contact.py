from sys import maxsize


class Contact:

    def __init__(self, number_of_contact=None, name=None, patronymic=None, surname=None, nick=None, title=None,
                 comp_name=None, comp_address=None, home_number=None,
                 mobile_number=None, work_number=None, fax=None, email1=None, email2=None,
                 day_Birth=None, month_Birth=None, year_Birth=None):
        self.number_of_contact = number_of_contact
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.nick = nick
        self.title = title
        self.comp_name = comp_name
        self.comp_address = comp_address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.day_Birth = day_Birth
        self.month_Birth = month_Birth
        self.year_Birth = year_Birth

    def __repr__(self):
        return "%s: %s %s" % (self.number_of_contact, self.surname, self.name)

    def __eq__(self, other):
        return (self.number_of_contact is None or other.number_of_contact is None
                or self.number_of_contact == other.number_of_contact) \
               and self.surname == other.surname and self.name == other.name

    def id_or_max(self):
        if self.number_of_contact:
            return int(self.number_of_contact)
        else:
            return maxsize

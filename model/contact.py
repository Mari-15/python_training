from sys import maxsize


class Contact:

    def __init__(self, number_of_contact=None, name=None, patronymic=None, surname=None, nick=None, title=None,
                 comp_name=None, comp_address=None, home_number=None, id=None,
                 mobile_number=None, work_number=None, fax=None, phone2=None, email1=None, email2=None, email3=None,
                 day_Birth=None, month_Birth=None, year_Birth=None, all_phones_from_homepage=None, all_emails=None):
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
        self.phone2 = phone2
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.day_Birth = day_Birth
        self.month_Birth = month_Birth
        self.year_Birth = year_Birth
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails = all_emails

    def __repr__(self):
        return "%s: %s, %s; %s; %s; %s" % (self.number_of_contact, self.surname, self.name, self.comp_address, self.all_emails, self.all_phones_from_homepage)

    def __eq__(self, other):
        return (self.number_of_contact is None or other.number_of_contact is None
                or self.number_of_contact == other.number_of_contact) \
               and self.surname == other.surname and self.name == other.name \
               and (self.comp_address is None or other.comp_address is None
                or self.comp_address == other.comp_address)

    def id_or_max(self):
        if self.number_of_contact:
            return int(self.number_of_contact)
        else:
            return maxsize

from model.contact import Contact
import random
import string

constant = [
    Contact(name='Vasilii', surname='Petrov', comp_name='Groupd+', home_number='00000000000'),
    Contact(name='Petr', surname='Osipov', patronymic='Iosivofich', comp_address='Green Street')
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numbers(prefix, maxlen):
    symbols = '+' + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name=random_string('name', 5), surname=random_string('surname', 10),
                    comp_address=random_string('address', 10), comp_name=random_string('com_name', 7),
                    email1=random_string('email', 7), email2=random_string('email2', 7),
                    home_number=random_numbers('home', 11), work_number=random_numbers('work', 11))
            for i in range(2)]
from model.contact import Contact
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(name=random_string('name', 5), surname=random_string('surname', 5), nick="VasiliiParovoz", title="Vasilii Parovoz",
            comp_name='OOO "GoodPeopleComp"', comp_address="The USA, Green str, apt 654",
            home_number="8-800-999-45-45", mobile_number="+7(921)456-45-45", work_number="+7(921)456-45-45",
            fax="8-800-999-45-45", email1="testVasili@mail.ru", email2="test2@mail.ru",
            email3="test3@mail.ru", day_Birth="15", month_Birth="June",
            year_Birth="1975")
]



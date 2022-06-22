from model.group import Group
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=random_string('name', 5), header=random_string('header', 5), footer='footer1')
]
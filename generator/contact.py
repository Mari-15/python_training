from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


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
            for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
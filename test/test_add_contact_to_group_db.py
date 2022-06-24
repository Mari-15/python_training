import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture


db1 = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_add_contact_to_group_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Lost7one'))
        app.navigation.return_to_homepage()
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db1.get_contacts_not_in_group(Group(number_of_group=group.number_of_group))) == 0:
        app.contact.create(Contact(name="Land", surname="Und"))
    contacts = db1.get_contacts_not_in_group(Group(number_of_group=group.number_of_group))
    contact = random.choice(contacts)
    contact_in_group_old = db1.get_contacts_in_group(Group(number_of_group=group.number_of_group))
    app.contact.add_some_contact_to_group(group_name=group.name, id1=contact.number_of_contact)
    contact_in_group_old.append(contact)
    contact_in_group_new = db1.get_contacts_in_group(Group(number_of_group=group.number_of_group))
    assert sorted(contact_in_group_old, key=Contact.id_or_max) == sorted(contact_in_group_new, key=Contact.id_or_max)



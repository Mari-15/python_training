from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
db1 = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_remove_some_contact_from_group(app, db):
    def clean(group):
        return Group(number_of_group=group.number_of_group, name=group.name.strip(), header=group.header.strip(), footer=group.footer.strip())
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Lost one'))
        app.navigation.return_to_homepage()
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = list(map(clean,db.get_group_list()))
    group = random.choice(groups)
    contact_in_group_old = db1.get_contacts_in_group(Group(number_of_group=group.number_of_group))
    if contact not in contact_in_group_old:
        app.group.show_all_contacts()
        app.contact.add_some_contact_to_group(group_name=group.name, id1=contact.number_of_contact)
        contact_in_group_old = db1.get_contacts_in_group(Group(number_of_group=group.number_of_group))
    app.contact.remove_first_contact_from_group(group_name=group.name, id1=contact.number_of_contact)
    contact_in_group_old.remove(contact)
    contact_in_group_new = db1.get_contacts_in_group(Group(number_of_group=group.number_of_group))
    assert sorted(contact_in_group_old, key=Contact.id_or_max) == sorted(contact_in_group_new, key=Contact.id_or_max)

from model.contact import Contact


def test_delete_all_contacts(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="Roland", surname="Braund"))
        app.contact.create(Contact(name="Voland", surname="Round"))
    old_contacts = db.get_contact_list()
    app.delete.all_contacts()
    assert len(old_contacts) > app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts = []
    assert old_contacts == new_contacts

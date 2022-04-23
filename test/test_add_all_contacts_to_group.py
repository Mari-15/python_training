def test_add_all_contacts_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_all_contacts_to_group(group_name="New one")
    app.session.logout()

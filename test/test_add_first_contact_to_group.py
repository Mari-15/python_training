def test_add_first_contact_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_first_contact_to_group(group_name="New one")
    app.session.logout()

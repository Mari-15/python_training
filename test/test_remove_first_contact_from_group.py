def test_remove_first_contact_from_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.remove_first_contact_from_group(group_name="New one")
    app.session.logout()

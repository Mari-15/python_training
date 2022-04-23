def test_add_first_contact_to_group(app):
    app.session.login(username="admin", password="secret")
    app.modify.add_first_contact_to_group(group_name="Test1")
    app.session.logout()

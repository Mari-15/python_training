def test_add_all_contacts_to_group(app):
    app.session.login(username="admin", password="secret")
    app.modify.add_all_contacts_to_group(group_name="Test2")
    app.session.logout()

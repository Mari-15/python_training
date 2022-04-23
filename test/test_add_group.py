# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(number_of_group=None, name="New one", header="Test2", footer="group for test"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(number_of_group=None, name="", header="", footer=""))
    app.session.logout()

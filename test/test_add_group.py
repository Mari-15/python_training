# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="New one", header="Test2", footer="group for test"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
    app.navigation.return_to_homepage()

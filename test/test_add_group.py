# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test2", header="Test2", footer="group for test"))
    app.session.logout()


def test_add_empty_group(app):
    pytest.skip()
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

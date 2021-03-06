# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.groups import testdata



def test_add_group0812(app, db, json_groups):
    group = json_groups
    old_group = db.get_group_list()
    app.group.create(group)
    #assert len(old_group) + 1 == app.group.count()
    new_group = db.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)





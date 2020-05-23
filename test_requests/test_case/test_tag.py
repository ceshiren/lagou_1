import json

import pytest
import yaml

from test_requests.api.base_api import BaseApi
from test_requests.api.tag import Tag


class TestTag:
    tag = Tag()
    test_data = tag.load('test_tag.data.yaml')

    @classmethod
    def setup_class(cls):
        data = cls.tag.get()
        for name in ["add demo"]:
            tag_id = cls.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                print(name)
                cls.tag.delete(tag_id=tag_id[0])

    def setup(self):
        pass

    @pytest.mark.parametrize("name_old, name_new", test_data)
    def test_all(self, name_old, name_new):

        data = self.tag.get()
        for name in [name_old, name_new]:
            tag_id = self.tag.jsonpath(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                print(name)
                self.tag.delete(tag_id[0])

        assert self.tag.add(name_old)['errcode'] == 0
        tag_id = self.tag.jsonpath(self.tag.get(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update(tag_id, name_new)['errcode'] == 0

    def test_get(self):
        assert self.tag.get()['errcode'] == 0

    def test_add(self):
        assert self.tag.add(tag_name="add demo")['errcode'] == 0

    def test_delete(self):
        name="add demo"
        assert self.tag.add(tag_name=name)['errcode'] == 0
        tag_id = self.tag.jsonpath(self.tag.get(), f'$..tag[?(@.name=="{name}")].id')[0]
        print(Tag().delete(tag_id=tag_id))

    def test_update(self):
        print(Tag().update('etQKd-CgAAE6Zdmx89xoc_LYuIyLWwNw', 'wangwu'))

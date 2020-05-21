import json

import yaml
from jsonpath import jsonpath

from test_requests.api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_all(self):
        tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')
        if tag_id:
            self.tag.delete(tag_id[0])
        self.tag.add("wangwu")
        tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')[0]
        self.tag.update(tag_id, "hahaha")

    def test_get(self):
        print(json.dumps(Tag().get(),indent=2))

    def test_delete(self):
        print(Tag().delete('etQKd-CgAAI70aMYm4j37aJyTo0EMRmw'))

    def test_update(self):
        print(Tag().update('etQKd-CgAAE6Zdmx89xoc_LYuIyLWwNw', 'wangwu'))

from pprint import pprint

import yaml

from test_requests.api.base_api import BaseApi


def test_load():
    with open("test_tag.data.yaml", 'r') as f:
        pprint(yaml.safe_load(f))


def test_template():
    print(BaseApi.template("../api/tag.add.yaml", {"token": "123", "tag_name": "demo"}))

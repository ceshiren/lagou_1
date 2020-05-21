from test_requests.api.base_api import BaseApi
from test_requests.api.wework import WeWork


class Tag(BaseApi):
    secrete = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'

    def __init__(self):
        self.token = WeWork().get_token(self.secrete)

    def add(self, tag_name):
        data = {
            "method": "post",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "test",
                "tag": [{"name": tag_name}]
            }
        }
        return self.send_api(data)

    def get(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": []
            }
        }

        return self.send_api(data)

    def delete(self, tag_id):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        return self.send_api(data)

    def update(self, tag_id, name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {

                "id": tag_id,
                "name": name
            }
        }
        return self.send_api(data)

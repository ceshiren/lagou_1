import requests

from test_requests.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = 'wwd6da61649bd66fea'

    # 获取 token
    def get_token(self, secrete):
        data = {
            "method": "get",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            "params": {
                "corpid": self.corpid,
                "corpsecret": secrete
            }

        }
        return self.send_api(data)['access_token']

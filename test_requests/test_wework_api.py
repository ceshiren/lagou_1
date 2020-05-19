import requests


class TestWeworkApi:
    secrete = 'C7uGOrNyxWWzwBsUyWEbLUlJOWjU7Qw5ORPxemPKw6w'
    id = 'wwd6da61649bd66fea'

    def setup(self):
        res = requests.get(
            f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.id}&corpsecret={self.secrete}')
        self.token = res.json()['access_token']

    def test_wework_api(self):
        # 获取成员
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=wangwu222')
        if r.json()['errcode'] == 0:
            r = requests.get(
                f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=wangwu222')
            print(r.json())

        create_data = {
            'userid': 'wangwu222',
            'name': 'wangwu212',
            'mobile': '13261993378',
            "department": [1]

        }
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=' + self.token,
                          json=create_data)
        print(r.json())

        data = {
            'userid': 'wangwu222',
            'name': 'zhangsan123456'
        }

        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=' + self.token, json=data)
        print(r.json())

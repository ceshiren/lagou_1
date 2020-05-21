import requests


class BaseApi:
    def send_api(self, req:dict):
        # 使用 request 完成多请求的改造（post, get, delete）
        return requests.request(**req).json()

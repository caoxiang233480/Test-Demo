# -*- coding: utf-8 -*-

import requests

"""封装一个发送请求的类"""


class handleRequest:
    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法大写同一转成程小写
        method = method.lower()
        if method == "get":
            return requests.get(url=url, params=params)
        elif method == "post":
            return requests.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return requests.patch(url=url, json=json, data=data, headers=headers)


class HandleSessionRequest:
    """session鉴权的接口使用此类发送请求"""

    def __init__(self):
        self.se = requests.session()

    def send(self, url, method, params=None, data=None, json=None, headers=None):
        # 将请求的方法大写同一转成程小写
        method = method.lower()
        if method == "get":
            return self.se.get(url=url, params=params)
        elif method == "post":
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == "patch":
            return self.se.patch(url=url, json=json, data=data, headers=headers)


token_http = handleRequest()
cookie_http = HandleSessionRequest()

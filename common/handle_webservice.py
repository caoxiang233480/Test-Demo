# -*- coding: utf-8 -*-

import suds
from suds.client import Client


class webrequests():

    def requests(self, url, interface, data):
        ws = Client(url)
        # 根据接口名称获取请求方法
        requests_method = getattr(ws.service, interface)
        try:
            # 传入参数访问该接口
            res = requests_method(data)
        except suds.WebFault as e:
            return (dict(e.fault))
        else:
            return dict(res)


wbs = webrequests()

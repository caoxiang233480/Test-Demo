# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 10:29
# @File    : handle_data.py
# @Software: PyCharm


import re
from common.myconfig import conf

class testdata:
    """专门存放要替换数据的"""
    member_id = ""



def replace_data(data):
    s=r"#(.+?)#"
    while re.search(s,data):
        # 匹配第一个待替换的数据,返回的是对象
        res=re.search(s,data)
        # 提取待替换的内容
        item=res.group()
        # 获取替换内容中的数据项
        key=res.group(1)
        try:
            data=data.replace(item,conf.get("url_project",key))
        except:
            data=data.replace(item,getattr(testdata,key))
    return data


if __name__=='__main__':
    setattr(testdata, "member_id", str(4789))
    data = ' {"amount":10000}'
    data = replace_data(data)
    print(data)
    # data = '{"mobile_phone":"#user#","pwd":"#pwd#","user":#user#}'
    # data=replace_data(data)
    # print(data)
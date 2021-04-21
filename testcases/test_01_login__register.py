# -*- coding: utf-8 -*-
import unittest
import random
from library.ddt import ddt, data
from common.readexcel import read_excel
from common.contants import URL_DIR
from common.myconfig import conf
from common.handle_request import token_http, cookie_http
from common.mylogger import Log
from common.handle_db import db


# -----------------------------示例代码----------------------------------------


@ddt
class Testregister(unittest.TestCase):
    excel = read_excel(URL_DIR, "register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self, case):
        # ------第一步：准备用例数据------------
        # 请求的参数
        # 增加判断
        if "#phone#" in case["data"]:
            # 生成手机号
            phone = self.random_phone()
            # 进行替换
            case["data"] = case["data"].replace("#phone#", phone)
        data = eval(case["data"])
        # 请求的方法
        method = case["method"]
        # 请求的地址
        url = conf.get("url_project", "url") + case["url"]
        # 当前用例所在行
        row = case["case_id"] + 1
        # 请求头(配置文件中读取请求头)
        headers = eval(conf.get("url_project", "headers"))
        # 预期结果
        expected = eval(case["expected"])

        # ------第二步：发送请求到接口，获取实际结果--------
        res1 = token_http.send(url=url, method=method, json=data, headers=headers)
        res = res1.json()

        # -------第三步：比对预期结果和实际结果-----
        try:
            self.assertEqual(eval(expected["code"]), res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            if res["msg"] == "ok":
                # 去数据库查询当前账号是否存在
                sql = "SELECT * FROM futureloan.member WHERE mobile_phone ={}".format(phone)
                # 获取数据库中有没有该用户信息
                count = self.db.count(sql)
                # 对数据库中返回的数据做断言，判断数据库中是否有一条数据
                self.assertEqual(1, count)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            print("预期结果：{}".format(expected))
            print("实际结果;{}".format(res))
            Log.info("用例：{}--------->未通过".format(case["title"]))
            Log.error(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            Log.info("用例：{}--------->通过".format(case["title"]))

    @staticmethod
    def random_phone():
        phone = "188"
        for i in range(8):
            phone += str(random.randint(0, 9))
        return phone

# -*- coding: utf-8 -*-

import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.myconfig import conf
from common.contants import REPORTS_DIR, CASE_DIR, REPORTS_DIR2
from library.BeautifulReport import BeautifulReport
from common.send_email import send_msg

# 第一步创建测试套件"""一定记得后面带括号（）""""
suite = unittest.TestSuite()
# 加载用例到套件

loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

# ——————————————第二种模块加载测试用例类的方式-------------------------------------------------
# 第2种，通过模块去加载用例
# 创建一个加载对象
# import testcases  #导入模块
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(testcases))


# 配置文件修改报告名称
res = conf.get("report", "filename")
dir = os.path.join(REPORTS_DIR, res)

with open(dir, "wb") as f:
    runner = HTMLTestRunner(stream=f,
                            title="接口测试报告",
                            description="测试报告的描述信息",
                            tester="测试人员"
                            )
    # 第四步：运行测试套件
    runner.run(suite)

# 方式二：生成测试报告
# runner=HTMLTestRunner(stream=open(r"D:\pycharm\test_project\reports\reports.html","wb"),tester="空城",description="进阶3",title="用例报告")
# runner.run(suite)
#
# """生成第二种测试报告样式"""
# result = BeautifulReport(suite)
# result.report(filename='测试报告', description='注册登录函数测试', log_path=REPORTS_DIR2)


# 执行完代码之后，发送邮件报告报告需要自己在配置文件中去写入收件人邮箱，以及send_email绑定自己发件人邮箱
# 不会配置的注释下行代码
# send_msg(dir)

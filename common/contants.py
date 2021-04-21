# -*- coding: utf-8 -*-

import os

"""该模块用来处理项目路径"""

res = os.path.dirname(__file__)
BASEDIR = os.path.dirname(res)

"""linux服务器上的路径处理方法,如果运行的时候报路径错误，就用这种方法"""
# dir=os.path.abspath(__file__)
# dir1=os.path.dirname(dir)
# BASEDIR=os.path.dirname(dir1)
# # 报告名称动态改
# res=conf.get("report","filename")
# print(res)

# 配置文件路径
CONF_DIR = os.path.join(BASEDIR, "conf/conf.ini")
# 用例数据目录
URL_DIR = os.path.join(BASEDIR, "data/cases.xlsx")
# 日志目录
LOG_DIR = os.path.join(BASEDIR, "log/log.log")
# 测试报告目录
REPORTS_DIR = os.path.join(BASEDIR, "reports")
# 用例模块
CASE_DIR = os.path.join(BASEDIR, "testcases")
REPORTS_DIR2 = os.path.join(BASEDIR, "reports")
# print(REPORTS_DIR2)


WEB = os.path.join(BASEDIR, "data\webservice_cases.xlsx")

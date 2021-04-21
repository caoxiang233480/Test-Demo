# -*- coding: utf-8 -*-


import logging
from logging.handlers import TimedRotatingFileHandler
from common.contants import LOG_DIR
from common.myconfig import conf

"""该模块是生成日志的"""

# 读取配置文件中的数据，方便后续修改直接在配置文件中修改
level = conf.get("logging", "level")
f_level = conf.get("logging", "f_level")  # 输出道文件等级
s_level = conf.get("logging", "s_level")  # 输出到控制台等级


class my_log():

    @staticmethod
    def cteate_logger():
        # 创建一个python24日志收集
        mylog = logging.getLogger("python24")
        # 设置日志默认收集等级
        mylog.setLevel(level)

        # 添加输出渠道
        # 输出到控制台
        sh = logging.StreamHandler()
        # 设置输出等级
        sh.setLevel(s_level)
        # 将输出渠道绑定到日志收集器上
        mylog.addHandler(sh)

        # 输出到文件
        fh = TimedRotatingFileHandler(filename=LOG_DIR, when="H", interval=24, backupCount=30, encoding="utf_8")
        # 设置输出等级
        fh.setLevel(f_level)
        # 将输出渠道绑定到日志收集器上
        mylog.addHandler(fh)

        # 创建文件输出格式
        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

        # 将输出格式与输出渠道进行绑定
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        return mylog


# 调用类的静态方法，创建一个日志收集器
Log = my_log.cteate_logger()

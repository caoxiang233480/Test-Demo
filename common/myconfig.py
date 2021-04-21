# -*- coding: utf-8 -*-


from common.contants import CONF_DIR
from configparser import ConfigParser

"""该模块处理读取配置文件的数据"""


class myconf(ConfigParser):
    def __init__(self, filename, encoding="utf8"):
        super().__init__()
        self.filename = filename
        self.encoding = encoding
        self.read(filename, encoding)

    def write_data(self, section, option, value):
        self.set(section, option, value)
        self.write(open(self.filename, "w", encoding=self.encoding))


conf = myconf(CONF_DIR)
res = conf.get("url_project", "url")

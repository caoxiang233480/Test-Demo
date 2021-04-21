# -*- coding: utf-8 -*-

import pymysql
from common.myconfig import conf


class HandleDB:
    def __init__(self):
        # 连接数据库
        self.con = pymysql.connect(host=conf.get("mysql", "host"), user=conf.get("mysql", "user"),
                                   password=conf.get("mysql", "password"), port=conf.getint("mysql", "port"),
                                   charset="utf8")
        # 创建一个游标
        self.cur = self.con.cursor()

    def get_one(self, sql):
        """获取到查询的第一条数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def get_all(self, sql):
        """获取到查询的所有数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def count(self, sql):
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def close(self):
        """关闭游标"""
        self.cur.close()
        """关闭连接"""
        self.con.close()


db = HandleDB()
if __name__ == "__main__":
    sql = "SELECT leave_amount FROM futureloan.member WHERE id=84228"

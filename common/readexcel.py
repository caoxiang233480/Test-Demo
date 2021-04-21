# -*- coding: utf-8 -*-

import openpyxl
import os
from common.contants import URL_DIR

# 暂时不用
# # 路径处理，全部处理为相对路径
# dir = os.path.dirname(__file__)
# filename = os.path.dirname(dir)
# # print(filename)
# path = os.path.join(filename, "data\case.xlsx")

"""该模块读取excel表格数据的"""


class case_data():
    pass


class read_excel():
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        self.workbook = openpyxl.load_workbook(self.filename)
        self.sheet = self.workbook[self.sheet_name]

    def close(self):
        self.workbook.close()

    def read_data(self):
        self.open()
        rows = list(self.sheet.rows)
        # print(rows)
        title = []
        for i in rows[0]:
            title.append(i.value)
        list1 = []
        for j in rows[1:]:
            list2 = []
            for k in j:
                list2.append(k.value)
            bb = dict(zip(title, list2))
            list1.append(bb)
        # self.close()
        # print(list1)
        return list1

    def read_data2(self):
        self.open()
        rows = list(self.sheet.rows)
        title = []
        for i in rows[0]:
            title.append(i.value)

        li1 = []
        for j in rows[1:]:
            li2 = []
            for k in j:
                li2.append(k.value)
            dd = list(zip(title, li2))

            cases = case_data()
            for w, v in dd:
                setattr(cases, w, v)
            li1.append(cases)
            self.close()
        # print(li1)
        return li1

    def write_data(self, row, column, value):
        # 打开
        self.open()
        # 写入
        self.sheet.cell(row=row, column=column, value=value)
        # 保存
        self.workbook.save(self.filename)
        # 关闭
        self.close()


if __name__ == '__main__':
    excel = read_excel(URL_DIR, "withdraw")
    cases = excel.read_data()
    print(cases)
    for i in cases:
        print(i["interface"])

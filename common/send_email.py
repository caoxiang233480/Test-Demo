# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.myconfig import conf


def send_msg(file_path):
    # 第一步连接到stmp服务器
    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.login("需要自己填写邮箱", "需要自己填写邮箱的秘钥")
    # 第二步构建邮件
    smg = MIMEMultipart()
    text_smg = MIMEText(open(file_path, "r", encoding="utf8").read(), "html")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path, "rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='reports.html')
    smg.attach(file_msg)

    smg["Subject"] = "测试报告"
    # 添加发件人
    smg["From"] = "需要自己填写邮箱"
    # 添加收件人  这里读取配置文件中的邮箱账号
    smg["To"] = conf.get("email", "email")

    # 第三步发送邮件
    smtp.send_message(smg, from_addr="需要自己填写邮箱", to_addrs=conf.get("email", "email"))

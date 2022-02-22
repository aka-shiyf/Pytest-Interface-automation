import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def send_mail(self, path):
        """第三发送测试报告"""
        # ----------1.跟发件相关的参数------

        smtpserver = "smtp.163.com"  # 发件服务器
        port = 25  # 非SSL协议端口号
        sender = "17702723837@163.com"
        psw = "ASPLSQQSHZCIQUMD"
        receiver = "1910491843@qq.com"  # 单个接收人也可以是 list
        # receiver = ["xxxxx@qq.com"]  # 多个收件人 list 对象

        # 读文件
        # file_path = "Result.html"
        # with open(file_path, "rb") as fp:
        #     mail_body = fp.read()
        with open(path, "rb") as f:
            mail_body = f.read()
        msg = MIMEMultipart()
        msg["from"] = sender  # 发件人
        msg["to"] = receiver  # 收件人
        # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
        msg["subject"] = "自动化测试报告"  # 主题

        # 正文
        # body = MIMEText(mail_body, "html", "utf-8")
        # msg.attach(body)
        filename = "测试报告.html"
        # 附件
        att = MIMEText(mail_body, "html", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # att.add["Content-Disposition"] = 'attachment; filename="登录测试.html"'  # 附件的名称
        att.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(att)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)  # 连服务器
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)  # QQ 邮箱
            smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        print("已向%s发送邮件" % receiver)
        smtp.quit()

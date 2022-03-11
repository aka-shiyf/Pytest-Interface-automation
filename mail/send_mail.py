import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def send_mail(self):
        """第三发送测试报告"""
        # ----------1.跟发件相关的参数------

        smtpserver = "smtp.163.com"   # 必填发件服务器
        port = 25  # 必填非SSL协议端口号
        sender = "17702723837@163.com"  # 必填
        psw = "ASPLSQQSHZCIQUMD"  # 必填
        receiver = "1910491843@qq.com"  # 必填单个接收人也可以是 list
        # receiver = ["xxxxx@qq.com"]  # 多个收件人 list 对象

        # 读文件
        # file_path = "Result.html"
        # with open(file_path, "rb") as fp:
        #     mail_body = fp.read()
        # with open(path, "rb") as f:
        mail_body = '测试报告地址：http://192.168.90.53:8081/view/test/job/flashchainsign_pytest/allure/'
        msg = MIMEMultipart()
        msg["from"] = sender  # 必填发件人
        msg["to"] = receiver  # 必填收件人
        # msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
        msg["subject"] = "自动化测试报告"  # 必填主题

        # 邮件正文正文
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)

        # filename = "测试报告.html"
        # 附件
        # att = MIMEText(mail_body, "html", "utf-8")
        # att["Content-Type"] = "application/octet-stream"
        # att.add["Content-Disposition"] = 'attachment; filename="登录测试.html"'  # 附件的名称
        # att.add_header('Content-Disposition', 'attachment', filename=filename)
        # msg.attach(att)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)  # 连服务器
            smtp.login(sender, psw)
        except:
            smtp = smtplib.SMTP_SSL(smtpserver, port)  # QQ 邮箱
            smtp.login(sender, psw)  # 登录
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送
        print(f"已向{receiver}发送邮件")
        smtp.quit()

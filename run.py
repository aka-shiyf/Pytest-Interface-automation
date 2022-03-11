# coding=utf-8
import os
import time
import pytest
from mail.send_mail import SendMail

if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system('allure generate ./temps -o ./reports --clean')
    SendMail().send_mail()
# pytest
# pytest-html 生成html报告
# pytest-xdist  多线程运行
# pytest-ordering  改变测试用例执行顺序
# pytest-rerunfailures 失败用例重跑
# allure-pytest  生成allure测试报告
# 通过pip install -r requrements.txt 执行安装插件


# markers =
# smoke:maoyan 仅执行标记用例  使用方法：-m "smoke"  通过@pytest.mark.smoke标记

# 运行方式
# -v输出更加详细的运行信息
# -s输出调试信息
# -n多线程
# --reruns 数字  失败用例重跑  --reruns=2重跑2次
# --html 生成html报告 --html=./report.html

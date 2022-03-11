import os
import re

import allure
import pytest
from common.yaml_util import YamlUtil
from method.request_method import RequestMethod


@allure.feature("消费记录")  # 一级菜单
class TestConsumption:
    token = YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["token"]

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("订单列表")  # 二级菜单
    @pytest.mark.parametrize('args',
                             YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/consumption_list.yml"))
    def test_consumption_list(self, args):
        """
        订单列表，post请求，/bes/order/getOrderList，正例：正常参数请求，获取订单列表
        """
        print(f"当前驱动数据：{args}")
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"],
                                                    headers=TestConsumption.token, data=args["payload"])
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("消费记录")  # 二级菜单
    @pytest.mark.parametrize('args',
                             YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/consumption_record.yml"))
    def test_consumption_record_list(self, args):
        """
        消费记录，post请求，/bes/bought_package/deductionWebList，正例：正常参数请求，获取消费记录
        """
        print(f"当前驱动数据：{args}")
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"],
                                                    headers=TestConsumption.token, data=args["payload"])
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("充值记录")  # 二级菜单
    @pytest.mark.parametrize('args',
                             YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/recharge_record.yml"))
    def test_recharge_record(self, args):
        """
        充值记录列表，post请求，/bes/order/list,正例：正常参数请求，获取充值记录列表
        """
        print(f"当前驱动数据：{args}")
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"],
                                                    headers=TestConsumption.token, data=args["payload"])
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("退款申请")  # 二级菜单
    @pytest.mark.parametrize('args',
                             YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/consumption_refund.yml"))
    def test_consumption_refund(self, args):
        """
        充值记录列表，post请求，/bes/order/list，反例：已使用套餐申请退款
        """
        print(f"当前驱动数据：{args}")
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"],
                                                    headers=TestConsumption.token, data=args["payload"])
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert re.findall(r'"code":(.+),', response.text)[0] == '500'
        with allure.step("断言接口返回code=500"):
            allure.attach(re.findall(r'"code":(.+),', response.text)[0])

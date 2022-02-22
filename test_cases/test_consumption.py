import os
import allure
import pytest
from common.yaml_util import YamlUtil
from method.request_method import RequestMethod


@allure.feature("消费记录")  # 一级菜单
class TestConsumption:
    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("订单列表")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/consumption_list.yml"))
    def test_consumption_list(self, args):
        """获取消费列表，对响应结果和合同数据进行断言"""""
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"], headers=YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["headers"], data=args["payload"])
        print(response.text)
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200
        with allure.step("断言状态码为200"):
            allure.attach("status_code", response.status_code)

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("消费记录")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/consumption_record.yml"))
    def test_consumption_record_list(self, args):
        """获取消费列表，对响应结果和合同数据进行断言"""""
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"], headers=YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["headers"], data=args["payload"])
        print(response.text)
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("充值记录")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/data/Consumption/recharge_record.yml"))
    def test_recharge_record(self, args):
        """获取消费列表，对响应结果和合同数据进行断言"""""
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"], headers=YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["headers"], data=args["payload"])
        print(response.text)
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200


import os
import allure
import pytest
from common.yaml_util import YamlUtil
from method.request_method import RequestMethod


@allure.feature("合同接口")  # 一级菜单
class TestContract:
    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("获取合同列表")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/data/Contract/query_contract_list.yml"))
    def test_check_contract_list(self, args):
        """获取合同列表，对响应结果和合同数据进行断言"""""
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"], headers=YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["headers"], data=args["payload"])
        print(response.text)
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert response.status_code == 200

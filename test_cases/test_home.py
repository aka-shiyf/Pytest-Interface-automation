import os
import allure
import pytest
from common.yaml_util import YamlUtil
from method.request_method import RequestMethod


@allure.feature("首页接口")  # 一级菜单
class TestHome:
    """
    获取首页合同数据，post请求，/bes/contract/home，正例：正常参数请求，获取首页合同数据
    """
    token = YamlUtil().read_extract_yaml(os.getcwd() + "/data/token.yml")["token"]

    @allure.severity(allure.severity_level.CRITICAL)  # 设置用例优先级
    @allure.story("获取首页合同数据")  # 二级菜单
    @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml(os.getcwd() + "/data/Home/contract_data.yml"))
    def test_home_list(self, args):
        response = RequestMethod().all_send_request(method=args["method"], url=args["url"], headers=TestHome.token,
                                                    data=args["payload"])
        with allure.step("响应结果"):
            allure.attach(response.text)
        assert args["validate"]["equals"] == response.status_code

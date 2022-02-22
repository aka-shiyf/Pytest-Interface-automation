# import allure
# import requests
# import pytest
# from common.yaml_util import YamlUtil
# from method.request_method import RequestMethod
#
#
# @allure.feature("测试类")
# class TestApi:
#     @allure.story("第一个allure用例")
#     @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
#     def test_setup(self):
#         print("我就是打酱油的setup")
#
#     @allure.step(title="run就是一个正常的方法.")
#     def test_run(self):
#         allure.attach("这是一个带描述的用例", "用例描述")
#         print("我要运行")
#         assert True
#
#     def test_skip(self):
#         print("我要跳过")
#
#     @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
#     @allure.testcase("http://www.baidu.com/", "测试用例的地址")
#     @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
#     def test_error(self):
#         with allure.attach("自定义描述1", "我需要让他进行错误"):
#             print("我错误了")
#             assert False
#
#     def test_alluer_feature(self):
#         print("测试需求")
#
#     # @pytest.mark.parametrize('args', YamlUtil().read_extract_yaml())
#     # def test_movide(self, args):
#     #     """
#     #     获取测试用例
#     #     根据不同请求去调用
#     #     :param args:
#     #     :return: 测试结果
#     #     """
#     #     url = args["url"]
#     #     params = args["params"]
#     #     method = args["method"]
#     #     res = RequestMethod().all_send_request(method=method, url=url, data=params)
#     #     print(res.text)
#     #     assert args["validate"]["equals"] == res.status_code
#     #     YamlUtil().clear_save_yaml()
#     #     YamlUtil().write_save_yaml(res.json())
#
#     @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
#     def test_xfail_expected_failure(self):
#         """this test is an xfail that will be marked as expected failure"""
#         assert False
#
#     @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
#     def test_xfail_unexpected_pass(self):
#         """this test is an xfail that will be marked as unexpected success"""
#         assert True
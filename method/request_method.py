import requests
import json


class RequestMethod:
    session = requests.session()  # 会话

    def all_send_request(self, method, url, data, headers, **kwargs):
        method = str(method).lower()
        if method == "get":
            res = RequestMethod.session.request(method=method, url=url, params=data, **kwargs)
        elif method == "post":
            str_data = json.dumps(data)
            # print(str_data)
            res = requests.request(method=method, url=url, data=str_data, headers=headers)
        else:
            print("不支持的请求方式")
        return res
        # url = self.args["url"]
        # headers = self.args["headers"]
        # params = self.args["params"]
        # files = self.args["files"]
        # cookies = self.args["cookies"]
        # method = self.args["method"]
        # json = self.args['json']
        # if method == "get":
        #     res = requests.request('get', url=url, params=params)
        #     return print(res.text)
        # elif method == "post":
        #     res = requests.request('post', url=url, json=json)
        #     return print(res.text)

        # if method == "POST":
        #     return requests.post(url, data, json, **kwargs)
        # if method == "PUT":
        #     if json:
        #         # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
        #         data = complexjson.dumps(json)
        #     return self.session.put(url, data, **kwargs)
        # if method == "DELETE":
        #     return self.session.delete(url, **kwargs)
        # if method == "PATCH":
        #     if json:
        #         data = complexjson.dumps(json)
        #     return self.session.patch(url, data, **kwargs)

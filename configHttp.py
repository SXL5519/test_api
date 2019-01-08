#-*- coding:utf-8 -*-
"""
配置接口请求方法
"""
import ast

import requests
import readConfig as readConfig
import json


class ConfigHttp:

    def __init__(self):
        localReadConfig = readConfig.ReadConfig()
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = float(localReadConfig.get_http("timeout"))
        ###将字符串转化成字典
        # headers = ast.literal_eval(localReadConfig.get_http("headers"))
        self.params = {}
        self.data = {}
        # self.data = json.dumps({})
        self.url = None
        self.files = {}
        self.headers={}

    def set_url(self, url):
        """
        组装URL
        :param url:
        :return:
        """
        self.url = host + url
        # print(self.url)
        # return self.url

    def set_headers(self, header):
        self.headers = ast.literal_eval(header)

    def convert_set_headers(self,headers):
        self.headers=headers

    def set_params(self, param):

        self.params = ast.literal_eval(param)

    def set_data(self, data):
        """
        组装data ，需要改变变量类型
        :param data:
        :return:
        """
        self.data =ast.literal_eval(data)

    def convert_set_data(self, data):
        """
        组装修改后的data ，不需要改变变量类型
        :param data:
        :return:
        """
        self.data =data

    def set_files(self, file):
        """
        上传文件接口，组装file
        :param file:
        :return:
        """
        self.files = ast.literal_eval(file)

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params,timeout=timeout)
            # response.raise_for_status()
            return response
        except TimeoutError:
            # self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url,data=self.data,headers=self.headers,timeout=timeout)
            # response.raise_for_status()
            return response
        except TimeoutError:
            # self.logger.error("Time out!")
            return None

# if __name__ == "__main__":
#     a=ConfigHttp()
#     a.set_url("/hxwj-wkj-controller/act/bigsurprise/subPage.do")
#     a.set_data({'surpriseId':'454'})
#     a.set_headers({'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Mobile Safari/537.36'})
#     print(a.post())
#     print(a.post().url)
#     print(a.post().status_code)
#     print(a.post().headers)
#     print(a.post().json())
#     # print(a.post().content)
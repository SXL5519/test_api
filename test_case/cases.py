#-*- coding:utf-8 -*-
import ast

from configHttp import ConfigHttp
from initial_file import MyTest
from read_data_file import Readfile
from db_file import DB



"""
测试用例
"""
class AA(MyTest):

    dicts = {'token': '',
            'id': '',
            'menuId':'',
            'goodsId':''}
    def test_01(self):
        """登录"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(0))
        a.set_data(b.read_data(0))
        r = a.post()
        print(r.json())
        self.dicts['token']=r.json()['data']['token']
        self.dicts['id']=r.json()['data']['id']
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'],b.read_success(0))
            print('登录成功')
        except:
            print('登录失败')
            raise

    def test_02(self):
        """首页"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(1))
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'],b.read_success(1))
            print('查询成功')
        except:
            print('查询失败')
            raise

    def test_03(self):
        """猜你喜欢"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(2))
        a.set_data(b.read_data(2))
        r = a.post()
        print(r.json())
        self.dicts['goodsId']=r.json()['data']['data'][0]['id']
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(2))
            print('查询成功')
        except:
            print('查询失败')
            raise

    def test_04(self):
        """启动广告页"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(3))
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(3))
            print('启动成功')
        except:
            print('启动失败')
            raise

    def test_05(self):
        """获取首页地址"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(4))
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(4))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_06(self):
        """获取首页数据"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(5))
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(5))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_07(self):
        """主页分类"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(6))
        r = a.post()
        print(r.json())
        self.dicts['menuId']=r.json()['data'][0]['id']
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(6))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_08(self):
        """分类列表-筛选商品页面"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(7))
        aa=ast.literal_eval(b.read_data(7))
        aa['menuId']=self.dicts['menuId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(7))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_09(self):
        """分类商品列表(人气/价格/筛选)"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(8))
        aa=ast.literal_eval(b.read_data(8))
        aa['menuId'] = self.dicts['menuId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(8))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_10(self):
        """某个商品评论-有图列表"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(9))
        aa=ast.literal_eval(b.read_data(9))
        aa['goodsId'] = self.dicts['goodsId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(9))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_11(self):
        """某个商品评论-所有评论"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(10))
        aa=ast.literal_eval(b.read_data(10))
        aa['goodsId'] = self.dicts['goodsId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(10))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_12(self):
        """某个商品评论-好评"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(11))
        aa = ast.literal_eval(b.read_data(11))
        aa['goodsId'] = self.dicts['goodsId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(11))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_13(self):
        """某个商品评论-中评"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(12))
        aa = ast.literal_eval(b.read_data(12))
        aa['goodsId'] = self.dicts['goodsId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(12))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_14(self):
        """某个商品评论-差评"""
        a = ConfigHttp()
        b = Readfile()
        a.set_url(b.read_url(13))
        aa = ast.literal_eval(b.read_data(13))
        aa['goodsId'] = self.dicts['goodsId']
        a.convert_set_data(aa)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(13))
            print('获取成功')
        except:
            print('获取失败')
            raise

    def test_15(self):
        """下单"""
        a = ConfigHttp()
        b = Readfile()
        c=DB()
        a.set_url(b.read_url(14))
        data = ast.literal_eval(b.read_data(14))
        data['customer'] = self.dicts['id']
        print(data)
        headers=ast.literal_eval(b.read_headers(14))
        headers['Authorization'] = self.dicts['token']
        a.convert_set_data(data)
        a.convert_set_headers(headers)
        r = a.post()
        print(r.json())
        self.assertEqual(r.status_code, 200)
        try:
            self.assertEqual(r.json()['success'], b.read_success(14))
            print('下单成功')
        except:
            print('下单失败')
            raise
        # c.connect_mongodb_all("tb_user",n={"telephone" : "17602882784"})



    # def test_(self):
    #     """提现记录"""
    #     a = ConfigHttp()
    #     b = Readfile()
    #     print(b.read_title(1))
    #     a.set_url(b.read_url(1))
    #     aa=ast.literal_eval(b.read_headers(1))
    #     print(aa)
    #     a.set_data(b.read_data(1))
    #     print(self.dicts)
    #     aa['Authorization']=self.dicts['token']
    #     a.convert_set_headers(aa)
    #     r = a.post()
    #     print(r.json())
    #     self.assertEqual(r.status_code, 200)
    #     try:
    #         self.assertEqual(r.json()['success'],b.read_success(1))
    #         print('登录成功')
    #     except:
    #         print('登录失败')
    #         raise



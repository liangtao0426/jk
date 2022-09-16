#coding=utf-8

import unittest
from utils.handle_excel import Handel_Excel
from utils.handle_path import *
from utils.handle_requests import Send_Requests
from utils.handle_conf import Handle_Conf
from ddt import ddt,data   #导入ddt模块中的dtt装饰器data装饰器



'''
ddt模块：用来做数据驱动
作用:可以在拿到exce1表格中的数据进行循环读取，每读取一个数据都会拿着该数据运行一下用例的代码
装饰器的作用:在不改变原有函数的功能基础之上给函数增加新的功能
ddt装饰器：用来装饰类的
data装饰器:用来装饰用例(只有在ddt装饰的类中的用例才能被data装饰器装饰)
'''
@ddt
class Test_Login(unittest.TestCase):

    case_file = os.path.join(data_path,'apicase.xlsx')
    excel = Handel_Excel(case_file,'login')
    cases = excel.read_data()   #保存所有用例数据的列表，并设置为一个类变量
    conf_file = os.path.join(conf_path,'conf.ini')   #实例化一个操作ini文件的对象，并设置为-一个类变量.
    conf = Handle_Conf(conf_file)   #实例化一个发送接口请求的对象，并设置为一个类变量
    request = Send_Requests()


    def setUp(self):
        pass

    def tearDown(self):
        pass
    @data(*cases)
    def test_login(self,case):
        #组建接口请求第一步:组建url地址
        url = self.conf.get_value('env','url') + case['url']
        #组建接口请求的第二步:获取请求参数
        datas = eval(case['data'])
        #组建接口请求的第三步:获取接口的请求方法
        method = case['method']
        #组建接口请求的第四步:获取接口的请求头
        headers = eval(self.conf.get_value('env','headers'))
        #发送接口请求
        resp = self.request.send(method=method,url=url,data=datas,headers=headers)
        result = resp.json()   #获取接口响应数据
        row_num = case['case_id'] + 1    #定义写入报告的行

        #对接口的响应数据进行断言
        excepted = eval(case['excepted'])  #提取excel表格中的预期结果
        try:  #try是尝试执行try下面的代码块，如果代码块报错则走到except后面的代码，如果代码块没报错则执else后面的代码
            self.assertEqual(result['msg'],excepted['msg'])  #断言接口的实际结果的msg数据与预期结果的msg数据相同
            self.assertEqual(result['code'],excepted['code']) #断言接口的实际结果的code数据与预期结果的code数据相同
        except Exception as e:  #捕获异常，并且将报错信息取个别名为e
            # print(e)
            self.excel.write_excel(row_num,8,'不通过')
            # self.assertEqual(result['code'],excepted['code'])
        else:
            self.excel.write_excel(row_num,8,'通过')

if __name__ == '__main__':
    unittest.main()


























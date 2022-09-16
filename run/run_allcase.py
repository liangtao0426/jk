#coding=utf-8


import unittest
import time
from lib.HTMLTestRunnerNew import HTMLTestRunner
from utils.handle_path import *

def auto_run():
    """
    运行用例的函数
    :return:
    """
    # print(report_path)
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    # print(now)
    report_filename = report_path + '\\' + now +'api_report.html'
    f = open(report_filename,'wb')

    #unittest框架中的discover方法testcase_path路经下的以test开头的模块中搜索以test开头的测试用例,并且返回以后suit套件对象

    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern='test*.py')
    runner = HTMLTestRunner(stream=f,
                            title='登录接口自动化运行报告',
                            description='登录接口运行情况如下',
                            tester='liangliang')
    runner.run(discover)
auto_run()





















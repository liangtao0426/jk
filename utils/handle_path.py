#coding=utf-8

"""
此模块时用来组建项目各个包的路径

"""
import os
#定义项目的路径
base_path=os.path.dirname(os.path.dirname(__file__))   #获取当前文件所在的目录
# print(base_path)
#定义conf包的路径
conf_path=os.path.join(base_path,'conf')
# print(conf_path)
#定义data包的路径
data_path=os.path.join(base_path,'data')
# print(data_path)
#定义lib包的路径
lib_path=os.path.join(base_path,'lib')
# print(lib_path)
#定义report包的路径
report_path=os.path.join(base_path,'report')
# print(report_path)
#定义run包的路径
run_path=os.path.join(base_path,'run')
# print(run_path)
#定义testcase包的路径
testcase_path=os.path.join(base_path,'testcase')
# print(testcase_path)
#定义utils包的路径
utils_path=os.path.join(base_path,'utils')
# print(utils_path)


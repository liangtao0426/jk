#coding=utf-8

from configparser import ConfigParser
from utils.handle_path import *
class Handle_Conf(ConfigParser):
    """
    当前类时用来处理ini文件的一个工具类
    """
    def __init__(self,filename):
        super(Handle_Conf, self).__init__()    #继承父类的初始化方法
        self.filename = filename   #把传入进来的形式参数复制给到一个实例变量filename
        self.read(self.filename)   #使用当前类的对象调用父类中的read方法读取传入进来的文件

    def get_value(self,section,option):
        """
        获取ini文件中对应的section下option的value值
        :return:
        """
        value = self.get(section,option)   #使用当前类的对象调用父类的get方法获取该对象的内容中section 下option的值
        # print(value)
        return value

if __name__ == '__main__':
    filepath = os.path.join(conf_path,'conf.ini')    #拼接conf.ini文件的路径
    h = Handle_Conf(filepath)    #通过Handle_conf类实例化一个操作conf.ini的文件对象出来
    h.get_value('env','url')     #使用操作conf. ini文件的工具对象调用get_value方法获取conf.ini文件中section,为env, option为url的值















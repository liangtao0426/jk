# coding=utf-8

import openpyxl        #导入openpyxl库，这个可以读取excel表格中的数据
from utils.handle_path import *

class Handel_Excel(object):
    """
    封装一个读取excel表格的工具类
    """
    def __init__(self,filename,sheetname):
        self.filename = filename    #将实例化时传进来的文件名设置为一个实例变量
        self.sheetname = sheetname  #将实例化时传进来的sheet名设置为一个实例变量

    def open(self):
        """
        封装一个打开excel表格的工具方法
        :return:
        """
        ##通过openpyxl包中的load_ workbook函数读取filename文件中的数据，并返回一个文件对象
        self.wb = openpyxl.load_workbook(self.filename)
        #读取该文件对象中指定sheet页的数据，并返回一个sheet对象
        self.sh = self.wb[self.sheetname]

    def read_data(self):
        """
        封装一个读取excel表格中数据的方法
        :return:
        """
        self.open()  #调用open方法先打开文件
        datas = list(self.sh.rows)    #提取sheet对象中所有存在内容行保存到一个列表中
        # print(datas)
        # title = []
        # for i in datas[0]:
        #     title.append(i.value)
        # 列表解析式
        title = [i.value for i in datas[0]]
        #创建一个空列表，用来保存所有的测试用例场景
        cases = []
        for j in datas[1:]:   #遍历datas这个列表中的第2行到最后一行的数据，j是一个个的元素数据
            values = [k.value for k in j]   #对j进行遍历，使k.value获取每个单元格中的数据保存到一个列表中
            case = dict(zip(title,values))  #将title列表和values列表进行打包，打完包以后转换成一个字典
            cases.append(case)   #将每个字典保存到cases这个列表纵
        # print(cases)
        return cases
    def write_excel(self,row,column,value):
        """
        封装一个向excel表格中写入数据的方法
        :return:
        """
        self.open()
        self.sh.cell(row,column,value) #向指定的row行和column列中写入value值
        self.wb.save(self.filename) #保存excel表格中的内容并关闭






if __name__ == '__main__':
    filepath = os.path.join(data_path,'apicase.xlsx')
    h = Handel_Excel(filepath,'login')
    h.read_data()
    # h.write_excel(2,8,'小申')









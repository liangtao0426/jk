#coding=utf-8
import requests

class Send_Requests(object):
    """
    封装了一个发送接口请求的工具类
    """
    def __init__(self):
        """
        用来保持会话
        :return:
        """
        self.session = requests.Session()    #实例化一个session对象，用来保持会话

    def send(self,method,url,data=None,json=None,params=None,headers=None):
        """
        对requests库中的请求方式进行二次封装
        :return:
        """
        method = method.lower()     #把所有的请求方法修改为小写的形式
        if method =='get':
            resp = self.session.get(url=url,params=params)
        elif method =='post':
            resp = self.session.post(url=url,data=data,headers=headers)
        elif method =='post_json':
            resp = self.session.post(url=url,json=json,headers=headers)
        elif method =='delete':
            resp = self.session.post(url=url)
        return resp

if __name__ == '__main__':
    s = Send_Requests()
    dict1 = {'userAccount':'admin','loginPwd':'123456'}
    headers = {'content-Type':'application/x-www-form-urlencoded'}
    a = s.send('get','http://cms.duoceshi.cn/cms/manage/loginJump.do')


















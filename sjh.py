import random


class CreatePhoneNum:

    # 随机生成手机号码
    @staticmethod
    def Cell_Phone_NUM():
        HeadNumList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                       "145", "146", "147",
                       "150", "151", "152", "153", "155", "156", "158", "159",
                       "172", "174", "175", "176", "178",
                       "180", "181", "182", "183", "185", "186", "187", "188",
                       "198","189","199"
                       ]
        HeadNum = random.choice(HeadNumList)
        LastNum = str(random.randint(10000000, 99999999))
        return HeadNum + LastNum
# 调试

if __name__ == '__main__':
    print("手机号码：", CreatePhoneNum.Cell_Phone_NUM())
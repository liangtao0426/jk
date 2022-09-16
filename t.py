# import turtle
# import time
#
# # 实现清屏
# def clear_screen():
#     turtle.penup()             #画笔抬起
#     turtle.goto(0,0)        #定位到（0，0）
#     turtle.color('white')
#     turtle.pensize(800)         #画笔粗细
#     turtle.pendown()           #画笔落下
#     turtle.setheading(0)        #设置朝向
#     turtle.fd(300)       #前进
#     turtle.bk(600)      #后退
#
# # 初始化海龟的位置
# def go_start(x, y, state):
#     turtle.pendown() if state else turtle.penup()
#     turtle.goto(x, y)
#
# #画线，state为真时海龟回到原点，为假时不回到原来的出发点
# def draw_line(length, angle, state):
#     turtle.pensize(1)
#     turtle.pendown()
#     turtle.setheading(angle)
#     turtle.fd(length)
#     turtle.bk(length) if state else turtle.penup()
#     turtle.penup()
#
# # 画出发射爱心的小人
# def draw_people(x, y):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.pensize(2)
#     turtle.color('black')
#     turtle.setheading(0)
#     turtle.circle(35, 360)
#     turtle.penup()
#     turtle.pensize(3)
#     turtle.setheading(90)
#     turtle.fd(45)
#     turtle.setheading(180)
#     turtle.fd(20)
#     turtle.setheading(0)
#     turtle.fd(35)
#     turtle.pendown()
#     turtle.circle(4, 360)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pensize(2)
#     turtle.setheading(0)
#     turtle.fd(20)
#     turtle.setheading(90)
#     turtle.fd(20)
#     turtle.setheading(-90)
#     turtle.pendown()
#     turtle.circle(5, 180)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.setheading(-90)
#     turtle.pendown()
#     turtle.fd(20)
#     turtle.setheading(0)
#     turtle.fd(35)
#     turtle.setheading(60)
#     turtle.fd(10)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.setheading(-90)
#     turtle.pendown()
#     turtle.fd(40)
#     turtle.setheading(0)
#     turtle.fd(35)
#     turtle.setheading(-60)
#     turtle.fd(10)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.setheading(-90)
#     turtle.pendown()
#     turtle.fd(60)
#     turtle.setheading(-135)
#     turtle.fd(60)
#     turtle.bk(60)
#     turtle.setheading(-45)
#     turtle.fd(30)
#     turtle.setheading(-135)
#     turtle.fd(35)
#     turtle.penup()
#
#
# # 画爱心
# def draw_heart(size):
#     turtle.color('red', 'pink')
#     turtle.pensize(2)
#     turtle.pendown()
#     turtle.setheading(150)
#     turtle.begin_fill()
#     turtle.fd(size)
#     turtle.circle(size * -3.745, 45)
#     turtle.circle(size * -1.431, 165)
#     turtle.left(120)
#     turtle.circle(size * -1.431, 165)
#     turtle.circle(size * -3.745, 45)
#     turtle.fd(size)
#     turtle.end_fill()
#
# # 画箭羽
# def draw_feather(size):
#     angle = 30  # 箭的倾角
#     feather_num = size // 6    # 羽毛的数量
#     feather_length = size // 3     # 羽毛的长度
#     feather_gap = size // 10     # 羽毛的间隔
#     for i in range(feather_num):
#         draw_line(feather_gap, angle + 180, False)  # 箭柄，不折返
#         draw_line(feather_length, angle + 145, True)  # 羽翼，要折返
#     draw_line(feather_length, angle + 145, False)
#     draw_line(feather_num * feather_gap, angle, False)
#     draw_line(feather_length, angle + 145 + 180, False)
#     for i in range(feather_num):
#         draw_line(feather_gap, angle + 180, False)   # 箭柄，不折返
#         draw_line(feather_length, angle - 145, True)    # 羽翼，要折返
#     draw_line(feather_length, angle - 145, False)
#     draw_line(feather_num * feather_gap, angle, False)
#     draw_line(feather_length, angle - 145 + 180, False)
#
# # 画一箭穿心,最后箭的头没有画出来，用海龟来代替
# def arrow_heart(x, y, size):
#     go_start(x, y, False)
#     draw_heart(size * 1.15)
#     turtle.setheading(-150)
#     turtle.penup()
#     turtle.fd(size * 2.2)
#     draw_heart(size)
#     turtle.penup()
#     turtle.setheading(150)
#     turtle.fd(size * 2.2)
#     turtle.color('black')
#     draw_feather(size)
#     turtle.pensize(4)
#     turtle.setheading(30)
#     turtle.pendown()
#     turtle.fd(size * 2)
#     turtle.penup()
#     turtle.setheading(29)
#     turtle.fd(size * 5.7)
#     turtle.color('black')
#     turtle.pensize(4)
#     turtle.pendown()
#     turtle.fd(size * 1.2)
#
# #显示倒数3,2,1
# def draw_0(i):
#     turtle.speed(0)
#     turtle.penup()
#     turtle.hideturtle()  # 隐藏箭头显示
#     turtle.goto(-50, -100)
#     turtle.color('red')
#     write = turtle.write(i, font=('宋体', 200, 'normal'))
#     time.sleep(1)
#
# # 显示文字
# def draw_1():
#     turtle.penup()
#     turtle.hideturtle()    #隐藏箭头显示
#     turtle.goto(-250, 0)
#     turtle.color('red')
#     write = turtle.write('你爹来喽', font=('宋体', 60, 'normal'))
#     time.sleep(2)
#
# # 显示发射爱心的小人儿
# def draw_2():
#     turtle.speed(3)
#     draw_people(-250, 20)
#     turtle.penup()
#     turtle.goto(-150, -30)
#     draw_heart(14)
#     turtle.penup()
#     turtle.goto(-20, -60)
#     draw_heart(25)
#     turtle.penup()
#     turtle.goto(205, -100)
#     draw_heart(43)
#     turtle.hideturtle()
#     time.sleep(2)
#
# def draw_3():
#     turtle.penup()
#     turtle.hideturtle()  # 隐藏箭头显示
#     turtle.goto(-220, 50)
#     turtle.color('red')
#     write = turtle.write('ihui', font=('宋体', 60, 'normal'))
#     turtle.penup()
#     turtle.goto(0, -50)
#     write = turtle.write('家族', font=('宋体', 60, 'normal'))
#     time.sleep(2)
#
#
# # 显示一箭穿心
# def draw_4():
#     turtle.speed(10)
#     turtle.penup()
#     turtle.goto(-210, -200)
#     turtle.color('blue')
#     turtle.pendown()
#     turtle.write('ihui家族   粉丝身份证', font=('wisdom', 50, 'normal'))
#     turtle.speed(1)
#     turtle.penup()
#     turtle.color("red")
#     turtle.goto(-31, -200)
#     turtle.write('   ❤    ',font=('wisdom', 50, 'normal'))
#     arrow_heart(20, -60, 51)
#     turtle.showturtle()
#
#
# number=[3,2,1]    #储存显示界面倒数数字1,2,3
#
# if __name__ == '__main__':
#     turtle.setup(900, 500)     #调画布的尺寸
#     for i in number:
#         draw_0(i)
#         clear_screen()
#     draw_1()
#     clear_screen()
#     draw_2()
#     clear_screen()
#     draw_3()
#     clear_screen()
#     draw_4()
#     turtle.done()
#
#
#
#
# # !/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # @Author: dong
# # @Date: 2018-07-05 19:37:42
# # @Env: python 3.6
# # @Github: https://github.com/PerpetualSmile
#
# from turtle import *
#
#
# # 无轨迹跳跃
# def my_goto(x, y):
#     penup()
#     goto(x, y)
#     pendown()
#
# # 眼睛
# def eyes():
#     fillcolor("#ffffff")
#     begin_fill()
#
#     tracer(False)
#     a = 2.5
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a -= 0.05
#             lt(3)
#             fd(a)
#         else:
#             a += 0.05
#             lt(3)
#             fd(a)
#     tracer(True)
#     end_fill()
#
#
# # 胡须
# def beard():
#     my_goto(-32, 135)
#     seth(165)
#     fd(60)
#
#     my_goto(-32, 125)
#     seth(180)
#     fd(60)
#
#     my_goto(-32, 115)
#     seth(193)
#     fd(60)
#
#     my_goto(37, 135)
#     seth(15)
#     fd(60)
#
#     my_goto(37, 125)
#     seth(0)
#     fd(60)
#
#     my_goto(37, 115)
#     seth(-13)
#     fd(60)
#
# # 嘴巴
# def mouth():
#     my_goto(5, 148)
#     seth(270)
#     fd(100)
#     seth(0)
#     circle(120, 50)
#     seth(230)
#     circle(-120, 100)
#
# # 围巾
# def scarf():
#     fillcolor('#e70010')
#     begin_fill()
#     seth(0)
#     fd(200)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     fd(207)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     end_fill()
#
# # 鼻子
# def nose():
#     my_goto(-10, 158)
#     seth(315)
#     fillcolor('#e70010')
#     begin_fill()
#     circle(20)
#     end_fill()
#
# # 黑眼睛
# def black_eyes():
#     seth(0)
#     my_goto(-20, 195)
#     fillcolor('#000000')
#     begin_fill()
#     circle(13)
#     end_fill()
#
#     pensize(6)
#     my_goto(20, 205)
#     seth(75)
#     circle(-10, 150)
#     pensize(3)
#
#     my_goto(-17, 200)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(5)
#     end_fill()
#     my_goto(0, 0)
#
#
#
# # 脸
# def face():
#
#     fd(183)
#     lt(45)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(120, 100)
#     seth(180)
#     # print(pos())
#     fd(121)
#     pendown()
#     seth(215)
#     circle(120, 100)
#     end_fill()
#     my_goto(63.56,218.24)
#     seth(90)
#     eyes()
#     seth(180)
#     penup()
#     fd(60)
#     pendown()
#     seth(90)
#     eyes()
#     penup()
#     seth(180)
#     fd(64)
#
# # 头型
# def head():
#     penup()
#     circle(150, 40)
#     pendown()
#     fillcolor('#00a0de')
#     begin_fill()
#     circle(150, 280)
#     end_fill()
#
# # 画哆啦A梦
# def Doraemon():
#     # 头部
#     head()
#
#     # 围脖
#     scarf()
#
#     # 脸
#     face()
#
#     # 红鼻子
#     nose()
#
#     # 嘴巴
#     mouth()
#
#     # 胡须
#     beard()
#
#     # 身体
#     my_goto(0, 0)
#     seth(0)
#     penup()
#     circle(150, 50)
#     pendown()
#     seth(30)
#     fd(40)
#     seth(70)
#     circle(-30, 270)
#
#
#     fillcolor('#00a0de')
#     begin_fill()
#
#     seth(230)
#     fd(80)
#     seth(90)
#     circle(1000, 1)
#     seth(-89)
#     circle(-1000, 10)
#
#     # print(pos())
#
#     seth(180)
#     fd(70)
#     seth(90)
#     circle(30, 180)
#     seth(180)
#     fd(70)
#
#     # print(pos())
#     seth(100)
#     circle(-1000, 9)
#
#     seth(-86)
#     circle(1000, 2)
#     seth(230)
#     fd(40)
#
#     # print(pos())
#
#
#     circle(-30, 230)
#     seth(45)
#     fd(81)
#     seth(0)
#     fd(203)
#     circle(5, 90)
#     fd(10)
#     circle(5, 90)
#     fd(7)
#     seth(40)
#     circle(150, 10)
#     seth(30)
#     fd(40)
#     end_fill()
#
#     # 左手
#     seth(70)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(-30)
#     end_fill()
#
#     # 脚
#     my_goto(103.74, -182.59)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(-15, 180)
#     fd(90)
#     circle(-15, 180)
#     fd(10)
#     end_fill()
#
#     my_goto(-96.26, -182.59)
#     seth(180)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(15, 180)
#     fd(90)
#     circle(15, 180)
#     fd(10)
#     end_fill()
#
#     # 右手
#     my_goto(-133.97, -91.81)
#     seth(50)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(30)
#     end_fill()
#
#     # 口袋
#     my_goto(-103.42, 15.09)
#     seth(0)
#     fd(38)
#     seth(230)
#     begin_fill()
#     circle(90, 260)
#     end_fill()
#
#     my_goto(5, -40)
#     seth(0)
#     fd(70)
#     seth(-90)
#     circle(-70, 180)
#     seth(0)
#     fd(70)
#
#     #铃铛
#     my_goto(-103.42, 15.09)
#     fd(90)
#     seth(70)
#     fillcolor('#ffd200')
#     # print(pos())
#     begin_fill()
#     circle(-20)
#     end_fill()
#     seth(170)
#     fillcolor('#ffd200')
#     begin_fill()
#     circle(-2, 180)
#     seth(10)
#     circle(-100, 22)
#     circle(-2, 180)
#     seth(180-10)
#     circle(100, 22)
#     end_fill()
#     goto(-13.42, 15.09)
#     seth(250)
#     circle(20, 110)
#     seth(90)
#     fd(15)
#     dot(10)
#     my_goto(0, -150)
#
#     # 画眼睛
#     black_eyes()
#
# if __name__ == '__main__':
#     screensize(800,600, "#f0f0f0")
#     pensize(3)  # 画笔宽度
#     speed(9)    # 画笔速度
#     Doraemon()
#     my_goto(100, -300)
#     write('by dongdong', font=("Bradley Hand ITC", 30, "bold"))
#     mainloop()


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: dong
# @Date: 2018-07-05 19:37:42
# @Env: python 3.6
# @Github: https://github.com/PerpetualSmile

from turtle import *


# 无轨迹跳跃
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()

# 眼睛
def eyes():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


# 胡须
def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)

    my_goto(-32, 125)
    seth(180)
    fd(60)

    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)

# 嘴巴
def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)

# 围巾
def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()

# 鼻子
def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()

# 黑眼睛
def black_eyes():
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)



# 脸
def face():

    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56,218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)

# 头型
def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()

# 画哆啦A梦
def Doraemon():
    # 头部
    head()

    # 围脖
    scarf()

    # 脸
    face()

    # 红鼻子
    nose()

    # 嘴巴
    mouth()

    # 胡须
    beard()

    # 身体
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)


    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    # print(pos())
    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print(pos())


    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    # 左手
    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    # 脚
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    # 右手
    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()

    # 口袋
    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    #铃铛
    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180-10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)

    # 画眼睛
    black_eyes()

if __name__ == '__main__':
    screensize(800,600, "#f0f0f0")
    pensize(3)  # 画笔宽度
    speed(9)    # 画笔速度
    Doraemon()
    my_goto(100, -300)
    write('by liangliang', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()

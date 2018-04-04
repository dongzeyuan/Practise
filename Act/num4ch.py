# coding=UTF-8

import wx


class MyFrame(wx.Frame):

    '''这是个测试各种函数用法的框架'''

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'TestFrame', size=(400, 300))
        panel = wx.Panel(self, -1)
        # 创建个文本框组件
        # 4-04，这个组件定义，必须定义为self.的形式，下面回调函数才能使用该变量
        self.num_txt = wx.TextCtrl(panel, -1, size=(150, 100),
                                   pos=(5, 5), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 试试SetValue方法

        # 创建个按钮组件
        self.num_button = wx.Button(
            panel, -1, "确定", size=(150, 100), pos=(5, 110))
        # 绑定按钮事件，绑定on_click回调函数
        self.num_button.Bind(wx.EVT_BUTTON, self.on_click)
    # 定义on_click回调函数，注意函数需要2个参数，self，event,但是这里我写的有问题
    # 我本意是想写成每点击一次，i自增1，记录点击次数，但是这里每次调用都会重置i，导致每次调用都打印1
    # 4-04，使用全局变量解决问题
    # 4-04, 终于学到了如何改变显示数值的方法

    def on_click(self, event):
        # 全局变量i。得这么写才能实现自增的功能
        global i
        i += 1
        # 清除上次传输的内容，如果不加Clear()方法，会导致逐行显示
        self.num_txt.Clear()
        self.num_txt.AppendText('%d\n' % i)


if __name__ == "__main__":
    # 初始化全局变量i
    i = 0
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()

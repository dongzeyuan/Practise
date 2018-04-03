# coding=UTF-8

import wx


class MyFrame(wx.Frame):

    '''这是个测试各种函数用法的框架'''

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'TestFrame', size=(400, 300))
        panel = wx.Panel(self, -1)
        # 创建个文本框组件
        num_txt = wx.TextCtrl(panel, -1, size=(150, 100), pos=(5, 5))

        # 创建个按钮组件
        self.num_button = wx.Button(
            panel, -1, "确定", size=(150, 100), pos=(5, 110))
        # 绑定按钮事件，绑定on_click回调函数
        self.num_button.Bind(wx.EVT_BUTTON, self.on_click)
    # 定义on_click回调函数，注意函数需要2个参数，self，event,但是这里我写的有问题
    # 我本意是想写成每点击一次，i自增1，记录点击次数，但是这里每次调用都会重置i，导致每次调用都打印1
    def on_click(self,event):
        i = 0
        i += 1
        print(i)


if __name__ == "__main__":
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()

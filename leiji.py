# coding=UTF-8

import wx


class Frame1(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='通过文本框输入输出',
                          size=(400, 200))
        panel = wx.Panel(self)
        wx.StaticText(parent=panel, label='输入n： ', pos=(10, 10))
        self.inputN = wx.TextCtrl(parent=panel, pos=(150, 10))
        wx.StaticText(parent=panel, label='1累加到n的结果： ', pos=(10, 50))
        self.outSum = wx.TextCtrl(parent=panel, pos=(150, 50))
        self.btnSum = wx.Button(parent=panel, label="计算", pos=(150, 100),
                                size=(50, 30))
        self.Bind(wx.EVT_BUTTON, self.f, self.btnSum)

    def f(self, event):
        n = self.inputN.GetValue()
        n = int(n)
        i = 1
        s = 0
        while i <= n:
            s = s + i
            i = i + 1
        self.outSum.SetValue(str(s))


if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()

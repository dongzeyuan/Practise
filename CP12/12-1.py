import sqlite3
import wx
import wx.grid


class MyFrame(wx.Frame):   
    def __init__(self):
        
        self.m = 0
        x0 = 22
        y0 = 20
        w = 90
        dx = 20
        dy = 20

        wx.Frame.__init__(self, None, -1, '通讯录管理小软件', size=(700, 400))
        panel = wx.Panel(self, -1)


        label_index = wx.StaticText(panel, -1, '编号', pos=(x0, y0))
        self.num = wx.TextCtrl(panel, -1, "", pos=(x0, y0 + dy), size=(w, 20))
        self.num.SetEditable(False)


        label_name = wx.StaticText(panel, -1, '姓名', pos=(x0 + w + dx, y0))
        self.name = wx.TextCtrl(panel, -1, "", pos=(x0 + w + dx, y0 + dy), size=(w, 20))

        label_sex = wx.StaticText(panel, -1, '性别', pos=(x0 + 2*(w + dx), y0))
        self.sex = wx.TextCtrl(panel, -1, "", pos=(x0 + 2*(w + dx), y0 + dy), size=(w, 20))

        label_tel = wx.StaticText(panel, -1, '电话', pos=(x0 + 3*(w + dx), y0))
        self.tel = wx.TextCtrl(panel, -1, "", pos=(x0 + 3*(w + dx), y0 + dy), size=(w, 20))

        label_qq = wx.StaticText(panel, -1, 'QQ', pos=(x0 + 4*(w + dx), y0))
        self.qq = wx.TextCtrl(panel, -1, "", pos=(x0 + 4*(w + dx), y0 + dy), size=(w, 20))

        label_adres = wx.StaticText(panel, -1, '地址', pos=(x0 + 5*(w + dx), y0))
        self.adres = wx.TextCtrl(panel, -1, "", pos=(x0 + 5*(w + dx), y0 + dy), size=(w, 20))


if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
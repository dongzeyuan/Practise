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
        self.num = label_index(panel, -1, "", pos=(x0, y0 + dy), size=(w, 20))
        self.num.SetEditable(Fales)


        label_name = wx.StaticText(panel, -1, '姓名', pos=(x0 + w + dx, y0))
        self.name = label_name(panel, -1, "", pos=(x0 + w + dx, y0 + dy), size=(w, 20))

        label_sex = wx.StaticText(panel, -1, '性别', pos=(x0 + 2*(w + dx), y0))
        self.sex = label_sex(panel, -1, "", pos=(x0 + 2*(w + dx), y0 + dy), size=(w, 20))

        label_tel = wx.StaticText(panel, -1, '电话', pos=(x0 + 3*(w + dx), y0))
        self.tel = label_tel(panel, -1, "", pos=(x0 + 3*(w + dx), y0 + dy), size=(w, 20))

        label_qq = wx.StaticText(panel, -1, 'QQ', pos=(x0 + 4*(w + dx), y0))
        self.qq = label_qq(panel, -1, "", pos=(x0 + 4*(w + dx), y0 + dy), size=(w, 20))

        label_adres = wx.StaticText(panel, -1, '地址', pos=(x0 + 5(w + dx), y0))
        self.adres = label_adres(panel, -1, "", pos=(x0 + 5*(w + dx), y0 + dy), size=(w, 20))


if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
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
        self.name = wx.TextCtrl(
            panel, -1, "", pos=(x0 + w + dx, y0 + dy), size=(w, 20))

        label_sex = wx.StaticText(panel, -1, '性别', pos=(x0 + 2 * (w + dx), y0))
        self.sex = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 2 * (w + dx), y0 + dy), size=(w, 20))

        label_tel = wx.StaticText(panel, -1, '电话', pos=(x0 + 3 * (w + dx), y0))
        self.tel = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 3 * (w + dx), y0 + dy), size=(w, 20))

        label_qq = wx.StaticText(panel, -1, 'QQ', pos=(x0 + 4 * (w + dx), y0))
        self.qq = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 4 * (w + dx), y0 + dy), size=(w, 20))

        label_adres = wx.StaticText(
            panel, -1, '地址', pos=(x0 + 5 * (w + dx), y0))
        self.adres = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 5 * (w + dx), y0 + dy), size=(w, 20))

        self.insert = wx.Button(panel, label="新增", pos=(
            6 * x0, y0 + 3 * dy), size=(w, 25))
        self.insert.SetToolTipString("新增记录方法:\n1.在文本框中输入数据；\n2.单击此按钮以增加记录")

        self.delete = wx.Button(panel, label='删除', pos=(
            6 * x0 + w + dx, y0 + 3 * dy), size=(w, 25))
        self.delete.SetToolTipString("删除记录方法:\n1.选择一行；\n2.单击此按钮以删除。")

        self.update = wx.Button(panel, label='修改', pos=(
            6 * x0 + 2 * (w + dx), y0 + 3 * dy), size=(w, 25))
        self.update.SetToolTipString(
            "修改记录方法:\n1.选择一行；\n2.在文本框中进行修改；\n3.单击此按钮以保存修改。")

        self.select = wx.Button(panel, label='查询', pos=(
            6 * x0 + 3 * (w + dx), y0 + 3 * dy), size=(w, 25))
        self.select.SetToolTipString("查询所有记录")

        self.Bind(wx.EVT_BUTTON, self.OnInsert, self.insert)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete)
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, self.update)
        self.Bind(wx.EVT_BUTTON, self.OnSelect, self.select)

        self.grid = wx.grid.Grid(panel, pos=(10, 140), size=(550, 200))
        self.grid.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.OnGridSelect)

        self.conn = sqlite3.connect('E:\Python\AddressBook.db')
        self.cur = self.conn.cursor()

        self.res = []

    def OnGridSelect(self, event):
        li = self.grid.GetSelectedRows()
        if len(li) >= 1:
            print(li[0])
            tu = self.res[li[0]]
            self.num.SetValue('%s' % tu[0])
            self.name.SetValue('%s' % tu[1])
            self.sex.SetValue('%s' % tu[2])
            self.phone.SetValue('%s' % tu[3])
            self.qq.SetValue('%s' % tu[4])
            self.address.SetValue('%s' % tu[5])

    def OnInsert(self, event):
        s = "'" + self.name.GetValue() + "','" + self.sex.GetValue() + "','"\
            + self.phone.GetValue() + "','" + self.qq.GetValue() + "','"\
            + self.address.GetValue() + "'"
        sql = "insert into addressList(name,sex,phone,qq,address) values(" + s + ")"
        self.conn.execute(sql)
        self.conn.commit()

    def OnDelete(self, event):
        pass

    def OnUpdate(self, event):
        pass

    def OnSelect(self, event):
        pass


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()

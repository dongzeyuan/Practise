import sqlite3
import wx
import wx.grid


class MyFrame(wx.Frame):

# 开始构造函数，实际上是开始编写界面部分
    def __init__(self):
# 下面几个参数，和后面布局位置有关，这个用的很聪明，应该是试了很久确定的数值
        self.m = 0
        x0 = 22
        y0 = 20
        w = 90
        dx = 20
        dy = 20
# 开始MyFrame框架，窗口名称叫做，通讯录管理小软件，尺寸为700*400
        wx.Frame.__init__(self, None, -1, '通讯录管理小软件', size=(700, 400))
# 设置Panel面板
        panel = wx.Panel(self, -1)
# 下面几个是设定标签，注意其中Index中的SetEditable为False
        label_index = wx.StaticText(panel, -1, '编号', pos=(x0, y0))
        self.num = wx.TextCtrl(panel, -1, "", pos=(x0, y0 + dy), size=(w, 20))
# 设定SetEditable为False，不可编辑，从数据库中读取编号，这个做法其实并不好
# 可以默认数据库内的编号不显示，编号这个东西，实在用处不大
        self.num.SetEditable(False)
# 设定姓名标签栏和输入框
        label_name = wx.StaticText(panel, -1, '姓名', pos=(x0 + w + dx, y0))
        self.name = wx.TextCtrl(
            panel, -1, "", pos=(x0 + w + dx, y0 + dy), size=(w, 20))
# 设定性别标签栏和输入框
        label_sex = wx.StaticText(panel, -1, '性别', pos=(x0 + 2 * (w + dx), y0))
        self.sex = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 2 * (w + dx), y0 + dy), size=(w, 20))
# 设定电话标签栏和输入框
        label_phone = wx.StaticText(
            panel, -1, '电话', pos=(x0 + 3 * (w + dx), y0))
        self.phone = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 3 * (w + dx), y0 + dy), size=(w, 20))
# 设定QQ标签栏和输入框
        label_qq = wx.StaticText(panel, -1, 'QQ', pos=(x0 + 4 * (w + dx), y0))
        self.qq = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 4 * (w + dx), y0 + dy), size=(w, 20))
# 设定地址标签栏和输入框
        label_address = wx.StaticText(
            panel, -1, '地址', pos=(x0 + 5 * (w + dx), y0))
        self.address = wx.TextCtrl(
            panel, -1, "", pos=(x0 + 5 * (w + dx), y0 + dy), size=(w, 20))
# 设定新增按钮，以及鼠标浮于按钮上时的提示说明
        self.insert = wx.Button(panel, label="新增", pos=(
            6 * x0, y0 + 3 * dy), size=(w, 25))
        self.insert.SetToolTipString("新增记录方法:\n1.在文本框中输入数据；\n2.单击此按钮以增加记录")
# 设定删除按钮，以及鼠标浮于按钮上时的提示说明
        self.delete = wx.Button(panel, label='删除', pos=(
            6 * x0 + w + dx, y0 + 3 * dy), size=(w, 25))
        self.delete.SetToolTipString("删除记录方法:\n1.选择一行；\n2.单击此按钮以删除。")
# 设定修改按钮，以及鼠标浮于按钮上时的提示说明
        self.update = wx.Button(panel, label='修改', pos=(
            6 * x0 + 2 * (w + dx), y0 + 3 * dy), size=(w, 25))
        self.update.SetToolTipString(
            "修改记录方法:\n1.选择一行；\n2.在文本框中进行修改；\n3.单击此按钮以保存修改。")
# 设定查询按钮，以及鼠标浮于按钮上时的提示说明
        self.select = wx.Button(panel, label='查询', pos=(
            6 * x0 + 3 * (w + dx), y0 + 3 * dy), size=(w, 25))
        self.select.SetToolTipString("查询所有记录")
# 设定按钮绑定
        self.Bind(wx.EVT_BUTTON, self.OnInsert, self.insert)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, self.delete)
        self.Bind(wx.EVT_BUTTON, self.OnUpdate, self.update)
        self.Bind(wx.EVT_BUTTON, self.OnSelect, self.select)
# 布局？
        self.grid = wx.grid.Grid(panel, pos=(10, 140), size=(550, 200))
        self.grid.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.OnGridSelect)
# 这里开始连接数据库了

        self.conn = sqlite3.connect('addressBook.db')
        self.cur = self.conn.cursor()
# 下面这条命令，创建一个表，表名为addressList，包括ID,name，sex，phone,QQ，address
# 等表头信息，但是每次执行这个脚本时都会运行这条命令，如果之前运行过这个脚本，已经生成了
# 会报错提示数据库中已经存在addressList这个表，如何改？
# 修改为create table if not exists 表名（）就好了
        self.cur.execute('''create table if not exists addressList(
        ID integer primary key autoincrement,
        name varchar(10),
        sex varchar(6) NULL,
        phone varchar(11) NULL,
        QQ varchar(11) NULL,
        address varchar(30) NULL)''')

        self.res = []
# 下面进入绑定好的选择函数
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
        if len(self.num.GetValue()) > 0:
            dlg = wx.MessageDialog(None, "是否真要删除，删除后无法恢复！", "删除", wx.YES_NO |
                                   wx.ICON_QUESTION)
            if dlg.ShowModal() != wx.ID_YES:
                return
            sql = "delete from addressList where ID=" + self.num.GetValue()
            self.conn.execute(sql)
            self.conn.commit()

    def OnUpdate(self, event):
        if len(self.num.GetValue()) > 0:
            sql = "update addressList set name = '" + self.name.GetValue() + "',sex='"\
                + self.sex.GetValue() + "',phone='"\
                + self.phone.GetValue() + "',qq='" + self.qq.GetValue() + "',address='"\
                + self.address.GetValue() + "'where ID = " + self.num.GetValue()
            self.conn.execute(sql)
            self.conn.commit()

    def OnSelect(self, event):
        self.cur.execute(" select * from addressList ")
        self.res = self.cur.fetchall()
        rowNum = len(self.res)
        colNum = len(self.cur.description)
        if self.m == 1:
            self.grid.DeleteRows(0, self.grid.GetNumberRows())
            self.grid.AooendRows(rowNum)
        if self.m == 0:
            self.grid.CreateGrid(rowNum, colNum)

        i = 0
        for line in self.res:
            j = 0
            for f in line:
                s = "%s" % f
                self.grid.SetCellValue(i, j, s)
                self.grid.SetReadOnly(i, j)
                j = j + 1

            i = i + 1
        for col in range(colNum):
            self.grid.SetColLabelValue(col, self.cur.description[col][0])

        self.m = 1


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()

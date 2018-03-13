# coding=UTF-8

# 下面这个是原型中的通讯录输入模块
'''
f = open('Telbook.csv', 'w')
f.write('姓名' + '\t性别' + '\t电话' + '\t\t地址' + '\n')
flag = 1
while flag == 1:
    name = input('请输入姓名：')
    sex = input('请输入性别：')
    phone = input('请输入电话：')
    address = input('请输入住址：')
    s = name + '\t' + sex + '\t' + phone + '\t' + address + '\n'
    f.write(s)
    flag = input('是否继续输入y/n ？')
    if flag == 'y':
        flag = 1
    else:
        flag = 0
f.close
'''


import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Ditap', size=(800,600))
        panel = wx.Panel(self, -1)
        labe_name = wx.StaticText(panel, -1, '姓名',(20,20))
        text_name = wx.TextCtrl(panel, -1, '', (20,50))
        text_name.SetInsertionPoint(0)
        labe_sex = wx.StaticText(panel, -1, '性别',(300,20))
        text_sex = wx.TextCtrl(panel, -1, '', (300,50))
        text_sex.SetInsertionPoint(0)
        labe_tel = wx.StaticText(panel, -1, '电话',(580,20))
        text_tel = wx.TextCtrl(panel, -1, '', (580,50))
        text_tel.SetInsertionPoint(0)
        self.button_add = wx.Button(panel, -1, '新增', pos = (20,100))
        self.button_modify = wx.Button(panel, -1, '修改', pos = (200,100))
        self.button_del = wx.Button(panel, -1, '删除', pos = (380,100))
        self.button_search = wx.Button(panel, -1, '查询', pos = (560,100))

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
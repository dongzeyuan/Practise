# coding:utf-8
# copyright
# license





import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio Demo', size=(1200,900))
        panel = wx.Panel(self, -1)
        list1 = ['xin','gui','meng','xin']
        list2 = ['boy','girl']
        wx.RadioBox(panel,-1,'The Name',(20,20),wx.DefaultSize,list1,4,wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel,-1,'The Sex',(20,100),wx.DefaultSize,list2,2,wx.RA_SPECIFY_ROWS)
        label = wx.StaticText(panel, -1, 'Text show only',(100,150))
        text = wx.TextCtrl(panel, -1, 'Input your name:', (100,200))
        text.SetInsertionPoint(0)

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
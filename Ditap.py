# coding:utf-8
# copyright
# license





import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Ditap', size=(1200,900))
        panel = wx.Panel(self, -1)
        list1 = ['LPR','ER']
        list2 = ['LPR','ER']
        wx.RadioBox(panel,-1,'Transimitter',(20,20),wx.DefaultSize,list1,4,wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel,-1,'Probe',(20,100),wx.DefaultSize,list2,2,wx.RA_SPECIFY_COLS)
        label = wx.StaticText(panel, -1, 'Text show only',(20,180))
        text = wx.TextCtrl(panel, -1, 'Input your name:', (20,200))
        text.SetInsertionPoint(0)

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
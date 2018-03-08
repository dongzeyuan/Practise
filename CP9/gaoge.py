import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Radio Demo', size=(400,300))
        panel = wx.Panel(self, -1)
        list1 = ['xin','gui','meng','xin']
        list2 = ['boy','girl']
        wx.RadioBox(panel,-1,'The Name',(20,20),wx.DefaultSize,list1,4,wx.RA_SPECIFY_COLS)
        wx.RadioBox(panel,-1,'The Sex',(20,100),wx.DefaultSize,list2,2,wx.RA_SPECIFY_ROWS)

if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
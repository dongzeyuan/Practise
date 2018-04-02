import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Num2CH', size=(300,200))
        panel = wx.Panel(self, -1)



if __name__ == "__main__":
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
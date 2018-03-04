# coding=UTF-8
# test

import wx

class Frame1(wx.Frame):
    def __init__(self, superior):
        wx.Frame.__init__(self, parent=superior, title='my window', pos=(100,200),\
        size=(400,200))

if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)

app.MainLoop()
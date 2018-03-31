# coding:utf-8
# copyright
# license


'''import wx
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
    app.MainLoop()'''

import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Text Entry Example',
                          size=(300, 250))
        panel = wx.Panel(self, -1)
        multiLabel = wx.StaticText(panel, -1, 'Multi-line')
        multiText = wx.TextCtrl(panel, -1,
                                'Here is a loooooooooooog line of text set in the control.\n\n'
                                'See that it wrapped, and that this line is after a blank',
                                size=(200, 100), style=wx.TE_MULTILINE)
        multiText.SetInsertionPoint(0)

        richLabl = wx.StaticText(panel, -1, 'Rich Text')
        richText = wx.TextCtrl(panel, -1,
                               'If supported by the native control, this is reversed, and this is \
                               a different font.', size=(200, 100), style=wx.TE_MULTILINE)
        richText.SetInsertionPoint(0)
        richText.SetStyle(44, 52, wx.TextAttr('white', 'black'))
        points = richText.GetFont().GetPointSize()
        f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True)
        richText.SetStyle(68, 82, wx.TextAttr('blue', wx.NullColour, f))
        sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)
        sizer.AddMany([multiLabel, multiText, richLabl, richText])
        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    MyFrame().Show(True)
    app.MainLoop()

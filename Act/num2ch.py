import wx


class MyFrame(wx.Frame):

    def __init__(self):
        xc = 30
        yc = 25
        dx = 5
        wx.Frame.__init__(self, None, -1, 'Num2CH', size=(500, 200))
        panel = wx.Panel(self, -1)
        label = wx.StaticText(panel, -1, '输入阿拉伯数字', (10, 10))
        num_txt = wx.TextCtrl(panel, -1, 'Enter the num',
                              size=(150, 25), pos=(10, 30))
        num_txt.SetInsertionPoint(0)
        self.button = wx.Button(panel, -1, '确定', size=(50, 25), pos=(170, 30))

        self.creatTextFields(panel)

    # 以下部分都是被重构后的，这么写很优美！
    def labelData(self):
        return(('拾', (40, 100)), ('万', (100, 100)), ('仟', (160, 100)), ('佰', (220, 100)),
               ('拾', (280, 100)), ('圆', (340, 100)), ('角', (400, 100)), ('分', (460, 100)))

    def onelabel(self, panel, label, pos):
        static = wx.StaticText(panel, -1, label, pos)
        textPos = (pos[0] - 30, pos[1])
        wx.TextCtrl(panel, -1, '', size=(25, 15), pos=textPos)

    def creatTextFields(self, panel):
        for eachlabel, eachpos in self.labelData():
            self.onelabel(panel, eachlabel, eachpos)


if __name__ == "__main__":
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()

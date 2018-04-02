import wx

class MyFrame(wx.Frame):
   
    def __init__(self):
        xc = 30
        yc = 25
        dx = 5
        wx.Frame.__init__(self, None, -1, 'Num2CH', size=(500,200))
        panel = wx.Panel(self, -1)
        label = wx.StaticText(panel,-1,'输入阿拉伯数字',(10,10))
        num_txt = wx.TextCtrl(panel,-1,'Enter the num',size=(150,25),pos=(10,30))
        num_txt.SetInsertionPoint(0)
        self.button = wx.Button(panel,-1,'确定',size=(50,25),pos = (170,30))
        ch_txt1 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10,100))
        ch_txt1.SetInsertionPoint(0)
        ch_label1 = wx.StaticText(panel,-1,'拾',size=(xc,yc),pos=(10+xc+dx,100))
        ch_txt2 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+2*xc,100))
        ch_txt2.SetInsertionPoint(0)
        ch_label2 = wx.StaticText(panel,-1,'万',size=(xc,yc),pos=(10+3*xc+dx,100))
        ch_txt3 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+4*xc,100))
        ch_txt3.SetInsertionPoint(0)
        ch_label3 = wx.StaticText(panel,-1,'仟',size=(xc,yc),pos=(10+5*xc+dx,100))
        ch_txt4 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+6*xc,100))
        ch_txt4.SetInsertionPoint(0)
        ch_label4 = wx.StaticText(panel,-1,'佰',size=(xc,yc),pos=(10+7*xc+dx,100))
        ch_txt5 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+8*xc,100))
        ch_txt5.SetInsertionPoint(0)
        ch_label5 = wx.StaticText(panel,-1,'拾',size=(xc,yc),pos=(10+9*xc+dx,100))
        ch_txt6 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+10*xc,100))
        ch_txt6.SetInsertionPoint(0)
        ch_label6 = wx.StaticText(panel,-1,'圆',size=(xc,yc),pos=(10+11*xc+dx,100))
        ch_txt7 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+12*xc,100))
        ch_txt7.SetInsertionPoint(0)
        ch_label7 = wx.StaticText(panel,-1,'角',size=(xc,yc),pos=(10+13*xc+dx,100))
        ch_txt8 = wx.TextCtrl(panel,-1,size=(xc,yc),pos=(10+14*xc,100))
        ch_txt8.SetInsertionPoint(0)
        ch_label8 = wx.StaticText(panel,-1,'分',size=(xc,yc),pos=(10+15*xc+dx,100))



if __name__ == "__main__":
    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()
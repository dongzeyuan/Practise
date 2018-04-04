import wx


class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # 创建一些sizer
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(vgap=5, hgap=5)  # 虚拟网格sizer，此处指定了行和列之间的间隙
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(self, label="面板示例:", pos=(20, 20))
        grid.Add(self.quote, pos=(0, 0))

        # 展示事件是如何在程序中工作的一个多行文本框控件
        self.logger = wx.TextCtrl(self, pos=(300, 20), size=(
            200, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # 一个按钮
        self.button = wx.Button(self, label="保存", pos=(200, 325))
        self.Bind(wx.EVT_BUTTON, self.Onclick, self.button)

        # 编辑组件
        self.lblname = wx.StaticText(self, label="Your Name:", pos=(20, 60))
        grid.Add(self.lblname, pos=(1, 0))
        self.editname = wx.TextCtrl(
            self, value="input your name", pos=(140, 60), size=(140, -1))
        grid.Add(self.editname, pos=(1, 1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # 组合框组件
        self.sampleList = ['friends', 'advertising',
                           'web search', 'Yellow Pages']
        self.lblhear = wx.StaticText(
            self, label="Select the topic ?", pos=(20, 90))
        grid.Add(self.lblhear, pos=(3, 0))
        self.edithear = wx.ComboBox(self, pos=(150, 90), size=(
            95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        grid.Add(self.edithear, pos=(3, 1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)

        # 往sizer中添加一些空间
        grid.Add((10, 40), pos=(2, 0))  # 此处设置了间隔物的宽高

        # 复选框
        self.insure = wx.CheckBox(
            self, label="Do you want Insured Shipment ?", pos=(20, 180))
        grid.Add(self.insure, pos=(4, 0), span=(1, 2))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # 单选按钮
        radioList = ['blue', 'red', 'yellow', 'orange',
                     'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList, majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5, 0), span=(1, 2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())

    def Onclick(self, event):
        self.logger.AppendText(' Click on object with Id %d\n' % event.GetId())

    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()

    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.IsChecked())


# 带有可切换导航的面板
app = wx.App(False)
frame = wx.Frame(None, title="NoteBook示例", size=(600, 400))
nb = wx.Notebook(frame)

nb.AddPage(ExamplePanel(nb), "Absolute Positioning")
nb.AddPage(ExamplePanel(nb), "Page Two")
nb.AddPage(ExamplePanel(nb), "Page Three")
frame.Show()
app.MainLoop()

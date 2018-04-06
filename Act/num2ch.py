import wx


class MyFrame(wx.Frame):

    def __init__(self):
        xc = 30
        yc = 25
        dx = 5
        wx.Frame.__init__(self, None, -1, 'Num2CH', size=(500, 200))
        panel = wx.Panel(self, -1)
        label = wx.StaticText(panel, -1, '输入阿拉伯数字', (10, 10))
        self.num_txt = wx.TextCtrl(panel, -1, '123456.78',
                                   size=(150, 25), pos=(10, 30))
        self.num_txt.SetInsertionPoint(0)
        self.button = wx.Button(panel, -1, '确定', size=(50, 25), pos=(170, 30))
        # 将self.button按钮绑定self.getval函数
        self.Bind(wx.EVT_BUTTON, self.num2ch, self.button)

        self.creatTextFields(panel)

    # 以下部分都是被重构后的，这么写很优美！
    # 定义标签的值和pos
    def labelData(self):
        return(('拾', (40, 100)), ('万', (100, 100)), ('仟', (160, 100)), ('佰', (220, 100)),
               ('拾', (280, 100)), ('圆', (340, 100)), ('角', (400, 100)), ('分', (460, 100)))

    # 生成单个的标签和文本框
    def onelabel(self, panel, label, pos, txt):
        static = wx.StaticText(panel, -1, label, pos)
        textPos = (pos[0] - 30, pos[1])
        self.block = wx.TextCtrl(panel, -1, '', size=(25, 25), pos=textPos)
        self.block.Clear()
        self.block.AppendText(txt)

        # wx.TextCtrl.Clear()
        # wx.TextCtrl.AppendText('%s\n' % i)
    # 根据data文件的返回值（元组），依次生成对应的标签和文本框
    def creatTextFields(self, panel):

        # 这里我想用返回的列表和列表长度确定哪些文本框需要刷新
        list_1 = []
        list_1, i = self.num2ch(panel)
        tuple_1 = self.labelData()
        j = 0
        for eachlabel, eachpos in tuple_1[-i:]:
            self.onelabel(panel, eachlabel, eachpos, list_1[j])
            j += 1
        

    # 生成读取文本框内容的函数
    def getval(self, panel):
        # self.num_txt.GetValue()函数返回的是str类型
        # ########################################
        # print(type(self.num_txt.GetValue()))
        return(self.num_txt.GetValue())

    # 定义数字转换成汉字的函数：
    def num2ch(self, panel):
        # 用户输入的数字被转换成字符串
        num = self.getval(panel)
        return_val = []
        global num_ch_dict
        # 给i赋初值0，对应num字符串中的第一个数字字符
        i = 0
        # 判定当 i 小于 num字符串长度时执行后续
        if i <= len(num):
            # j作为num字符串中的元素
            for j in num:
                # 如果num[i]在词典中
                if num[i] in num_ch_dict:
                    # 打印对应的键值（key-value，键-键值）
                    return_val.append(num_ch_dict[num[i]])
                    # i自增
                    i += 1
                # 如果num[i]不在词典中，就是遇到'.'符号了
                else:
                    # i自增，跳过'.'符号
                    i += 1
        return(return_val, len(return_val))


if __name__ == "__main__":

    # 定义全局词典
    num_ch_dict = {'0': '零', '1': '壹', '2': '贰', '3': '叁',
                   '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}

    app = wx.App()
    MyFrame().Show(True)
    app.MainLoop()

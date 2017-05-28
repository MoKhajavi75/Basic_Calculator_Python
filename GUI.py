import wx


'''
app = wx.App()

frame = wx.Frame(None, wx.ID_ANY, "Fuck Ali Abdi")
frame.Show()

app.MainLoop()
'''

#djfhsjkdfhsaf

import functions


#ssdsdfsjdfabsdlfk;hajsdfhasdfha


#jadshasdjhadsk;jh

class MyFrame(wx.Frame):

    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()

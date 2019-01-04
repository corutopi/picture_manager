"""
top frame class and parts used by oneself.
"""

import wx
from view.auto.layout import MainLayout


class MainForm(MainLayout):
    def event_read_file(self, event):
        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        dialog.SetWildcard('picture|*.bmp; *.png; *.jpg')
        dialog.ShowModal()
        if dialog.GetPath() == '':
            return
        self.main_picture.SetBitmap(wx.Bitmap(dialog.GetPath()))
        self.Layout()


if __name__ == '__main__':
    app = wx.App()
    f = MainForm(None)
    f.Show()
    app.MainLoop()
    pass

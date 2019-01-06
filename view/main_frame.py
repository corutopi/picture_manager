"""
top frame class and parts used by oneself.
"""

import wx
from view.auto.layout import MainLayout


def resize_bitmap(b: wx.Bitmap, width, height) -> wx.Bitmap:
    # @todo enable to choice Correct the orientation of the image
    i: wx.Image = b.ConvertToImage()
    s: wx.Size = i.GetSize()
    old_h = s.GetHeight()
    old_w = s.GetWidth()
    if old_h / old_w == height / width:
        new_h = height
        new_w = width
    elif old_h > old_w:
        new_h = height
        new_w = (old_w * height) / old_h
    else:
        new_h = (old_h * width) / old_w
        new_w = width
    i = i.Scale(int(new_w), int(new_h), wx.IMAGE_QUALITY_HIGH)
    return wx.Bitmap(i)
    pass


class MainForm(MainLayout):
    def event_read_file(self, event):
        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        dialog.SetWildcard('picture|*.bmp; *.png; *.jpg')
        dialog.ShowModal()
        if dialog.GetPath() == '':
            return

        # @todo Correct the orientation of the image
        # part4 outside image size correct
        print(self.main_picture.GetSize())
        b = wx.Bitmap(dialog.GetPath())
        w, h = self.main_picture.GetSize()
        b = resize_bitmap(b, w, h)
        print(b.GetWidth())
        print(b.GetHeight())
        self.main_picture.SetBitmap(b)
        '''the image before centering is not displayed on the screen'''
        self.main_picture.GetParent().Layout()
        self.Layout()

        # # part3 remove warning from part2
        # b = wx.Bitmap(dialog.GetPath())
        # i: wx.Image = b.ConvertToImage()
        # i = i.Scale(100, 100, wx.IMAGE_QUALITY_HIGH)
        # b = wx.Bitmap(i)
        # self.main_picture.SetBitmap(b)
        # '''the image before centering is not displayed on the screen'''
        # self.main_picture.GetParent().Layout()
        # self.Layout()

        # # part2 use ImageFromBitmap and BitmapFromImage
        # b = wx.Bitmap(dialog.GetPath())
        # i: wx.Image = wx.ImageFromBitmap(b)
        # i = i.Scale(100, 100, wx.IMAGE_QUALITY_HIGH)
        # b = wx.BitmapFromImage(i)
        # self.main_picture.SetBitmap(b)
        # '''the image before centering is not displayed on the screen'''
        # self.main_picture.GetParent().Layout()
        # # self.main_picture.SetBitmap(wx.Bitmap(dialog.GetPath()))
        # self.Layout()

        # # part1 normal
        # b = wx.Bitmap(dialog.GetPath())
        # print(b.GetSize())
        # b.SetSize((100, 100))
        # print(b.GetSize())
        # self.main_picture.SetBitmap(b)
        # # self.main_picture.SetBitmap(wx.Bitmap(dialog.GetPath()))
        # self.Layout()
        pass


if __name__ == '__main__':
    app = wx.App()
    f = MainForm(None)
    f.Show()
    app.MainLoop()
    pass

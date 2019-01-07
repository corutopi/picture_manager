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
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path = None
        self.origin_bitmap = None
        pass

    def event_read_file(self, event):
        """Open file select dialog and display selected picture file.
        :param event:
        :return:
        """
        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        dialog.SetWildcard('picture|*.bmp; *.png; *.jpg')
        dialog.ShowModal()
        if dialog.GetPath() == '':
            return
        # set picture
        self.file_path = dialog.GetPath()
        self.origin_bitmap = wx.Bitmap(self.file_path)
        print(self.main_picture.GetSize())
        w, h = self.main_picture.GetSize()
        b = resize_bitmap(self.origin_bitmap, w, h)
        print(b.GetWidth())
        print(b.GetHeight())
        self.main_picture.SetBitmap(b)
        '''the image before centering is not displayed on the screen'''
        self.main_picture.GetParent().Layout()
        self.Layout()

    def event_change_size(self, event):
        """Resize picture to fit the frame.
        @todo not resize when maximizing window with double click
        :param event:
        :return:
        """
        if self.file_path is None:
            return
        w, h = self.main_picture.GetSize()
        b = resize_bitmap(self.origin_bitmap, w, h)
        self.main_picture.SetBitmap(b)
        self.main_picture.GetParent().Layout()
        self.Layout()

    def event_key_down(self, event):
        """Key down event like this.
        Left / Right cursor keys:
            Prev / next picture is display in same folder.
        Delete key:
            Remove displayed picture(goto trash box).
        Function key 5:
            Reload picture file.
        @todo implement
        :param event:
        :return:
        """
        pass


if __name__ == '__main__':
    app = wx.App()
    f = MainForm(None)
    f.Show()
    app.MainLoop()
    pass

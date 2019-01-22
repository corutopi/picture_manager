"""
top frame class and parts used by oneself.
@todo open picture to drag and drop file.
"""

import wx

from picture_manager.common.wx_parts import resize_bitmap
from picture_manager.view.auto.layout import MainLayout


class MainForm(MainLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self.file_path = None
        self.origin_bitmap = None
        from picture_manager.common.wx_common import get_app
        from picture_manager.ctr import MainCtr
        self.ctr: MainCtr = get_app().ctr
        pass

    def event_read_file(self, event):
        """Open file select dialog and display selected picture file.
        :param event:
        :return:
        """
        self.ctr.read_file(self)

        # dialog = wx.FileDialog(None, u'ファイルを選択してください')
        # dialog.SetWildcard('picture|*.bmp; *.png; *.jpg')
        # dialog.ShowModal()
        # if dialog.GetPath() == '':
        #     return
        # # set picture
        # self.file_path = dialog.GetPath()
        # self.origin_bitmap = wx.Bitmap(self.file_path)
        # print(self.main_picture.GetSize())
        # w, h = self.main_picture.GetSize()
        # b = resize_bitmap(self.origin_bitmap, w, h)
        # print(b.GetWidth())
        # print(b.GetHeight())
        # self.main_picture.SetBitmap(b)
        # '''the image before centering is not displayed on the screen'''
        # self.main_picture.GetParent().Layout()
        # self.Layout()

    def event_change_size(self, event):
        """Resize picture to fit the frame.
        @todo not resize when maximizing window with double click
        :param event:
        :return:
        """
        self.ctr.change_picture_size()
        # print('resize panel!')
        # print(self.main_picture.GetSize())
        # if self.file_path is None:
        #     return
        # # if wx.Bitmap, can't get Correct Size when window is maximized.
        # w, h = self.main_picture_panel.GetSize()
        # b = resize_bitmap(self.origin_bitmap, w, h)
        # self.main_picture.SetBitmap(b)
        # self.main_picture.GetParent().Layout()
        # self.Layout()

    def event_key_down(self, event: wx.KeyEvent):
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
        print('key down')
        if event.GetKeyCode() == wx.WXK_LEFT:
            # @todo Try stopping motion when you stop pressing the key
            self.ctr.prev_file()
        elif event.GetKeyCode() == wx.WXK_RIGHT:
            self.ctr.next_file()
        elif event.GetKeyCode() == wx.WXK_DELETE:
            pass
        elif event.GetKeyCode() == wx.WXK_F5:
            pass

    def event_change_size_frame(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    f = MainForm(None)
    f.Show()
    app.MainLoop()
    pass

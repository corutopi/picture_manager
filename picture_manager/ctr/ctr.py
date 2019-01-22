import wx

from picture_manager.common.wx_parts import resize_bitmap
from picture_manager.model.model import MainModel
from picture_manager.view.main_frame import MainForm


class MainCtr:
    """
    @todo implements 'undo file delete operation'
    """
    def __init__(self):
        self.view = None
        self.model: MainModel = MainModel()
        pass

    def read_file(self, window: MainForm):
        """
        Open and display picture of file_path.
        And read pictures in the folder that file_path belong.
        :return:
        """
        self.view = window
        dialog = wx.FileDialog(None, u'ファイルを選択してください')
        dialog.SetWildcard('picture|*.bmp; *.png; *.jpg')
        dialog.ShowModal()
        if dialog.GetPath() == '':
            return
        # set picture
        self.model.set_file(dialog.GetPath())
        self.set_picture(dialog.GetPath())
        # self.view.file_path = dialog.GetPath()
        # self.view.origin_bitmap = wx.Bitmap(self.view.file_path)
        # print(self.view.main_picture.GetSize())
        # w, h = self.view.main_picture.GetSize()
        # b = resize_bitmap(self.view.origin_bitmap, w, h)
        # print(b.GetWidth())
        # print(b.GetHeight())
        # self.view.main_picture.SetBitmap(b)
        # '''the image before centering is not displayed on the screen'''
        # self.view.main_picture.GetParent().Layout()
        # self.view.Layout()

    def set_picture(self, file_path):
        """
        Change displayed picture to file_path picture.
        :param file_path:
        :return:
        """
        self.view.file_path = file_path
        self.view.origin_bitmap = wx.Bitmap(self.view.file_path)
        print(self.view.main_picture.GetSize())
        w, h = self.view.main_picture.GetSize()
        b = resize_bitmap(self.view.origin_bitmap, w, h)
        print(b.GetWidth())
        print(b.GetHeight())
        self.view.main_picture.SetBitmap(b)
        '''the image before centering is not displayed on the screen'''
        self.view.main_picture.GetParent().Layout()
        self.view.Layout()

    def next_file(self):
        self.set_picture(self.model.get_next(self.view.file_path))

    def prev_file(self):
        self.set_picture(self.model.get_prev(self.view.file_path))

    def delete_file(self, file_name):
        pass

    def change_picture_size(self):
        if self.view is None:
            return
        if self.view.file_path is None:
            return
        print(self.view.main_picture.GetSize())
        # if wx.Bitmap, can't get Correct Size when window is maximized.
        w, h = self.view.main_picture_panel.GetSize()
        b = resize_bitmap(self.view.origin_bitmap, w, h)
        self.view.main_picture.SetBitmap(b)
        self.view.main_picture.GetParent().Layout()
        self.view.Layout()
        pass

    pass

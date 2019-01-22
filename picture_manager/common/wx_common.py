import wx


class MyApp(wx.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from picture_manager.ctr import ctr
        self.ctr: ctr.MainCtr = ctr.MainCtr()


def get_app() -> MyApp():
    """get wx.App that this application use"""
    return wx.GetApp()

"""
"""

from picture_manager.common.wx_common import MyApp


def main():
    """App starter."""
    from picture_manager.view import main_frame
    app = MyApp()
    f = main_frame.MainForm(None)
    f.Show()
    app.MainLoop()
    pass

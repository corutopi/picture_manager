#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
import wx.aui


class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        self.auimgr = wx.aui.AuiManager(self)
        txtctrl1 = wx.TextCtrl(self, -1, "Hello", wx.DefaultPosition,
                               wx.Size(200, 200), wx.TE_MULTILINE)
        txtctrl2 = wx.TextCtrl(self, -1, "World", wx.DefaultPosition,
                               wx.Size(200, 200), wx.TE_MULTILINE)
        self.auimgr.AddPane(txtctrl1, wx.LEFT, "hello")
        self.auimgr.AddPane(txtctrl2, wx.BOTTOM, "world")
        self.auimgr.Update()

    def OnQuit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame("test", wx.DefaultPosition, wx.Size(300, 300))
    frame.Show()
    app.MainLoop()

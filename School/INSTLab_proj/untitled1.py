# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:29:36 2022

@author: Justin
"""

import wx
class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(None, title='Hello World')
        self.Show()
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
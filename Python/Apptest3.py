# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:31:02 2022

@author: Justin
"""

import wx
class MyPanel(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        button = wx.Button(self, label='Press Me')
        button2 = wx.Button(self, label='Press Me too')
        button3 = wx.Button(self, label='Another button')
class MyFrame(wx.Frame):
    
    def __init__(self):
        super().__init__(None, title='Hello World')
        panel = MyPanel(self)
        self.Show()
if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MyFrame()
    app.MainLoop()
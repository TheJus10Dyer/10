# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:31:06 2022

@author: Justin
"""

import wx
import numpy as np 

source1 = open('INSTtest2problem1.py').read()
code1 = compile(source1, 'INSTtest2problem1.py', 'exec')

source2 = open('INSTtest2problem2.py').read()
code2 = compile(source2, 'INSTtest2problem2.py', 'exec')


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        button = wx.Button(self, label='Problem 1')
        button.Bind(wx.EVT_BUTTON, self.on_button1)
        button2 = wx.Button(self, label='Problem 2')
        button2.Bind(wx.EVT_BUTTON, self.on_button2)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(button, 0,
                       flag=wx.ALL | wx.CENTER,
                       border=5)
        main_sizer.Add(button2, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)
    def on_button1(self, event):
        print('Answer to Problem 1: \n')
        exec(code1)
    def on_button2(self, event):
        print('Answer to Problem 2: \n')
        exec(code2)
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Instrumentation Exam 2')
        panel = MyPanel(self)
        self.Show()
if __name__ == '__main__':
    app = wx.App(redirect=True)
    frame = MyFrame()
    app.MainLoop()
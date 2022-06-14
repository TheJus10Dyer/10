# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:16:07 2022

@author: 500308
"""

import time


 
while True:
    print('Openinig File...')
    file = open('longlat.txt','r+')
    print('File Opened')
    print('Writing: ', time.monotonic())
    file.seek(0)
    file.write(str(time.monotonic()))
    file.truncate()
    print('Closing File...')
    file.close()
    
    time.sleep(5)
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:06:33 2019

@author: salim
"""

os.chdir('/Users/salim/Desktop')
pip install pysftp
import pysftp
from ftplib import FTP
from ftplib import FTP

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

srv = pysftp.Connection(host="35.222.158.208", username="edemExercise3",
password= "edemExercise3", cnopts = cnopts)


srv.put("Salim.txt","/home/edemExercise3/Upload/Salim)

srv.close()
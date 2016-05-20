#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys
import os
from oogway import FeedParser
from oogway import OogwayWindow 

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__author__ =  'girish946'



if __name__ == '__main__':

    allFeeds = FeedParser()

    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        Dlg = OogwayWindow(sys.argv[1], feed = allFeeds.getCompleteFeed())
    else:
        Dlg = OogwayWindow(feed = allFeeds.getCompleteFeed())
    Dlg.show()
    app.exec_()


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
    count = 0
    feed = {}
    for i in allFeeds.sites:
        feed[i] = []
        entries = allFeeds.getRssFeedOf(i).entries
        for j in entries:

            #print j.title
            #print j.link
            count+=1
            feed[i].append((j.title, j.link,))

    

    #print feed
    #print count

    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        Dlg = OogwayWindow(sys.argv[1], feed = feed)
    else:
        Dlg = OogwayWindow(feed = feed)
    Dlg.show()
    app.exec_()


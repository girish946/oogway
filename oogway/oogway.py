#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Oogway_MainWindow(QtGui.QMainWindow):


    def __init__(self, parent=None, feed = {}):
        QtGui.QMainWindow.__init__(self, parent)
        self.centralWidget = QtGui.QWidget()
        self.resize(800, 500)
        self.setWindowTitle('Test')
        self.tabs = QTabWidget()
        self.tabs.blockSignals(True)

        self.webview = QWebView()
        self.webview.load(QUrl("http://www.google.com"))

        

        centralLayout = QtGui.QVBoxLayout()
        centralLayout.addWidget(self.tabs, 1)


        self.tabs.addTab(self.webview, "Home Page")
        

        self.tabs.tabBar().setTabsClosable(True)
        self.tabs.tabBar().tabCloseRequested.connect(self.close_handler)

        self.centralWidget.setLayout(centralLayout)
        self.setCentralWidget(self.centralWidget)

        self.feed = feed

        self.setupUi(self)


    def setupUi(self, MainWindow):

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)


        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)


        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton.clicked.connect(self.removeSite)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButton_2.clicked.connect(self.addSite)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.dockWidget.setWidget(self.dockWidgetContents)

        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget_2 = QtGui.QListWidget(self.dockWidgetContents_4)
        self.listWidget_2.setObjectName(_fromUtf8("listView_2"))
        self.horizontalLayout.addWidget(self.listWidget_2)
        self.dockWidget_2.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_2)


        self.widgetItems = []
        self.linkItems = []

        for i in self.feed:

            item = QListWidgetItem(i)
            self.listWidget.addItem(item)

            for j in self.feed[i]:
               self.widgetItems.append(j[0])
               self.linkItems.append(j[1])

        self.listWidget_2.addItems(self.widgetItems)

        self.listWidget.doubleClicked.connect(self.setLinks)
        self.listWidget_2.doubleClicked.connect(self.openLink)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Oogway_RSS_Reader", "Oogway_RSS_Reader", None))
        self.pushButton.setText(_translate("Oogway_RSS_Reader", "-", None))
        self.pushButton_2.setText(_translate("Oogway_RSS_Reader", "+", None))


    def close_handler(self, index):
        print "close_handler called, index = %s" % index
        self.tabs.removeTab(index)


    def openLink(self,index):
        
        print "clicked %s"%index.row()
        self.webview.load(QUrl(self.linkItems[index.row()]))

    def setLinks(self, index):

        print "setLinks clicked %s "%index.row()


    def addSite(self):

        print "addSiteClicked"

    def removeSite(self):

        print "removeSiteClicked"


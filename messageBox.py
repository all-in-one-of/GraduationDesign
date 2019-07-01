#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: mcc
# filename:messageBox
# datetime:2019/5/8 19:21
from PySide import QtGui
class MyMessageBox(QtGui.QMessageBox):
    def __init__(self,parent,stdstr=None):
        super(MyMessageBox,self).__init__(parent)
        self.InitUI(parent,stdstr)

    def InitUI(self,parent,stdstr):
        if stdstr:
            self.information(parent, "Error", u"渲染失败请检查设置")
        else:
            self.information(parent, "Message", u"渲染结束")


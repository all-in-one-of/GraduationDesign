#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: mcc
# filename:deskTopCenter
# datetime:2019/5/8 20:02
from PySide import QtGui, QtCore
class DeskTopCenter(QtGui.QWidget):
    def __init__(self,parent=None):
        super(DeskTopCenter, self).__init__(parent)
        self.initUI(parent)
    def initUI(self,parent):
        # 获得窗口的数据,PySide.QtCore.QRect
        qr = parent.frameGeometry()
        # 获得本机可视窗口的中心点坐标
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        # 将QRect移动到中心点
        qr.moveCenter(cp)
        # 用模拟矩形得到的位置，将窗口本身移动到中心点
        parent.move(qr.topLeft())

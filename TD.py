# -*- coding: utf-8 -*-
import sys
import os
import json
import glob
import subprocess
try: 
    from PySide import QtGui
    from PySide import QtCore
except ImportError:
    from PySide2 import QtWidgets as QtGui
    from PySide2 import QtGui as QtGui1
    from PySide2 import QtCore
 #from PySide import QtGui,QtCore
from _Qss import qss
import messageBox as message
import deskTopCenter as center
HOUDINIEXE = r"D:\Program Files\houdini16.5\bin\hython.exe"
Path_File=os.path.dirname(os.path.realpath("render.py"))
path=Path_File+"/"+"File"
Path = os.path.dirname(os.path.realpath("render.py"))
def gci(path):#获取制定路径下的所有文件夹的名称
    parents = os.listdir(path)
    return parents

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.Init()

    def Init(self):
        self.setWindowTitle(u'预渲染工具v0.1')
        self.setGeometry(500,100,500,600)
        self.label_project = QtGui.QLabel(u'项目')
        self.ComboBox_project = QtGui.QComboBox()

        self.label_sequence = QtGui.QLabel(u'场  ')
        self.ComboBox_sequence = QtGui.QComboBox()

        self.label_shot = QtGui.QLabel(u'镜头  ')
        self.ComboBox_shot = QtGui.QComboBox()

        self.label_zichan = QtGui.QLabel(u'资产:')
        self.label_animation = QtGui.QLabel(u'动画')
        self.ComboBox_animation = QtGui.QComboBox()

        self.label_comp = QtGui.QLabel(u'合成')
        self.ComboBox_comp = QtGui.QComboBox()

        self.label_FX = QtGui.QLabel(u'特效')
        self.ComboBox_FX = QtGui.QComboBox()

        self.label_light = QtGui.QLabel(u"灯光")
        self.ComboBox_light = QtGui.QComboBox()

        self.label_layout = QtGui.QLabel("layout")
        self.ComboBox_layout = QtGui.QComboBox()

        self.label_engine = QtGui.QLabel(u'渲染方式')
        self.ComboBox_engine = QtGui.QComboBox()
        self.ComboBox_engine.addItems(
            ["...Choose...", "micropoly", "raytrace", "pbrmicropoly", "pbrraytrace", "photon"])
        self.ComboBox_engine.setMinimumWidth(500)
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        self.label_resultion = QtGui.QLabel(u"分辨率 :")
        self.resultion_edit = QtGui.QLineEdit()
        #self.resultion_edit.setValidator(QtGui1.QIntValidator())
        self.label_hight = QtGui.QLabel("  *   ")
        self.resultion_edit1 = QtGui.QLineEdit()
        #self.resultion_edit1.setValidator(QtGui1.QIntValidator())

        self.label_start_frame = QtGui.QLabel(u"开始帧 :")
        self.start_frame_edit = QtGui.QLineEdit()
        #self.start_frame_edit.setValidator(QtGui1.QIntValidator())

        self.label_end_frame = QtGui.QLabel(u"结束帧")
        self.end_frame_edit = QtGui.QLineEdit()
        #self.end_frame_edit.setValidator(QtGui1.QIntValidator())

        self.label_save = QtGui.QLabel(u"输出路径")
        self.save_edit = QtGui.QLineEdit()
        Button = QtGui.QPushButton(u"选择")
        Button.clicked.connect(self.save_Button)

        label_refreshButton = QtGui.QPushButton(u"刷新")
        label_refreshButton.clicked.connect(self.refreshButton)

        # matBtn = QtGui.QPushButton(u"赋予材质")
        # matBtn.clicked.connect(self.setMat)

        label_okButton = QtGui.QPushButton(u'渲染')
        label_okButton.setGeometry(QtCore.QRect(4, 18, 31, 2))
        label_okButton.clicked.connect(self.Render_Button)

        label_cancleButton = QtGui.QPushButton(u'取消')
        label_cancleButton.clicked.connect(self.Cancle_Button)

        projectLayout = QtGui.QFormLayout()
        projectLayout.addRow(self.label_project,self.ComboBox_project)
        projectLayout.addRow(self.label_animation,self.ComboBox_animation)

        sequenceLayout = QtGui.QFormLayout()
        sequenceLayout.addRow(self.label_sequence,self.ComboBox_sequence)
        sequenceLayout.addRow(self.label_FX,self.ComboBox_FX)

        shotLayout = QtGui.QFormLayout()
        shotLayout.addRow(self.label_shot,self.ComboBox_shot)
        shotLayout.addRow(self.label_layout,self.ComboBox_layout)

        renderStyles = QtGui.QHBoxLayout()
        renderStyles.addWidget(self.label_engine)
        renderStyles.addWidget(self.ComboBox_engine)
        renderStyles.addStretch()

        fristRowLayout = QtGui.QHBoxLayout()
        fristRowLayout.addLayout(projectLayout)
        fristRowLayout.addSpacing(10)
        fristRowLayout.addLayout(sequenceLayout)
        fristRowLayout.addSpacing(10)
        fristRowLayout.addLayout(shotLayout)

        secondRowLayout = QtGui.QHBoxLayout()
        secondRowLayout.addSpacing(10)
        secondRowLayout.addSpacing(10)

        thirdRowLayout = QtGui.QHBoxLayout()
        thirdRowLayout.addWidget(self.label_resultion)
        thirdRowLayout.addWidget(self.resultion_edit)
        thirdRowLayout.addWidget(self.label_hight)
        thirdRowLayout.addWidget(self.resultion_edit1)
        fourthRowLayout = QtGui.QHBoxLayout()
        fourthRowLayout.addWidget(self.label_start_frame)
        fourthRowLayout.addWidget(self.start_frame_edit)

        fourthRowLayout.addWidget(self.label_end_frame)
        fourthRowLayout.addWidget(self.end_frame_edit)
        fivethRowLayout = QtGui.QHBoxLayout()
        fivethRowLayout.addWidget(self.label_save)
        fivethRowLayout.addWidget(self.save_edit)
        fivethRowLayout.addWidget(Button)

        sixthRowLayout = QtGui.QHBoxLayout()
        sixthRowLayout.addWidget(label_refreshButton)
        #sixthRowLayout.addWidget(matBtn)
        sixthRowLayout.addWidget(label_okButton)
        sixthRowLayout.addWidget(label_cancleButton)

        lastLayout = QtGui.QVBoxLayout()
        lastLayout.addSpacing(10)
        lastLayout.addLayout(fristRowLayout)
        lastLayout.addLayout(secondRowLayout)
        lastLayout.addWidget(self.label_zichan)
        lastLayout.addWidget(self.treeWidget)
        lastLayout.addLayout(thirdRowLayout)
        lastLayout.addLayout(fourthRowLayout)
        lastLayout.addLayout(renderStyles)
        lastLayout.addLayout(fivethRowLayout)
        lastLayout.addLayout(sixthRowLayout)
        self.setLayout(lastLayout)
        center.DeskTopCenter(self)

    # def setMat(self):
    #     pass

    def refreshButton(self):
        def gci(path):
            parents = os.listdir(path)
            return parents
        project_pos = gci(path)
        project_choose = ["...Choose..."]
        project_list = project_choose + project_pos
        self.ComboBox_project.addItems(project_list)
        self.ComboBox_project.currentIndexChanged.connect(self.sequence)

    def sequence(self):
        self.ComboBox_sequence.clear()
        self.project_chose=self.ComboBox_project.currentText()
        self.path_sequence=path+"/"+self.project_chose
        sequence_pos = gci(self.path_sequence)
        sequence_choose = ["...Choose..."]
        sequence_list = sequence_choose + sequence_pos
        self.ComboBox_sequence.addItems(sequence_list)
        self.ComboBox_sequence.currentIndexChanged.connect(self.shot)

    def shot(self):
        self.ComboBox_shot.clear()
        self.sequence=self.ComboBox_sequence.currentText()
        self.path_shot=self.path_sequence+"/"+self.sequence
        shot_pos = gci(self.path_shot)
        shot_choose = ["...Choose..."]
        shot_list = shot_choose + shot_pos
        self.ComboBox_shot.addItems(shot_list)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_animition)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_comp)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_FX)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_layout)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_light)
        self.ComboBox_shot.currentIndexChanged.connect(self.child1_func)

    def list_animition(self):
        self.animition=self.ComboBox_shot.currentText()
        self.path_animition=self.path_shot+"/"+self.animition
        self.list_pos = gci(self.path_animition)
        self.animition_pos=self.path_animition+"/"+self.list_pos[0]
        for root, dirs, files in os.walk(str(self.animition_pos)):
            if(len(files)==0):
                empty=True
                self.ComboBox_animation.addItem("empty")
            else:
                self.Animation_pos = gci(self.animition_pos)
                animation_choose = ["...Choose..."]
                filename_list=[]
                for parent, dirnames, filenames in os.walk(str(self.animition_pos)):
                    for filename in filenames:
                        filename_list.append(filename)

                    for i in range(0,len(filename_list)):
                        animation_choose.append("Animation_00"+str(i+1))
                    self.ComboBox_animation.addItems(animation_choose)
                    self.ComboBox_animation.currentIndexChanged.connect(self.animation)
    # 查找动画文件函数
    def animation(self):
        self.index=self.ComboBox_animation.currentIndex()
        self.animition = self.ComboBox_shot.currentText()
        self.path_animition = self.path_shot + "/" + self.animition

        self.list_pos = gci(self.path_animition)
        self.animition_pos = self.path_animition + "/" + self.list_pos[0]

        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.animition_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Animation_file= filename_list[self.index-1]
            self.Path_pos_animation=self.animition_pos+"/"+Animation_file
        print self.Path_pos_animation

    def list_comp(self):
        self.comp_name=self.ComboBox_shot.currentText()
        self.path_comp=self.path_shot+"/"+self.comp_name
        self.list_pos = gci(self.path_comp)
        self.comp_pos=self.path_comp+"/"+self.list_pos[2]
        for root, dirs, files in os.walk(str(self.comp_pos)):
            if(len(files)==0):
                empty=True
                self.ComboBox_comp.addItem("empty")
            else:
                self.Comp_pos = gci(self.comp_pos)

                comp_choose = ["...Choose..."]
                filename_list=[]
                for parent, dirnames, filenames in os.walk(str(self.comp_pos)):
                    for filename in filenames:
                        filename_list.append(filename)

                    for i in range(0,len(filename_list)):
                        comp_choose.append("Comp_00"+str(i+1))
                    self.ComboBox_comp.addItems(comp_choose)
                    self.ComboBox_comp.currentIndexChanged.connect(self.comp)
    def comp(self):
        self.index = self.ComboBox_comp.currentIndex()
        self.comp_name = self.ComboBox_shot.currentText()
        self.path_comp = self.path_shot + "/" + self.comp_name
        self.list_pos = gci(self.path_comp)
        self.comp_pos = self.path_comp + "/" + self.list_pos[2]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.comp_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Comp_file = filename_list[self.index - 1]
            self.Path_pos_comp = self.animition_pos + "/" + Comp_file
        print self.Path_pos_comp

    def list_FX(self):
        self.FX_name=self.ComboBox_shot.currentText()
        self.path_FX=self.path_shot+"/"+self.FX_name
        self.list_pos = gci(self.path_FX)
        self.fx_pos=self.path_FX+"/"+self.list_pos[3]
        for root, dirs, files in os.walk(str(self.fx_pos)):
            if(len(files)==0):
                empty=True
                self.ComboBox_FX.addItem("empty")
            else:
                self.FX_pos = gci(self.fx_pos)
                Fx_choose = ["...Choose..."]
                filename_list = []
                for parent, dirnames, filenames in os.walk(str(self.fx_pos)):
                    for filename in filenames:
                        filename_list.append(filename)

                    for i in range(0, len(filename_list)):
                        Fx_choose.append("Fx_00" + str(i + 1))
                    self.ComboBox_FX.addItems(Fx_choose)
                    self.ComboBox_FX.currentIndexChanged.connect(self.FX)
    # 查找FX文件函数
    def FX(self):
        self.index=self.ComboBox_FX.currentIndex()
        self.FX_name = self.ComboBox_shot.currentText()
        self.path_FX = self.path_shot + "/" + self.FX_name
        self.list_pos = gci(self.path_FX)
        self.comp_pos = self.path_FX + "/" + self.list_pos[3]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.fx_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Fx_file = filename_list[self.index - 1]
            self.Path_pos_FX = self.comp_pos + "/" + Fx_file
            print self.Path_pos_FX

    def list_layout(self):
        self.layout_name=self.ComboBox_shot.currentText()
        self.path_layout=self.path_shot+"/"+self.layout_name
        self.list_pos = gci(self.path_layout)
        self.layout_pos=self.path_layout+"/"+self.list_pos[4]
        for root, dirs, files in os.walk(str(self.layout_pos)):
            if(len(files)==0):
                empty=True
                self.ComboBox_layout.addItem("empty")
            else:
                self.Layout_pos = gci(self.layout_pos)
                Layout_choose = ["...Choose..."]
                filename_list = []
                for parent, dirnames, filenames in os.walk(str(self.layout_pos)):
                    for filename in filenames:
                        filename_list.append(filename)

                    for i in range(0, len(filename_list)):


                        Layout_choose.append("Layout_00" + str(i + 1))
                    self.ComboBox_layout.addItems(Layout_choose)
                    self.ComboBox_layout.currentIndexChanged.connect(self.layout)

    # 查找layout文件函数
    def layout(self):
        self.index = self.ComboBox_layout.currentIndex()
        self.layout_name = self.ComboBox_shot.currentText()
        self.path_layout = self.path_shot + "/" + self.layout_name
        def gci(path):
            parents = os.listdir(path)
            return parents

        self.list_pos = gci(self.path_layout)
        self.layout_pos = self.path_layout + "/" + self.list_pos[4]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.layout_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Layout_file = filename_list[self.index - 1]
            self.Path_pos_layout = self.layout_pos + "/" + Layout_file
            print self.Path_pos_layout

    def list_light(self):
        self.light_name=self.ComboBox_shot.currentText()
        self.path_light=self.path_shot+"/"+self.light_name
        self.list_pos = gci(self.path_light)
        self.light_pos=self.path_light+"/"+self.list_pos[5]
        for root, dirs, files in os.walk(str(self.light_pos)):
            if(len(files)==0):
                empty=True
                self.ComboBox_light.addItem("empty")
            else:
                self.Light_pos = gci(self.light_pos)
                Light_choose = ["...Choose..."]
                filename_list = []
                for parent, dirnames, filenames in os.walk(str(self.light_pos)):
                    for filename in filenames:
                        filename_list.append(filename)

                    for i in range(0, len(filename_list)):
                        Light_choose.append("Light_00" + str(i + 1))
                    self.ComboBox_light.addItems(Light_choose)
                    self.ComboBox_light.currentIndexChanged.connect(self.light)
    #查找灯光文件函数
    def light(self):
        self.index = self.ComboBox_light.currentIndex()
        self.light_name = self.ComboBox_shot.currentText()
        self.path_light = self.path_shot + "/" + self.light_name
        self.list_pos = gci(self.path_light)
        self.light_pos = self.path_light + "/" + self.list_pos[5]

        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.light_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Light_file = filename_list[self.index - 1]
            self.Path_pos_light = self.light_pos + "/" + Light_file
            print self.Path_pos_light

    def child1_func(self):
        self.treeWidget.clear()
        self.animition = self.ComboBox_shot.currentText()
        self.path_animition = self.path_shot + "/" + self.animition
        self.list_pos = gci(self.path_animition)

        print "list_pos==============:",self.list_pos
        self.assets_pos = self.path_animition + "/" + self.list_pos[1]
        for root, dirs, files in os.walk(str(self.assets_pos)):
            if (len(files) == 0):
                pass
                empty = True
                
            else:
                print "++++++++++++++++++",self.assets_pos
                self.Assets_pos = gci(self.assets_pos)

                filename_list = []
                for parent, dirnames, filenames in os.walk(str(self.assets_pos)):
                    for filename in filenames:
                        filename_list.append(filename)
                    self.root = QtGui.QTreeWidgetItem(self.treeWidget)
                    self.root.setText(0, 'Assets')
                    for i in range(0, len(filename_list)):
                        self.treeWidget.setColumnCount(2)
                        self.treeWidget.setHeaderLabels(['Name', 'Files'])
                        self.treeWidget.setColumnWidth(0,200)
                        self.child1 = QtGui.QTreeWidgetItem(self.root)
                        self.child1.setText(1,self.Assets_pos[i])
                    self.treeWidget.itemSelectionChanged.connect(self.assets_func)

    # 获得资产文件路径名
    def assets_func(self):
        self.Assets_path=[]
        selectedItemList=self.treeWidget.selectedItems()
        for items in selectedItemList:
            self.Assets_path.append("%s/%s"%(self.assets_pos,items.text(1)))

        print self.Assets_path
    #选择按钮连接函数
    def save_Button(self):
        save_name=QtGui.QFileDialog.getSaveFileName(self)
        print "save_name:",save_name
        self.save_edit.setText(str(save_name[0]))

    #取消按钮连接函数
    def Cancle_Button(self):
        self.close()

    #渲染按钮连接函数
    def Render_Button(self):
        start_frame = self.start_frame_edit.text()
        end_frame = self.end_frame_edit.text()
        renderengine = self.ComboBox_engine.currentText()
        resultion_wight = self.resultion_edit.text()
        resultion_hight = self.resultion_edit1.text()
        pathName = self.save_edit.text()

        if (self.ComboBox_animation.currentText() == "...Choose..." or self.ComboBox_animation.currentText() == "empty"):
            self.Path_pos_animation = []
        if (self.ComboBox_comp.currentText() == "...Choose..." or self.ComboBox_comp.currentText()=="empty"):
            self.Path_pos_comp = []
        if (self.ComboBox_FX.currentText() == "...Choose..." or self.ComboBox_FX.currentText() == "empty"):
            self.Path_pos_FX = []
        if (self.ComboBox_layout.currentText() == "...Choose..." or self.ComboBox_layout.currentText() == "empty"):
            self.Path_pos_layout = []
        if (self.ComboBox_light.currentText() == "...Choose..." or self.ComboBox_light.currentText() == "empty"):
            self.Path_pos_light = []

        if self.treeWidget.selectedItems()==[]:
            self.Assets_path = []

        dict_all = {"animation": self.Path_pos_animation, "comp": self.Path_pos_comp,
                    "FX": self.Path_pos_FX,
                    "layout":self.Path_pos_layout,"light":self.Path_pos_light,"renderengine":renderengine,
                    "assets":self.Assets_path,
                    "camera_resultion_wight":resultion_wight, "camera_resultion_hight":resultion_hight,
                    "start_frame": start_frame, "end_frame": end_frame, "save_pos": (pathName)+".$F4.jpeg"}

        with open("dir.json", "w") as film:
            end = json.dumps(dict_all, indent=4)
            film.write(end)
        command = '"%s" %s/render.py'%(HOUDINIEXE,Path)
        mytask = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdstr = mytask.stdout.read()
        if stdstr:
            pass
        else:
            message.MyMessageBox(self,mytask.poll())

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    ex.setStyleSheet(qss)
    ex.show()
    sys.exit(app.exec_())

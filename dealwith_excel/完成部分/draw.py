# -*- coding: utf-8 -*-   
from PyQt4.QtCore import *  
from PyQt4.QtGui import *  
import sys  

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  



  
class InputDlg(QDialog):  
    def __init__(self,parent=None):  
        super(InputDlg,self).__init__(parent)  
  
        label1=QLabel(self.tr(".xls path"))  
        label2=QLabel(self.tr("sex"))  
        label3=QLabel(self.tr("age"))  
        label4=QLabel(self.tr("height"))  
  
        self.nameLabel=QLabel(" ") #显示.xls路径  
        self.nameLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)  
        self.sexLabel=QLabel(self.tr("male"))  
        self.sexLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)  
        self.ageLabel=QLabel("25")  
        self.ageLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)  
        self.statureLabel=QLabel("168")  
        self.statureLabel.setFrameStyle(QFrame.Panel|QFrame.Sunken)  
  
        nameButton=QPushButton("...")  
        sexButton=QPushButton("...")  
        ageButton=QPushButton("...")  
        statureButton=QPushButton("...")  
  
        self.connect(nameButton,SIGNAL("clicked()"),self.slotName)  
        self.connect(sexButton,SIGNAL("clicked()"),self.slotSex)  
        self.connect(ageButton,SIGNAL("clicked()"),self.slotAge)  
        self.connect(statureButton,SIGNAL("clicked()"),self.slotStature)  
  
        layout=QGridLayout()  
        layout.addWidget(label1,0,0)  
        layout.addWidget(self.nameLabel,0,1)  
        layout.addWidget(nameButton,0,2)  
        layout.addWidget(label2,1,0)  
        layout.addWidget(self.sexLabel,1,1)  
        layout.addWidget(sexButton,1,2)  
        layout.addWidget(label3,2,0)  
        layout.addWidget(self.ageLabel,2,1)  
        layout.addWidget(ageButton,2,2)  
        layout.addWidget(label4,3,0)  
        layout.addWidget(self.statureLabel,3,1)  
        layout.addWidget(statureButton,3,2)  
  
        self.setLayout(layout)  
  
        self.setWindowTitle(self.tr("colect data"))  
  
    def slotName(self):  
        name,ok=QInputDialog.getText(self,self.tr("user name"),QLineEdit.Normal,self.nameLabel.text())  
        if ok and (not name.isEmpty()):  
           self.nameLabel.setText(name)  
    #def slotName( self ):
    #   openfile_ch= u'打开'
    #   fileNamedir = QtGui.QFileDialog.getOpenFileName( self, openfile_ch )
    #    print fileNamedir
    #   self.fileNamedir=fileNamedir #获取文件路径


	
    def slotSex(self):  
        list=QStringList()  
        list.append(self.tr("male"))  
        list.append(self.tr("female"))  
        sex,ok=QInputDialog.getItem(self,self.tr("sex"),self.tr("please choice"),list)  
  
        if ok:  
            self.sexLabel.setText(sex)  
  
    def slotAge(self):  
        age,ok=QInputDialog.getInteger(self,self.tr("age"),  
                                       self.tr("input name:"),  
                                       int(self.ageLabel.text()),0,150)  
        if ok:  
            self.ageLabel.setText(str(age))  
  
    def slotStature(self):  
        stature,ok=QInputDialog.getDouble(self,self.tr("height"),  
                                          self.tr("input height:"),  
                                          float(self.statureLabel.text()),0,2300.00)  
        if ok:  
            self.statureLabel.setText(str(stature))  
  
app=QApplication(sys.argv)  
form=InputDlg()  
form.show()  
app.exec_()  
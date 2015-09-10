#__*__ coding:utf-8 __*__
import xlrd
import xlwt
import os
import shutil   #复制文件


import sys
reload(sys)  
sys.setdefaultencoding('utf8')

from PyQt4 import QtGui, QtCore

#http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html 此网站给出获取sheetname的方法


class MyFunc(object):
    def __init__(self):
        self.filepath=None   #路径
        self.fextension=None #扩展名
        self.filename=None	 #文件名

	#获取文件路径
	#路经非空返回true
    def getfilepath(self,getfpath=None):
        self.filepath=getfpath
        if self.filepath:
            self.fextension=self.filepath.split(".")[-1] #文件后缀
            self.filename=self.filepath.split("/")[-1]   #文件名
            return True
        else:
            return False

    #判断文件后缀
    def isxlsfile(self):
        if self.filepath and (self.fextension=='xls'):
            return True
        else:
            return False

    #获取表单
    def getsheet(self):
        if self.filepath and (self.fextension=='xls'):
            data = xlrd.open_workbook(self.filepath)
            #table = data.sheets()[0]          #通过索引顺序获取
            table=data.sheet_names()
            for x in table:
                print x    
            #table = data.sheet_by_index(0) #通过索引顺序获取
            return table
        else:
            return False



class MyProgess(QtGui.QDialog):  
    def __init__(self,parent=None):  
        super(MyProgess,self).__init__(parent)  
        self.setWindowTitle(self.tr("please use bar"))   #使用进度条
        typeLabel=QtGui.QLabel("Sheet选择".decode("GBK"))     #显示类型
        self.typeComboBox=QtGui.QComboBox()
        choicebutton_ch='选择'.decode("GBK")
        startPushButton=QtGui.QPushButton(choicebutton_ch)  #开始
        layout=QtGui.QGridLayout()  
        layout.addWidget(typeLabel,1,0)  
        layout.addWidget(self.typeComboBox,1,1)  
        layout.addWidget(startPushButton,3,1)  
        layout.setMargin(30)  
        layout.setSpacing(50) 
        self.setLayout(layout)  
          
        self.connect(startPushButton,QtCore.SIGNAL("clicked()"),self.slotStart)  
  
    def slotStart(self):
        self.indexnum=self.typeComboBox.currentIndex() #self.indexnum为选定的sheetindex
        #print '%s'%self.indexnum
        self.done(1)
    def myQComboBox(self,sheetname):
        for x in sheetname:
            self.typeComboBox.addItem(x)
            #self.typeComboBox.addItem(self.tr("sheet1")) 

    #信息弹窗
    def slotInformation(self,info_ch):  
        QtGui.QMessageBox.information(self,"提示窗".decode("GBK"),info_ch.decode("GBK")) 


class MyWindow( QtGui.QWidget ):
    def __init__( self ):
        super( MyWindow, self ).__init__()
        self.setGeometry(800,500,400,300)  #设置窗口在屏幕的位置x，y和窗口本身大小w，h
        appname_ch='Excel信息处理'.decode("GBK") 
        self.setWindowTitle( appname_ch )
        self.setWindowIcon(QtGui.QIcon('Icon/tubiao_32.ico'))
        #self.resize( 500, 500 )  #窗口大小
        self.exesheet=False   #sheet框选择
        self.myfunc=MyFunc()  #函数功能

        gridlayout = QtGui.QGridLayout()
        addexcel_ch='添加.xls文件'.decode("GBK") 
        sheetchoice_ch='选择Sheet'.decode("GBK")
        executefile_ch='执行'.decode("GBK")
        quit_ch='退出'.decode("GBK")
        self.button1 = QtGui.QPushButton( addexcel_ch )
        self.button2 = QtGui.QPushButton( sheetchoice_ch )
        self.button3 = QtGui.QPushButton( executefile_ch )
        self.button4 = QtGui.QPushButton( quit_ch )
        gridlayout.addWidget( self.button1 )
        gridlayout.addWidget( self.button2 )
        gridlayout.addWidget( self.button3 )
        gridlayout.addWidget( self.button4 )
        spacer = QtGui.QSpacerItem( 200, 80 )
        gridlayout.addItem( spacer, 3, 1, 1, 3 )
        self.setLayout( gridlayout )
         
        self.connect( self.button1, QtCore.SIGNAL( 'clicked()' ), self.OnButton1 )
        self.connect( self.button2, QtCore.SIGNAL( 'clicked()' ), self.OnButton2 )
        self.connect( self.button3, QtCore.SIGNAL( 'clicked()' ), self.OnButton3 )
        self.connect( self.button4, QtCore.SIGNAL( 'clicked()' ), QtGui.qApp, QtCore.SLOT('quit()')) #退出操作
         
    #导入xls函数     
    def OnButton1( self ):
        openfile_ch= '打开.xls'.decode("GBK")
        self.filepath = QtGui.QFileDialog.getOpenFileName( self, openfile_ch )  #文件路径

        if self.filepath.split(".")[-1]=='xls': #文件后缀
            
            self.myfunc.getfilepath(self.filepath)
        elif self.filepath:
            process = MyProgess()
            process.slotInformation('请导入.xls文件类型')

    
	#表单函数
    def OnButton2( self ):
        self.sheetname=self.myfunc.getsheet()
        #process = MyProgess()       # 创建对话框对象
        if self.myfunc.isxlsfile():
            process = MyProgess()       # 创建对话框对象
            process.myQComboBox(self.sheetname)
            process.exec_()         # 运行对话框
            self.choicesheet = process.indexnum
            self.exesheet=True
        else:
            process = MyProgess()
            process.slotInformation('请先导入.xls文件')
    
	#执行函数
    def OnButton3( self ):
        if self.myfunc.isxlsfile():
            if not self.exesheet:
                process = MyProgess()
                process.slotInformation('请先选择sheet表单')
            else:
                pass#执行excel文档操作！！！（主要功能实现）
        else:
            process = MyProgess()
            process.slotInformation('请先导入.xls文件')
        

         
app = QtGui.QApplication( sys.argv )
win = MyWindow()
win.show()
app.exec_()
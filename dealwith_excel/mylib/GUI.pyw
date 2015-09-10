#__*__ coding:utf-8 __*__
import xlrd
import xlwt
import os
import shutil   #�����ļ�


import sys
reload(sys)  
sys.setdefaultencoding('utf8')

from PyQt4 import QtGui, QtCore

#http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html ����վ������ȡsheetname�ķ���


class MyFunc(object):
    def __init__(self):
        self.filepath=None   #·��
        self.fextension=None #��չ��
        self.filename=None	 #�ļ���

	#��ȡ�ļ�·��
	#·���ǿշ���true
    def getfilepath(self,getfpath=None):
        self.filepath=getfpath
        if self.filepath:
            self.fextension=self.filepath.split(".")[-1] #�ļ���׺
            self.filename=self.filepath.split("/")[-1]   #�ļ���
            return True
        else:
            return False

    #�ж��ļ���׺
    def isxlsfile(self):
        if self.filepath and (self.fextension=='xls'):
            return True
        else:
            return False

    #��ȡ��
    def getsheet(self):
        if self.filepath and (self.fextension=='xls'):
            data = xlrd.open_workbook(self.filepath)
            #table = data.sheets()[0]          #ͨ������˳���ȡ
            table=data.sheet_names()
            for x in table:
                print x    
            #table = data.sheet_by_index(0) #ͨ������˳���ȡ
            return table
        else:
            return False



class MyProgess(QtGui.QDialog):  
    def __init__(self,parent=None):  
        super(MyProgess,self).__init__(parent)  
        self.setWindowTitle(self.tr("please use bar"))   #ʹ�ý�����
        typeLabel=QtGui.QLabel("Sheetѡ��".decode("GBK"))     #��ʾ����
        self.typeComboBox=QtGui.QComboBox()
        choicebutton_ch='ѡ��'.decode("GBK")
        startPushButton=QtGui.QPushButton(choicebutton_ch)  #��ʼ
        layout=QtGui.QGridLayout()  
        layout.addWidget(typeLabel,1,0)  
        layout.addWidget(self.typeComboBox,1,1)  
        layout.addWidget(startPushButton,3,1)  
        layout.setMargin(30)  
        layout.setSpacing(50) 
        self.setLayout(layout)  
          
        self.connect(startPushButton,QtCore.SIGNAL("clicked()"),self.slotStart)  
  
    def slotStart(self):
        self.indexnum=self.typeComboBox.currentIndex() #self.indexnumΪѡ����sheetindex
        #print '%s'%self.indexnum
        self.done(1)
    def myQComboBox(self,sheetname):
        for x in sheetname:
            self.typeComboBox.addItem(x)
            #self.typeComboBox.addItem(self.tr("sheet1")) 

    #��Ϣ����
    def slotInformation(self,info_ch):  
        QtGui.QMessageBox.information(self,"��ʾ��".decode("GBK"),info_ch.decode("GBK")) 


class MyWindow( QtGui.QWidget ):
    def __init__( self ):
        super( MyWindow, self ).__init__()
        self.setGeometry(800,500,400,300)  #���ô�������Ļ��λ��x��y�ʹ��ڱ����Сw��h
        appname_ch='Excel��Ϣ����'.decode("GBK") 
        self.setWindowTitle( appname_ch )
        self.setWindowIcon(QtGui.QIcon('Icon/tubiao_32.ico'))
        #self.resize( 500, 500 )  #���ڴ�С
        self.exesheet=False   #sheet��ѡ��
        self.myfunc=MyFunc()  #��������

        gridlayout = QtGui.QGridLayout()
        addexcel_ch='���.xls�ļ�'.decode("GBK") 
        sheetchoice_ch='ѡ��Sheet'.decode("GBK")
        executefile_ch='ִ��'.decode("GBK")
        quit_ch='�˳�'.decode("GBK")
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
        self.connect( self.button4, QtCore.SIGNAL( 'clicked()' ), QtGui.qApp, QtCore.SLOT('quit()')) #�˳�����
         
    #����xls����     
    def OnButton1( self ):
        openfile_ch= '��.xls'.decode("GBK")
        self.filepath = QtGui.QFileDialog.getOpenFileName( self, openfile_ch )  #�ļ�·��

        if self.filepath.split(".")[-1]=='xls': #�ļ���׺
            
            self.myfunc.getfilepath(self.filepath)
        elif self.filepath:
            process = MyProgess()
            process.slotInformation('�뵼��.xls�ļ�����')

    
	#������
    def OnButton2( self ):
        self.sheetname=self.myfunc.getsheet()
        #process = MyProgess()       # �����Ի������
        if self.myfunc.isxlsfile():
            process = MyProgess()       # �����Ի������
            process.myQComboBox(self.sheetname)
            process.exec_()         # ���жԻ���
            self.choicesheet = process.indexnum
            self.exesheet=True
        else:
            process = MyProgess()
            process.slotInformation('���ȵ���.xls�ļ�')
    
	#ִ�к���
    def OnButton3( self ):
        if self.myfunc.isxlsfile():
            if not self.exesheet:
                process = MyProgess()
                process.slotInformation('����ѡ��sheet��')
            else:
                pass#ִ��excel�ĵ���������������Ҫ����ʵ�֣�
        else:
            process = MyProgess()
            process.slotInformation('���ȵ���.xls�ļ�')
        

         
app = QtGui.QApplication( sys.argv )
win = MyWindow()
win.show()
app.exec_()
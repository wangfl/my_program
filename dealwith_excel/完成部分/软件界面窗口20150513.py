#__*__ coding:utf-8 __*__
import xlrd
import xlwt
import os
import shutil   #复制文件

import sys
from PyQt4 import QtGui, QtCore



#函数copysrc： 拷贝源文件

def copysrc(fname):
    abs=os.path.abspath('.')  #当前路径
    srcdir=os.path.join(abs,'Import')  #源目录路径
    if not os.path.isdir(srcdir):
        os.makedirs(srcdir)
    #print fname #!!!!!!!!!!!!!!!!!
    src=os.path.join(srcdir,fname)     #源文件路径
    dstdir=os.path.join(abs,'Export')  #目标目录路径
    if not os.path.isdir(dstdir):
        os.makedirs(dstdir)
    shutil.copy(src,dstdir)  #复制源文件
    return os.path.join(dstdir,fname)  #返回拷贝文件所在路径

	
	
#函数dealexcel：载入excel文档
#参数：fname文件名称,shname excel表单名称

def dealexcel(fname,filedir,shname):
	#打开excel文档
    os.chdir(filedir)
    bk = xlrd.open_workbook(fname)
    for m in bk.sheet_names():
        print m
    try:
    #打开sheet1
        sh = bk.sheet_by_name(shname)
    except:
        print "没有找到 %s Sheet" % shname
		#exit()					#此处待测！！！
	#获取行数
    nrows = sh.nrows
	#获取列数
    ncols = sh.ncols
    print '%s,%s'%(nrows,ncols)


class MyDialog(QtGui.QDialog):        # 继承QtGui.QDialog
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.gridlayout = QtGui.QGridLayout()    # 创建布局组件
		self.label = QtGui.QLabel('Input:')    # 创建标签
		self.gridlayout.addWidget(self.label, 0, 0)
		self.edit = QtGui.QLineEdit()      # 创建单行文本框
		self.gridlayout.addWidget(self.edit, 0, 1)
		self.ok = QtGui.QPushButton('Ok')     # 创建Ok按钮
		self.gridlayout.addWidget(self.ok, 1, 0)
		self.cancel = QtGui.QPushButton('Cancel')   # 创建Cancel按钮
		self.gridlayout.addWidget(self.cancel, 1, 1)
		self.setLayout(self.gridlayout)
		self.connect(self.ok,QtCore.SIGNAL('clicked()'),self.OnOk)  # Ok按钮事件
		self.connect(self.cancel,QtCore.SIGNAL('clicked()'),self.OnCancel)  # Cancel按钮事件
	def OnOk(self):           # 处理Ok按钮事件
		self.text = self.edit.text()      # 获取文本框中内容
		self.done(1)          # 结束对话框返回1
	def OnCancel(self):          # 处理Cancel按钮事件
		self.done(0)          # 结束对话框返回0


	

class MyWindow( QtGui.QWidget ):
    def __init__( self ):
        super( Window, self ).__init__()
		#self.getfileName=None  #初始化文件名为空，防止未导入文件即执行
        appname_ch=u'Excel信息处理'
        self.setWindowTitle( appname_ch )
        #self.resize( 500, 500 )  #窗口大小
        self.setGeometry(800,500,400,300)  #设置窗口在屏幕的位置x，y和窗口本身大小w，h
		
        gridlayout = QtGui.QGridLayout()
        addexcel_ch=u'添加.xls文件' 
		sheetchoice_ch=u'选择Sheet'
        self.button1 = QtGui.QPushButton( addexcel_ch )
        self.button2 = QtGui.QPushButton( sheetchoice_ch )
        #self.button3 = QtGui.QPushButton( "Color" )
        gridlayout.addWidget( self.button1 )
        gridlayout.addWidget( self.button2 )
        #gridlayout.addWidget( self.button3 )
        spacer = QtGui.QSpacerItem( 200, 80 )
        gridlayout.addItem( spacer, 3, 1, 1, 3 )
        self.setLayout( gridlayout )
         
        self.connect( self.button1, QtCore.SIGNAL( 'clicked()' ), self.OnButton1 )
        self.connect( self.button2, QtCore.SIGNAL( 'clicked()' ), self.OnButton2 )
        #self.connect( self.button3, QtCore.SIGNAL( 'clicked()' ), self.OnButton3 )
         
         
    def OnButton1( self ):
        openfile_ch= u'打开.xls'
        fileName = QtGui.QFileDialog.getOpenFileName( self, openfile_ch )
        #self.getfileName=fileName  #获取.xls文件名
        #print type(fileName)
        #self.getfileName=os.path.basename(fileName)
        print fileName.split("/")[-1]
	
    def OnButton2( self ):
        



    
    #def OnButton2( self ):
    #    if self.getfileName==None:
            #弹出提示框：‘请先导入.xls文件’
    #    else:
            
			
     
    #def OnButton3( self ):
    #    color = QtGui.QColorDialog.getColor()
    #    if color.isValid():
    #        self.setWindowTitle( color.name() )
	#函数copysrc： 拷贝源文件

         
app = QtGui.QApplication( sys.argv )
win = MyWindow()
win.show()
app.exec_()
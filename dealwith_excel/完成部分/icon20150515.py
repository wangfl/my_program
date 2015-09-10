# __*__ coding:utf-8 __*__

import sys
from PyQt4 import QtGui

class Icon(QtGui.QWidget):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		
		self.setGeometry(300,300,250,150)  #设置窗口在屏幕的位置x，y和窗口本身大小w，h
		self.setWindowTitle('Icon')
		self.setWindowIcon(QtGui.QIcon('Icon/tubiao_32.ico'))
		
app=QtGui.QApplication(sys.argv)
icon=Icon()
icon.show()
sys.exit(app.exec_())
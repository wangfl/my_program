# -*- coding:utf-8 -*-
# file: PyQtDialog.py
#
import sys
from PyQt4 import QtCore, QtGui 
class MyDialog(QtGui.QDialog):        # �̳�QtGui.QDialog
	def __init__(self):
		QtGui.QDialog.__init__(self)
		self.gridlayout = QtGui.QGridLayout()    # �����������
		self.label = QtGui.QLabel('Input:')    # ������ǩ
		self.gridlayout.addWidget(self.label, 0, 0)
		self.edit = QtGui.QLineEdit()      # ���������ı���
		self.gridlayout.addWidget(self.edit, 0, 1)
		self.ok = QtGui.QPushButton('Ok')     # ����Ok��ť
		self.gridlayout.addWidget(self.ok, 1, 0)
		self.cancel = QtGui.QPushButton('Cancel')   # ����Cancel��ť
		self.gridlayout.addWidget(self.cancel, 1, 1)
		self.setLayout(self.gridlayout)
		self.connect(self.ok,QtCore.SIGNAL('clicked()'),self.OnOk)  # Ok��ť�¼�
		self.connect(self.cancel,QtCore.SIGNAL('clicked()'),self.OnCancel)  # Cancel��ť�¼�
	def OnOk(self):           # ����Ok��ť�¼�
		self.text = self.edit.text()      # ��ȡ�ı���������
		self.done(1)          # �����Ի��򷵻�1
	def OnCancel(self):          # ����Cancel��ť�¼�
		self.done(0)          # �����Ի��򷵻�0

class MyWindow(QtGui.QWidget):
	def __init__(self):          # ��ʼ������
		QtGui.QWidget.__init__(self)      # ���ø����ʼ������
		self.setWindowTitle('PyQt')       # ���ô��ڱ���
		self.resize(300,200)        # ���ô��ڴ�С
		gridlayout = QtGui.QGridLayout()     # �����������
		self.button = QtGui.QPushButton('CreateDialog') # ����Button1
		gridlayout.addWidget(self.button, 1, 1)
		self.setLayout(gridlayout)       # �򴰿�����Ӳ������
		self.connect(self.button,QtCore.SIGNAL('clicked()'),self.OnButton) # Button�¼�
	def OnButton(self):          # ����ť�¼�
		dialog = MyDialog()         # �����Ի������
		r = dialog.exec_()         # ���жԻ���
		if r:
			self.button.setText(dialog.text)

app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
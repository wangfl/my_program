#__*__ coding:utf-8 __*__
import os


abs = os.path.abspath('.')  #当前路径
print abs
sourcedir = os.path.join(abs,'Source')  #安装模块录路径
sourcedir_pyqt = os.path.join(sourcedir,'openpyxl-2.2.2')  #安装模块xlutils路径
sourcedir_pyqtexe = os.path.join(sourcedir_pyqt,'setup.py install')  #安装模块xlutils路径
#execfile(sourcedir_pyqtexe)
#cmd =r'cmd.exe /k '+sourcedir_pyqtexe
#cmd =r'cmd.exe /k '+sourcedir_pyqtexe
#os.system(r'cmd.exe /k sourcedir_pyqtexe')
os.system(sourcedir_pyqtexe)
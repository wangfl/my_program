#__*__ coding:utf-8 __*__
import os


abs = os.path.abspath('.')  #��ǰ·��
print abs
sourcedir = os.path.join(abs,'Source')  #��װģ��¼·��
sourcedir_pyqt = os.path.join(sourcedir,'openpyxl-2.2.2')  #��װģ��xlutils·��
sourcedir_pyqtexe = os.path.join(sourcedir_pyqt,'setup.py install')  #��װģ��xlutils·��
#execfile(sourcedir_pyqtexe)
#cmd =r'cmd.exe /k '+sourcedir_pyqtexe
#cmd =r'cmd.exe /k '+sourcedir_pyqtexe
#os.system(r'cmd.exe /k sourcedir_pyqtexe')
os.system(sourcedir_pyqtexe)
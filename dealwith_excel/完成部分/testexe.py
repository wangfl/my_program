#__*__ coding:utf-8 __*__
import os
import sys


fpath = os.path.join(sys.prefix,'Lib')             #��ȡpython��Lib·��
findpath = os.path.join(fpath,'site-packages')     #��ȡ·��..Python27\Lib\site-packages·��
findpath_pyqt = os.path.join(findpath,'PyQt4')                    #��ȡPyQt4·��

if os.path.isdir(findpath_pyqt):

    abs = os.path.abspath('.')  #��ǰ·��
    sourcedir = os.path.join(abs,'Source')  #��װģ��¼·��
    sourcedir_pyqt = os.path.join(sourcedir,'Pyqt')  #��װģ��xlutils·��
    sourcedir_pyqtexe = os.path.join(sourcedir_pyqt,'PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x32.exe')  #��װģ��xlutils·��
    os.system(sourcedir_pyqtexe)
#__*__ coding:utf-8 __*__
import os
import sys


fpath = os.path.join(sys.prefix,'Lib')             #获取python下Lib路径
findpath = os.path.join(fpath,'site-packages')     #获取路径..Python27\Lib\site-packages路径
findpath_pyqt = os.path.join(findpath,'PyQt4')                    #获取PyQt4路径

if os.path.isdir(findpath_pyqt):

    abs = os.path.abspath('.')  #当前路径
    sourcedir = os.path.join(abs,'Source')  #安装模块录路径
    sourcedir_pyqt = os.path.join(sourcedir,'Pyqt')  #安装模块xlutils路径
    sourcedir_pyqtexe = os.path.join(sourcedir_pyqt,'PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x32.exe')  #安装模块xlutils路径
    os.system(sourcedir_pyqtexe)
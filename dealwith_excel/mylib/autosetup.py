#__*__ coding:utf-8 __*__
import os
import sys

fpath = os.path.join(sys.prefix,'Lib')             #sys.prefix 获取python安装路径
print fpath
findpath = os.path.join(fpath,'site-packages')     
findpath_xlrd = os.path.join(findpath,'xlrd')                        #获取xlrd路径
findpath_xlwt = os.path.join(findpath,'xlwt-1.0.0-py2.7.egg')        #获取xlwt路径
findpath_xlutils = os.path.join(findpath,'xlutils-1.7.1-py2.7.egg')  #获取xlutils路径
findpath_pyqt = os.path.join(findpath,'PyQt4')                       #获取PyQt4路径



if not os.path.isdir(findpath_xlrd):
    abs = os.path.abspath('.')  
    sourcedir = os.path.join(abs,'source')     
    sourcedir_xlrd = os.path.join(sourcedir,'xlrd-0.9.3')  
    #sourcedir_xlrdpy = os.path.join(sourcedir_xlrd,'setup.py install')
    os.chdir(sourcedir_xlrd)
    cmd = 'python setup.py install'
    os.system(cmd)    #未测试
    os.chdir(abs)
    
if not os.path.isdir(findpath_xlwt):
    abs = os.path.abspath('.') 
    sourcedir = os.path.join(abs,'source') 
    sourcedir_xlwt = os.path.join(sourcedir,'xlwt-1.0.0')  
    #sourcedir_xlwtpy = os.path.join(sourcedir_xlwt,'xlwt-1.0.0')
    os.chdir(sourcedir_xlwt)
    cmd = 'python setup.py install'
    os.system(cmd)    #未测试
    os.chdir(abs)
    #os.system(sourcedir_xlwtpy)    #未测试
    
    
if not os.path.isdir(findpath_xlutils):

    abs = os.path.abspath('.')  
    sourcedir = os.path.join(abs,'source')  
    sourcedir_xlutils = os.path.join(sourcedir,'xlutils-1.7.1')
    os.chdir(sourcedir_xlutils)
    cmd = 'python setup.py install'
    os.system(cmd)    #未测试
    os.chdir(abs)
    #sourcedir_xlutilspy = os.path.join(sourcedir_xlutils,'setup.py install') 
    #os.system(sourcedir_xlutilspy)    #未测试
    
    
if not os.path.isdir(findpath_pyqt):

    abs = os.path.abspath('.') 
    sourcedir = os.path.join(abs,'source')  
    sourcedir_pyqt = os.path.join(sourcedir,'Pyqt')  
    sourcedir_pyqtexe = os.path.join(sourcedir_pyqt,'PyQt4-4.11.3-gpl-Py2.7-Qt4.8.6-x32.exe')  
    os.system(sourcedir_pyqtexe)     #已测试


#__*__ coding:utf-8 __*__
import os
abs = os.path.abspath('.')  
sourcedir = os.path.join(abs,'source')  
sourcedir_xlutils = os.path.join(sourcedir,'xlutils-1.7.1')  
#sourcedir_xlutilspy = os.path.join(sourcedir_xlutils,'setup.py install') 
os.chdir(sourcedir_xlutils)
os.system('cmd.exe')
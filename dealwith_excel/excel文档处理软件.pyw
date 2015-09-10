#__*__ coding:utf-8 __*__
import os

absp = os.path.abspath('.')
#absup = os.path.split(absp)[0] #上级菜单
abs = os.path.join(absp,'mylib')
abs_auto = os.path.join(abs,'autosetup.py') 
abs_gui = os.path.join(abs,'GUI.pyw')     

execfile(abs_auto)
execfile(abs_gui)
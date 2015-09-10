#__*__ coding:utf-8 __*__
import xlrd
import xlwt
import os
import shutil   #复制文件

	
class MyFunc(object):
    def __init__(self):
        self.filepath=None   #路径
        self.fextension=None #扩展名
        self.filename=None	 #文件名
	
	#获取文件路径	
	#路经非空返回true
    def getfilepath(self,getfpath=None):
        self.filepath=getfpath
        if self.filepath:
            self.fextension=self.filepath.split(".")[-1] #文件后缀
            self.filename=self.filepath.split("/")[-1]   #文件名
            return True
        else:
            return False

    #判断文件后缀
    def isxlsfile(self):
        if self.filepath and (self.fextension=='xls'):
            return True
        else:
            return False
		
    #获取表单		
    def getsheet(self):
        if self.filepath and (self.fextension=='xls'):
            data = xlrd.open_workbook(self.filepath)
            #table = data.sheets()[0]          #通过索引顺序获取
            table=data.sheet_names()
            for x in table:
                print x    
            #table = data.sheet_by_index(0) #通过索引顺序获取
            return table
        else:
            return False
	
	

if __name__=='__main__':
    myfunc=MyFunc()
    #pat=myfunc.getfilepath('d:/file/program/tss.tcl')
    pat=myfunc.getfilepath('d:/file/program/ttss.xls')
    print ('filepath is %s'%myfunc.filepath +' fextension is %s'%myfunc.fextension +' filename is %s'%myfunc.filename)
    print ('getfilepath is %s'%pat,'isxlsfile %s'%(myfunc.isxlsfile()))
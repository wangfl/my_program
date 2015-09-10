#__*__ coding:utf-8 __*__
import xlrd
import xlwt
import os
import shutil   #�����ļ�

	
class MyFunc(object):
    def __init__(self):
        self.filepath=None   #·��
        self.fextension=None #��չ��
        self.filename=None	 #�ļ���
	
	#��ȡ�ļ�·��	
	#·���ǿշ���true
    def getfilepath(self,getfpath=None):
        self.filepath=getfpath
        if self.filepath:
            self.fextension=self.filepath.split(".")[-1] #�ļ���׺
            self.filename=self.filepath.split("/")[-1]   #�ļ���
            return True
        else:
            return False

    #�ж��ļ���׺
    def isxlsfile(self):
        if self.filepath and (self.fextension=='xls'):
            return True
        else:
            return False
		
    #��ȡ��		
    def getsheet(self):
        if self.filepath and (self.fextension=='xls'):
            data = xlrd.open_workbook(self.filepath)
            #table = data.sheets()[0]          #ͨ������˳���ȡ
            table=data.sheet_names()
            for x in table:
                print x    
            #table = data.sheet_by_index(0) #ͨ������˳���ȡ
            return table
        else:
            return False
	
	

if __name__=='__main__':
    myfunc=MyFunc()
    #pat=myfunc.getfilepath('d:/file/program/tss.tcl')
    pat=myfunc.getfilepath('d:/file/program/ttss.xls')
    print ('filepath is %s'%myfunc.filepath +' fextension is %s'%myfunc.fextension +' filename is %s'%myfunc.filename)
    print ('getfilepath is %s'%pat,'isxlsfile %s'%(myfunc.isxlsfile()))
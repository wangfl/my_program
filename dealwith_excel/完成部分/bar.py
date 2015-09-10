#http://www.linuxidc.com/Linux/2012-06/63652p8.htm
#Qt�ṩ��������ʾ�������ķ�ʽ��һ����QProgressBar����һ����QProgressDialog��QProgressBar���ṩ���ֺ����������ʾ�������Ŀؼ���ʾ��ʽ�����������������������QProgressDialog���ṩ��һ��������ٹ��̵Ľ��ȶԻ����ʾ��ʽ����������������ɵĽ����������׼�Ľ������Ի������һ��������ʾ����һ��ȡ����ť�Լ�һ����ǩ��

#QProgressBar�м�����Ҫ������ֵ��minimum,maximum������������ʾ����Сֵ�����ֵ��format������������ʾ���ֵĸ�ʽ��������3����ʾ��ʽ��%p%,%v,%m��%p%��ʾ��ɵİٷֱȣ�����Ĭ����ʾ��ʽ��%v��ʾ��ǰ�Ľ���ֵ��%m��ʾ�ܵĲ���ֵ��invertedAppearance���Կ����ý������Է�������ʾ���ȡ�

#QProgressDialogҲ�м�����Ҫ������ֵ�������˽������Ի����ʱ���֣����ֶ೤ʱ�䣬�ֱ���minimum,maximum��minimumDuration��minimum��maximum�ֱ��ʾ����������Сֵ�����ֵ�������˽������ı仯��Χ��minimumDurationΪ�������Ի������ǰ�ĵȴ�ʱ�䡣ϵͳ����������ɵĹ���������һ��Ԥ�ƻ��ѵ�ʱ�䣬�������趨�ĵȴ�ʱ��minimumDuration������ֽ������Ի�����С���趨�ĵȴ�ʱ�䣬�򲻳��ֽ������Ի���

#������ʹ����һ������ֵ�ĸ����һʱ���úý����������ֵ����Сֵ��������������ʾ��ɵĲ���ֵռ�ܵĲ���ֵ�İٷֱȣ��ٷֱȵļ��㹫ʽΪ��

#�ٷֱ�=(value()-minimum())/(maximum()-minimum())

#��������ʵ�ִ������£�

# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
   
class Progess(QDialog):  
    def __init__(self,parent=None):  
        super(Progess,self).__init__(parent)  
        self.setWindowTitle(self.tr("ʹ�ý�����"))  
        numLabel=QLabel(self.tr("�ļ���Ŀ"))  
        self.numLineEdit=QLineEdit("10")  
        typeLabel=QLabel(self.tr("��ʾ����"))  
        self.typeComboBox=QComboBox()  
        self.typeComboBox.addItem(self.tr("������"))  
        self.typeComboBox.addItem(self.tr("���ȶԻ���"))  
  
        self.progressBar=QProgressBar()  
  
        startPushButton=QPushButton(self.tr("��ʼ"))  
  
        layout=QGridLayout()  
        layout.addWidget(numLabel,0,0)  
        layout.addWidget(self.numLineEdit,0,1)  
        layout.addWidget(typeLabel,1,0)  
        layout.addWidget(self.typeComboBox,1,1)  
        layout.addWidget(self.progressBar,2,0,1,2)  
        layout.addWidget(startPushButton,3,1)  
        layout.setMargin(15)  
        layout.setSpacing(10)  
  
        self.setLayout(layout)  
          
        self.connect(startPushButton,SIGNAL("clicked()"),self.slotStart)  
  
    def slotStart(self):  
        num=int(self.numLineEdit.text())  
  
        if self.typeComboBox.currentIndex()==0:  
            self.progressBar.setMinimum(0)  
            self.progressBar.setMaximum(num)  
  
            for i in range(num):  
                self.progressBar.setValue(i)  
                QThread.msleep(100)  
  
        elif self.typeComboBox.currentIndex()==1:  
            progressDialog=QProgressDialog(self)  
            progressDialog.setWindowModality(Qt.WindowModal)  
            progressDialog.setMinimumDuration(5)  
            progressDialog.setWindowTitle(self.tr("��ȴ�"))  
            progressDialog.setLabelText(self.tr("����..."))  
            progressDialog.setCancelButtonText(self.tr("ȡ��"))  
            progressDialog.setRange(0,num)  
  
            for i in range(num):  
                progressDialog.setValue(i)  
                QThread.msleep(100)  
                if progressDialog.wasCanceled():  
                    return  
                  
app=QApplication(sys.argv)  
progess=Progess()  
progess.show()  
app.exec_()  

#��38�л�õ�ǰ��Ҫ���Ƶ��ļ���Ŀ�������Ӧ���������ܵĲ���ֵ��

#��40-46�в��ý������ķ�ʽ��ʾ���ȡ�

#��41��42�����ý������Ĳ�����Χ��0����Ҫ���Ƶ��ļ���Ŀ��

#��45��46��ģ��ÿһ���ļ��ĸ��ƹ��̣�����ͨ��QThread.msleep(100)��ģ�⣬��ʵ����ʹ���ļ����ƹ������滻�����������ܵĲ���ֵΪ��Ҫ���Ƶ��ļ���Ŀ�����������һ���ļ��󣬲���ֵ����1��

#��48-61�в��ý��ȶԻ���ķ�ʽ��ʾ���ȡ�

#��49�д���һ�����ȶԻ���

#��50�����ý��ȶԻ������ģ̬��ʽ������ʾ������ʾ���ȵ�ͬʱ���������ڽ�����Ӧ�����źš�

#��51 �����ý��ȶԻ�����ֵȴ�ʱ�䣬�˴��趨Ϊ5�룬Ĭ��Ϊ4�롣

#��52-54�����ý��ȶԻ���Ĵ�����⣬��ʾ������Ϣ�Լ�ȡ����ť����ʾ���֡�

#��55�����ý��ȶԻ���Ĳ�����Χ��

#��57-61��ģ��ÿһ���ļ����ƹ��̣�����ͨ��QThread.msleep(100)����ģ�⣬��ʵ����ʹ���ļ����ƹ������滻�����������ܵĲ���ֵΪ��Ҫ���Ƶ��ļ���Ŀ����������һ���ļ��󣬲���ֵ����1��������Ҫʹ��processEvents()��������Ӧ�¼�ѭ������ȷ��Ӧ�ó��򲻻����������

#��60��61�м�⡰ȡ������ť�Ƿ񱻴��������������˳�ѭ�����رս��ȶԻ�����ʵ��Ӧ���У��˴����������ص���������

#���ȶԻ����ʹ�������ַ�������ģ̬��ʽ���ģ̬��ʽ����ʵ����ʹ�õ���ģ̬��ʽ��ģ̬��ʽ��ʹ�ñȽϼ򵥷��㣬������ʹ��processEvents��ʹ�¼�ѭ��������������״̬���Ӷ�ȷ��Ӧ�ò�����������ʹ�÷�ģ̬��ʽ������Ҫͨ��QTime��ʵ�ֶ�ʱ���ý�������ֵ��
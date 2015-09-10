#http://www.linuxidc.com/Linux/2012-06/63652p8.htm
#Qt提供了两种显示进度条的方式，一种是QProgressBar，另一种是QProgressDialog，QProgressBar类提供了种横向或纵向显示进度条的控件表示方式，用来描述任务的完成情况。QProgressDialog类提供了一种针对慢速过程的进度对话框表示方式，用于描述任务完成的进度情况。标准的进度条对话框包括一个进度显示条，一个取消按钮以及一个标签。

#QProgressBar有几个重要的属性值，minimum,maximum决定进度条提示的最小值和最大值，format决定进度条显示文字的格式，可以有3种显示格式：%p%,%v,%m。%p%显示完成的百分比，这是默认显示方式；%v显示当前的进度值；%m显示总的步进值。invertedAppearance属性可以让进度条以反方向显示进度。

#QProgressDialog也有几个重要的属性值，决定了进度条对话框何时出现，出现多长时间，分别是minimum,maximum和minimumDuration。minimum和maximum分别表示进度条的最小值和最大值，决定了进度条的变化范围，minimumDuration为进度条对话框出现前的等待时间。系统根据所需完成的工作量估算一个预计花费的时间，若大于设定的等待时间minimumDuration，则出现进度条对话框；若小于设定的等待时间，则不出现进度条对话框。

#进度条使用了一个步进值的概念，即一时设置好进度条的最大值和最小值，进度条将会显示完成的步进值占总的步进值的百分比，百分比的计算公式为：

#百分比=(value()-minimum())/(maximum()-minimum())

#本例具体实现代码如下：

# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
   
class Progess(QDialog):  
    def __init__(self,parent=None):  
        super(Progess,self).__init__(parent)  
        self.setWindowTitle(self.tr("使用进度条"))  
        numLabel=QLabel(self.tr("文件数目"))  
        self.numLineEdit=QLineEdit("10")  
        typeLabel=QLabel(self.tr("显示类型"))  
        self.typeComboBox=QComboBox()  
        self.typeComboBox.addItem(self.tr("进度条"))  
        self.typeComboBox.addItem(self.tr("进度对话框"))  
  
        self.progressBar=QProgressBar()  
  
        startPushButton=QPushButton(self.tr("开始"))  
  
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
            progressDialog.setWindowTitle(self.tr("请等待"))  
            progressDialog.setLabelText(self.tr("拷贝..."))  
            progressDialog.setCancelButtonText(self.tr("取消"))  
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

#第38行获得当前需要复制的文件数目，这里对应进度条的总的步进值。

#第40-46行采用进度条的方式显示进度。

#第41，42行设置进度条的步进范围从0到需要复制的文件数目。

#第45，46行模拟每一个文件的复制过程，这里通过QThread.msleep(100)来模拟，在实际中使用文件复制过程来替换，进度条的总的步进值为需要复制的文件数目，当复制完成一个文件后，步进值增加1。

#第48-61行采用进度对话框的方式显示进度。

#第49行创建一个进度对话框。

#第50行设置进度对话框采用模态方式进行显示，即显示进度的同时，其他窗口将不响应输入信号。

#第51 行设置进度对话框出现等待时间，此处设定为5秒，默认为4秒。

#第52-54行设置进度对话框的窗体标题，显示文字信息以及取消按钮的显示文字。

#第55行设置进度对话框的步进范围。

#第57-61行模拟每一个文件复制过程，这里通过QThread.msleep(100)进行模拟，在实际中使用文件复制过程来替换，进度条的总的步进值为需要复制的文件数目，当复制完一个文件后，步进值增加1，这里需要使用processEvents()来正常响应事件循环，以确保应用程序不会出现阻塞。

#第60，61行检测“取消”按钮是否被触发，若触发则退出循环并关闭进度对话框，在实际应用中，此处还需进行相关的清理工作。

#进度对话框的使用有两种方法，即模态方式与非模态方式。本实例中使用的是模态方式，模态方式的使用比较简单方便，但必须使用processEvents来使事件循环保持正常进行状态，从而确保应用不会阻塞。若使用非模态方式，则需要通过QTime来实现定时设置进度条的值。
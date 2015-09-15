BEGIN{
i=0
qtcount=-1
colicount=0
sum=0
}
{
 colb[i]=$1
 coli[i]=$8
 colk[i]=$10
 
 outputl[i]=0
 outputm[i]=0
 outputn[i]=0

 #qtcount=0表示开始qtcount=1表示结束
if(colk[i]=="QT")
{
qtcount++
if(qtcount>1)
{
qtcount=0
}
}
#当i列值为非0时
if(coli[i]!=0)
{
#判断是否为段落开头
if(coli[i-1]==0||(colk[i-1]=="QT"&&qtcount==1)||(colk[i]=="QT"&&qtcount==0))
{
 outputl[i]=colb[i]
 sum=0
 colicount=0 
}
sum=sum+coli[i]
colicount++
#判断是否为段尾
if(colk[i]=="QT"&&qtcount==1)
{
 outputm[i]=colb[i]
 outputn[i]=sum/colicount
 sum=0
 colicount=0
}
}
#当coli为0时
else
{
#前一列为段尾
if(sum!=0)
{
 outputm[i-1]=colb[i-1]
 outputn[i-1]=sum/colicount
}
colicount=0
sum=0
}
 
 i++
}

END{
printf("\n\n\n")
for(j=0;j<i;j++)
{
 printf("%f\n",outputl[j])   #输出l列
 printf("%f\n",outputm[j])	 #输出m列
 printf("%f\n",outputn[j])	 #输出n列
}
}
#_*_ coding: utf-8 _*_
from selenium import webdriver
import time
import os
import json
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

browserie = webdriver.Ie()

"""
@函数模块
"""
def get_resume_info():
    """
    @功能：获取简历基本信息
    @返回值：信息内容 (字典)
    """
    abs = os.path.abspath(".")
    basic_info_path = os.path.join(abs,"baseinfo.txt")
    with open(basic_info_path,"r") as fp: 
        get_info = json.load(fp)
    return get_info

def istone_login(browserie,*login_account):
    """
    @功能：登录istone
    @参数：账号密码
    """
    first_url= 'https://passport.isoftstone.com/?DomainUrl=http://ipsapro.isoftstone.com&ReturnUrl=%2fWebRRP%2fDefault.aspx'
    browserie.get(first_url)
    browserie.implicitly_wait(5)
    browserie.find_element_by_name("emp_DomainName").clear()
    browserie.find_element_by_name("emp_DomainName").send_keys(login_account[0])
    browserie.find_element_by_name("emp_Password").send_keys(login_account[1])
    browserie.find_element_by_id("BtnLogin").click()

def istone_import(browserie,**resume_info):
    """
    @功能：导入个人简历
    @参数：简历信息(字典)
    @返回值：无
    """
    time.sleep(1)
    browserie.implicitly_wait(5)
    browserie.find_element_by_class_name("i_in").click()
    browserie.switch_to_frame("IfContent") #切换到相应frame
    time.sleep(1)
    istone_name_id ="ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_Name_TextBox1"
    browserie.find_element_by_id(istone_name_id).send_keys(resume_info["name"])
    istone_channeltype_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_ddlRS_ChannelType"
    istone_channeltype = browserie.find_element_by_id(istone_channeltype_id) #渠道类型 招聘网站
    istone_channeltype.find_element_by_xpath("//option[@value='3417fd0f-b608-4813-bf09-97a4a1f474bb']").click()
    time.sleep(1)
    browserie.implicitly_wait(10)
    istone_channelname_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_ddlRS_ChannelName"
    istone_channelname = browserie.find_element_by_id(istone_channelname_id)     #渠道名称 51job
    istone_channelname.find_element_by_xpath("//option[@title='51JOB']").click()
    istone_graduationschool_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_GraduationSchool_TextBox1"
    browserie.find_element_by_id(istone_graduationschool_id).send_keys(resume_info["college"])    # 毕业院校  
    istone_major_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_Specialty_TextBox1"
    browserie.find_element_by_id(istone_major_id).send_keys(resume_info["major"])    #专业
    browserie.implicitly_wait(10)
    if resume_info["company"] == "":
        resume_info["company"] ==u"无"
    istone_company_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtBeforeCompanyName_TextBox1"
    browserie.find_element_by_id(istone_company_id).send_keys(resume_info["company"])    #上家就职公司 
    istone_city_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_lbRS_ExpectWorkArea_From"
    istone_city = browserie.find_element_by_id(istone_city_id)
    istone_city.find_element_by_xpath("//option[@value='70cadf2e-6bef-438c-b271-38989e1846d2']").click()
    istone_cityaddbutton_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_ibtnAddEWA"
    browserie.find_element_by_id(istone_cityaddbutton_id).click()    #期望工作地  南京
    time.sleep(1)
    browserie.implicitly_wait(10)
    istone_position_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_lbRS_ExpectPosition_From"
    istone_position = browserie.find_element_by_id(istone_position_id)
    istone_position.find_element_by_xpath("//option[@value='e5a6ca51-ee91-4832-b709-bbea9c3143f0']").click()
    istone_postaddbutton_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_ibtnAddEP"
    browserie.find_element_by_id(istone_postaddbutton_id).click()    #期望职位类别  计算机网络
    time.sleep(1)
    if resume_info["email"] == "":
        resume_info["email"] =="no email"
    istone_email_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_Email_TextBox1"    
    browserie.find_element_by_id(istone_email_id).send_keys(resume_info["email"])    #email
    istone_phone_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_Tel_TextBox1"
    browserie.find_element_by_id(istone_phone_id).send_keys(resume_info["phone"])   #联系手机 
    istone_workyear_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_ddlRS_WorkExerience"
    istone_workyear = browserie.find_element_by_id(istone_workyear_id)    #工作年限 1-3年
    istone_workyear.find_element_by_xpath("//option[@value='add4d45f-fa60-48eb-a0bf-1b3fa8d606f2']").click()
    istone_resume_id = "ctl00_ContentPlaceHolder1_ResumeEdit1_txtRS_ResumeDetail_TextBox1"
    browserie.find_element_by_id(istone_resume_id).send_keys(resume_info["content"])   #简历详细内容
    istone_submit_id="ctl00_ContentPlaceHolder1_ResumeEdit1_btnSubmitandPre"
    browserie.find_element_by_id(istone_submit_id).click()   #提交信息
    browserie.switch_to_alert().accept()
    browserie.switch_to_default_content()    #切换回原框架

def search_istonelib(browserie,search_info):
    """
    @功能：检索简历是否可用&&
    @返回值：istonelib无简历信息返回True、有简历信息返回False
    """
    time.sleep(1)
    browserie.implicitly_wait(10)
    browserie.find_element_by_class_name("i_resume").click()
    time.sleep(1)
    browserie.implicitly_wait(10)
    browserie.find_element_by_id("ctl00_Left1_ctl03_tvResumeLibraryt0").click()
    browserie.switch_to_frame("IfContent") #切换到相应frame
    #browserie.switch_to_default_content() 切回原框架
    istone_searchmethod = browserie.find_element_by_id("Search")    #选择全文搜索
    istone_searchmethod.find_element_by_xpath("//option[@value='5']").click()
    search_text_id = "ctl00_ContentPlaceHolder1_CommonOperateAndSearch1_txtWholeSearch_TextBox1"
    browserie.find_element_by_id(search_text_id).send_keys(search_info)    #全文搜索 号码 或 自我评价
    search_button_id ="ctl00$ContentPlaceHolder1$CommonOperateAndSearch1$btnWholeSearch"
    browserie.find_element_by_name(search_button_id).click()    #搜索按钮
    time.sleep(2)
    #简历是否存在
    try:
        search_result_content = browserie.find_element_by_id("ctl00_ContentPlaceHolder1_gpDown").text 
    except:
        search_result_content = browserie.find_element_by_id("ctl00_ContentPlaceHolder1_ResumeList1_gpDown").text   
    if search_result_content == u"没有查询到符合条件的记录":
        print "istone_lib: resume match condition"
        browserie.switch_to_default_content()    #切回原框架    
        return True
    else: 
        istone_talbe_element = browserie.find_element_by_id("ctl00_ContentPlaceHolder1_gv")
        search_resume_state = istone_talbe_element.find_element_by_xpath("//tr[@class='Grid_Item']/td[2]").text
        if search_resume_state == "":
            print "istone_lib: resume match condition"
            """
            @导入
            """
            browserie.find_element_by_id("ctl00_ContentPlaceHolder1_gv_ctl02_chkSel").click()
            browserie.switch_to_default_content()    #切回原框架  
            browserie.find_element_by_id("i_share").click()
            browserie.switch_to_alert()
            return False 
    print "istone_lib: resume is invalid"    
    browserie.switch_to_default_content()    #切回原框架  
    return False

def deal_evaluation_info(get_info):
    """
    @功能：从evaluationinfo.txt中获取个人评价信息，用于检索
    @返回值：评价信息list
    """
    if re.search("[\n]+",get_info):
        get_evaluation_info = re.split("[\n]+",get_info)
        temp_info = get_evaluation_info[0]
        for eva_info in get_evaluation_info:
            if len(eva_info)>len(temp_info):
                temp_info = eva_info
        return temp_info.decode("utf-8")
    else:
        return get_info.decode("utf-8")

"""
@函数模块@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
#browserie = webdriver.Ie()
login_account = ("xiaoniu","vicky@123")
info_dict = get_resume_info()
istone_login(browserie,*login_account)

abs_path = os.path.abspath(".")
ex_info_path = os.path.join(abs_path,"exchange_info.txt")

if info_dict["phone"] =="":    #未下载简历
    #获取个人评价信息用于检索
    evaluation_info = deal_evaluation_info(info_dict["evaluation"])
    if search_istonelib(browserie,evaluation_info[:20]) :
        with open(ex_info_path,"w") as write_fp:
            write_fp.write("1")   #希望下载该简历
else:    #已下载简历
    if search_istonelib(browserie,info_dict["phone"]) :
        istone_import(browserie,**info_dict)   #导入个人信息

browserie.quit()

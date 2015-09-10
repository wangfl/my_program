#_*_ coding:utf-8 _*_
from selenium import webdriver
import time
import os
import json
import re
import ImageGrab
import random
from selenium.webdriver.support.ui import Select
import sys
reload(sys)
sys.setdefaultencoding("utf8")

"""
@函数模块列表
"""
def wakeup_time(start_hour=2,start_min=30,default_hour=21):
    """
    功能： 定时执行后续程序
    入参： 执行时间 默认2：40, 3～21点可立即执行
    返回值： 是否sleep
    示例：time.localtime()  << (2007, 6, 2, 12, 47, 7, 5, 153, 0)
    """
    time_hour =time.localtime()[3]
    time_min = time.localtime()[4]
    if time_hour>=default_hour:
        sleep_hour = 24 - time_hour+start_hour
    else:
        sleep_hour = start_hour - time_hour
    sleep_sec = (sleep_hour)*3600 + (start_min-time_min)*60
    if sleep_sec<0:
        print "No need sleep"
        return False
    print "Sleep %s sec"%sleep_sec
    time.sleep(sleep_sec)
    return True

def open_url():
    """
    @打开51job网址
    @返回 登录页title
    """
    jobnet_url= 'http://ehire.51job.com/MainLogin.aspx'
    browser.maximize_window()
    browser.get(jobnet_url)
    browser.implicitly_wait(10)
    return browser.title


def login_account(*job_account):
    """
    @登录 公司名、账号、密码
    @判断网页中是否有验证码&& 处理验证码
    @返回 登录是否成功
    """
    browser.implicitly_wait(10)
    browser.find_element_by_id("txtMemberNameCN").clear()
    browser.find_element_by_id("txtMemberNameCN").send_keys(job_account[0])
    browser.find_element_by_id("txtUserNameCN").clear()
    browser.find_element_by_id("txtUserNameCN").send_keys(job_account[1])
    browser.find_element_by_id("txtPasswordCN").send_keys(job_account[2])
    try :
        imgfoucs = browser.find_element_by_id("imgCheckCodeCN") 
    except :
        browser.find_element_by_id("Login_btnLoginCN").click()
        print "VerifyCode is NOT EXIST"
    else :
        print "VerifyCode is EXIST"
        if browser.find_element_by_id("lblErrorCN").text =="":
            save_verifycode()
        else:
            save_verifycode(603,664)
        vcodevalue = getverify()
        browser.find_element_by_id("txtCheckCodeCN").send_keys(vcodevalue)
    browser.implicitly_wait(10)
    if browser.title == u"网才":
        return True
    else:
        if browser.title == u"在线用户管理":
            browser.find_element_by_link_text(u"强制下线").click()
            return True
        return False

def save_verifycode(lable_x =603,lable_y=657):
    """
    @截取保存网页验证码图片
    @返回 验证码图片地址
    """
    abs = os.path.abspath(".")
    imagepath = os.path.join(abs,"RandomNumber.gif") 
    bbox = (lable_x, lable_y, lable_x+60, lable_y+25)
    img = ImageGrab.grab(bbox)
    img.save(imagepath)
    return imagepath

def getverify():
    """
    @验证码识别命令 tesseract 图片名 生成文件名
    @ 图片名：默认为RandomNumber.gif 
    @生成文件名默认为result.txt
    @dos命令执行多条使用 &&连接
    """
    abs = os.path.abspath('.')
    imagefile = os.path.join(abs,"RandomNumber.gif")
    cmd = "cd " + abs + " && tesseract RandomNumber.gif randomnumber"
    os.system(cmd)
    resultpath = os.path.join(abs,"randomnumber.txt")
    with open(resultpath,"r") as f:
        verifyvalue = f.read()
    verifyvalue = verifyvalue.replace(" ", "")
    return verifyvalue

def search_condition(set_a="java",set_b=u"一年",set_c=u"四年",set_sex ="SEX_1"):
    """
    @参数 设置搜索条件
    @返回 搜索结果页面窗口值
    """
    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_id("MainMenuNew1_imgResume").click()
    browser.find_element_by_id("MainMenuNew1_hlResumeSearch").click()
    time.sleep(1)
    browser.implicitly_wait(10)
    browser.find_element_by_id("KEYWORD").clear()
    browser.find_element_by_id("KEYWORD").send_keys(set_a)
    browser.find_element_by_id("AREA_btn").click()
    time.sleep(1)
    browser.find_element_by_css_selector("#td_Area_070200 > span").click()
    time.sleep(1)
    browser.find_element_by_id("ajchx070200").click()
    time.sleep(1)
    browser.find_element_by_css_selector(u"span[title=\"按 回车键(Enter) 直接确定\"]").click()
    Select(browser.find_element_by_id("WorkYearFrom")).select_by_visible_text(set_b)
    Select(browser.find_element_by_id("WorkYearTo")).select_by_visible_text(set_c)
    Select(browser.find_element_by_id("TopDegreeFrom")).select_by_visible_text(u"大专")
    Select(browser.find_element_by_id("TopDegreeTo")).select_by_visible_text(u"本科")
    browser.find_element_by_id(set_sex).click()
    browser.find_element_by_id("btnSearch").click()
    time.sleep(1)
    browser.implicitly_wait(10)
    return browser.current_window_handle

def refresh_resume():
    """
    @功能：检查简历是否刷新
    @返回值：布尔
    """
    try:
        first_resume_info = browser.find_element_by_id("trBaseInfo_1").text
    except:
        first_resume_info = browser.find_element_by_id("trBaseInfo_2").text
    first_resume_id = re.findall(r"\d{6,12}", first_resume_info)
    refresh_resume_id= first_resume_id
    while refresh_resume_id[0]==first_resume_id[0] :
        print refresh_resume_id[0]
        print first_resume_id[0]
        time.sleep(random.randint(40,120))
        browser.refresh()
        #此处未验证
        try:
            browser.switch_to_alert().accept()
        except:
            print "no alert open"
        #测试是否需要 switch_to_default_content()
        time.sleep(1)
        browser.implicitly_wait(10)
        refresh_resume_info = browser.find_element_by_id("trBaseInfo_1").text
        #refresh_resume_id = re.findall(r"\d+", refresh_resume_info)
        first_resume_id = re.findall(r"\d{6,12}", refresh_resume_info)
        if time.localtime()[3]>=4 :
            print "there is an error : refresh_resume()"
            exit()

    print "resume refreshed"
    return True

def jump_resumepage(path_var=1):
    """
    @进入个人信息界面
    """
    time.sleep(1)
    path_head = "//tr[@id='trBaseInfo_"
    path_tail = "']/td[3]/p/span/a"
    failed_path_tail = "']/td[2]"
    failed_path_full = path_head+str(path_var)+failed_path_tail
    browser.implicitly_wait(10)
    resume_id_content = browser.find_element_by_xpath(failed_path_full).text
    if resume_id_content == u"抱歉！该简历被求职者设为保密，暂不能查看！":
        print "resume is set secret :",resume_id_content
        return False
    path_full = path_head+str(path_var)+path_tail
    browser.implicitly_wait(10)
    browser.find_element_by_xpath(path_full).click()
    time.sleep(1)
    print "jump to No_id：%s resume"%path_var
    return True

def change_windows():
    """
    @切换窗口
    @返回 切换窗口状态
    """
    allhandles=browser.window_handles
    for handle in allhandles:
        if handle!=main_win_handle:     #比较当前窗口是不是原先的窗口
            browser.switch_to_window(handle)     #获得当前窗口的句柄
            return True   #窗口切换成功
    return False    #窗口切换失败

def resume_abstract(*company_forbiden):
    """
    @功能 提取简历信息
    @company_forbiden用于存储华为外包公司
    @返回值 简历是否可用
    """
    fileabs = os.path.abspath('.')
    baseinfo_path = os.path.join(fileabs,"baseinfo.txt")

    baseinfo ={"name":"","phone":"","email":"","company":"","degree":"","major":"","college":"","content":"","evaluation":""}
    time.sleep(1)
    if browser.title == "简历":
        print "resume is not public ,invalid"  #此人简历保密
        return False,baseinfo
    #处理特殊简历（resume仅显示 其他信息）
    special_resume_path = "//td[@id='divInfo']/table[2]"
    special_resume_content = browser.find_element_by_xpath(special_resume_path).text
    if special_resume_content =="":
        print "this is a special resume , invalid"
        return False,baseinfo
    judge_phone_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td"
    judge_resume_phone = browser.find_element_by_xpath(judge_phone_path).text
    print judge_resume_phone.encode("utf-8")
    if judge_resume_phone == u"电　话：" or judge_resume_phone == "":
        phone_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]"
        email_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]"
    else:
        judge_phone_path_1 = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td"
        judge_resume_phone_1 = browser.find_element_by_xpath(judge_phone_path_1).text
        if judge_resume_phone_1 == u"电　话：":
            phone_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]"
            email_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]"
        else:
            return False,baseinfo
    #获取简历基本信息
    browser.implicitly_wait(10)
    phone_email_path = "//div[@id='divResume']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody"
    company_path = "//div[@id='divResume']/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr[2]/td[2]"
    degree_path = "//div[@id='divResume']/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr[2]/td[2]"
    major_path = "//div[@id='divResume']/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr[3]/td[2]"
    college_path = "//div[@id='divResume']/table/tbody/tr/td/table[2]/tbody/tr/td[3]/table/tbody/tr[4]/td[2]"
    vocation_path = "//div[@id='divResume']/table/tbody/tr/td/table[3]/tbody/tr[3]/td/table[3]/tbody/tr[4]/td/table/tbody/tr[3]/td/span"
    resume_phone = browser.find_element_by_xpath(phone_path).text
    resume_email = browser.find_element_by_xpath(email_path).text
    resume_company = browser.find_element_by_xpath(company_path).text
    resume_degree = browser.find_element_by_xpath(degree_path).text
    resume_major = browser.find_element_by_xpath(major_path).text
    resume_college = browser.find_element_by_xpath(college_path).text
    resume_vocation = browser.find_element_by_xpath(vocation_path).text
    #自我评价存储
    if resume_phone =="":
        evaluation_path = "//div[@id='divResume']/table/tbody/tr/td/table[3]/tbody/tr[3]/td/table[2]/tbody/tr[4]/td/span"
        baseinfo["evaluation"] = browser.find_element_by_xpath(evaluation_path).text
    #简历内容存储
    baseinfo["content"] = browser.find_element_by_id("divResume").text
    search_istone = re.findall(u"软通动力",baseinfo["content"])
    if len(search_istone) !=0:
        return False,baseinfo
    #个人信息存储
    if resume_phone=="" and resume_email =="" :
        print "this is an unload resmue!" 
    else:
        phonenumber = re.findall(r"\d+", resume_phone)
        baseinfo["phone"] = phonenumber[0]
        baseinfo["email"] = resume_email
        print "this is an loaded resmue!"
    baseinfo["name"] =  browser.title
    baseinfo["company"] = resume_company
    baseinfo["degree"] = resume_degree
    baseinfo["major"] = resume_major
    baseinfo["college"] = resume_college
    with open(baseinfo_path,'w') as fp : 
        #ensure_ascii=False 存储时不使用unicode编码
        json.dump(baseinfo,fp,ensure_ascii=False) 
    """
    @初步筛选掉不符合条件的简历
    """
    #Resume_salary   xpath位置不固定，进行筛选处理
    salary_relate_path = "//div[@id='divResume']/table/tbody/tr/td/table[3]/tbody/tr[3]/td/table[3]/tbody/tr[4]/td/table/tbody"
    resume_salary_operate = browser.find_element_by_xpath(salary_relate_path)
    alltr_salarys = resume_salary_operate.find_elements_by_tag_name("tr")
    resume_salary =""
    for tr_salary in alltr_salarys :
        salary_option_judge = tr_salary.find_element_by_tag_name("td")
        if re.search(u"期望薪资：",salary_option_judge.text): 
            resume_salary = salary_option_judge.find_element_by_tag_name("span").text
    salary_wanted =[0,0]
    if resume_salary != "":
        salary_wanted = re.findall(r"\d+" , resume_salary)
    #薪资>12000不考虑
    if (int(salary_wanted[0]) < 12000 and int(salary_wanted[0]) > 1000) or (int(salary_wanted[0]) >= 0 and int(salary_wanted[0]) <=12): 
        print "salary_wanted is not less than %s"%salary_wanted[0]
        for company in company_forbiden:
            re_judge = re.findall(company,resume_company)
            if len(re_judge) != 0 :
                print "resume_company is not match"
                return False,baseinfo
    else:
        print "resume_salary is not match: ",salary_wanted[0],"  ",salary_wanted[1]
        return False,baseinfo

    print "resume_salary && resume_company is match "
    return True,baseinfo

def calculate_resume_weight(resume_content,**condition_dict):
    """
    @功能 计算简历权值
    @返回 简历权值
    """
    condition_weight =0
    for k,v in condition_dict.iteritems() :
        detectresult = re.findall(k,resume_content)
        condition_weight += len(detectresult) * v
    return condition_weight

def judge_resume_date(path_var=1):
    path_head = "//tr[@id='trBaseInfo_"
    path_tail = "']/td[2]"
    date_path_tail = "']/td[10]"
    judge_path = path_head+str(path_var)+path_tail
    date_path = path_head+str(path_var)+date_path_tail
    browser.implicitly_wait(10)
    resume_id_content = browser.find_element_by_xpath(judge_path).text
    if resume_id_content == u"抱歉！该简历被求职者设为保密，暂不能查看！":
        return True
    else:
        get_date = browser.find_element_by_xpath(date_path).text
        date_info = re.split('-',get_date)
        #current_day  = int(time.strftime("%d",time.localtime()))
        current_day = time.localtime()[2]
        yesterday = current_day-1   #注：每月1号只下当天日期
        if int(date_info[2])==current_day or int(date_info[2]) == yesterday :
            return True
        else:
            return False

def input_valid_resume(download_count,download_max,*weight_list,**baseinfo_resume):
    """
    @功能
    @参数 下载数、权值字典、baseinfo字典
    @返回值 已下载简历数
    """
    baseinfo = baseinfo_resume

    if baseinfo["phone"] !="":
        if weight_list[0] > weight_list[1] :
            print "resume is matched",weight_list[0]
            #处理已下载文件
            execfile("istonenet.py") 
        else:
            print "resume is not matched",weight_list[0]
    else:
        if weight_list[0] > weight_list[2] and download_count < download_max :
            print "resume is matched",weight_list[0]
            #处理未下载resume
            abs_path = os.path.abspath(".")
            exchange_info_path = os.path.join(abs_path,"exchange_info.txt")
            with open(exchange_info_path,"w") as ex_write_fp:
                ex_write_fp.write("0")
            execfile("istonenet.py")
            with open(exchange_info_path,"r") as read_fp:
                getinfo = read_fp.read()

            if getinfo =="1":
                browser.find_element_by_xpath("//div[@id='divMenuContent']/p[2]").click()   #下载简历
                time.sleep(1)
                browser.implicitly_wait(10)
                browser.find_element_by_id("btnCommonOK").click()
                resume_abstract(*company_forbiden)
                execfile("istonenet.py")
                return (download_count+1)
        else:
            print "resume is not matched or download limited",weight_list[0],download_count
            
    return download_count

def page_turning(count_i):
    """
    @功能 处理是否需要翻页
    @参数 ID计数器、页码
    @返回 ID计数器、页码
    """
    if count_i>=51 :
        browser.find_element_by_id("pagerBottom_nextButton").click()
        time.sleep(2)
        return 1
    else:
        return count_i

"""
@函数模块列表@@@@@@@@

"""

wakeup_time() #唤醒程序
browser = webdriver.Chrome()  #调用chrome
loginpage_title = open_url()    #登录51job

job_account =(u"软通动力","xxxxxxxxxx","xxxxxx")
company_forbiden=(u"中软",u"易宝",u"佰钧成",u"易思博")  #前东家不能为华为外包
java_condition = ("java",u"一年",u"四年","SEX_1")
test_condition =(u"测试",u"一年",u"四年","SEX_1")
java_weight = {"java":1,"Java":1,"JAVA":1,"javascript":-1,u"软件测试":-2,u"测试工程师":-2,"android":0.5,"Android":0.5,u"研发":0.5,"软件工程师":1,u"安卓":0.5,"eclipse":1,"Eclipse":1,u"维护":-1.5,u"维护工程师":-4,u"测试":-1,"bug":0.5,"Bug":0.5,"mysql":0.5,"Mysql":0.5,"oracle":0.5,"Oracle":0.5,u"运维工程师":-6,u"运维":-4,u"运营":-4}
test_weight = {"测试":1,"软件测试":1,"测试工程师":2,"java":1,"Java":1,"JAVA":1,"bug":0.5,"Bug":0.5,"mysql":2,"Mysql":2,"oracle":2,"Oracle":2,"JQuery":1,"sql":1,"SQL":1,"Sql":1}

weight_list = [0,8,8]  #[0]为简历权值 已下载简历权值>8时为合格，未下载简历权值>8时为合格

download_max = 2  #简历下载次数上限
"""
@登录
"""
cycle_command =True
while cycle_command :
    login_state = login_account(*job_account)   #返回登录状态
    if login_state :
        cycle_command = False
    else:
        browser.refresh()
        time.sleep(3)   #保证刷新后能够截取验证码

main_win_handle = search_condition(*java_condition)    #搜索条件设置 获取搜索界面窗口值

refresh_resume()    #循环检查简历是否更新

#计数初始化
count_i = 1
count_download = 0

#下载当日更新及昨日信息
while judge_resume_date(count_i): 
    print "a test for judge_resume_date"
    #跳转至ID = count_i 个人简历
    resume_state = jump_resumepage(count_i)       
    if resume_state :
        #简历不为保密状态
        change_windows()   #切换窗口至个人简历窗口
        #返回简历判断和信息&&筛选前东家和薪资
        try:
            resume_judge,baseinfo = resume_abstract(*company_forbiden)
        except:
            print "this is an unnormal resume"
            resume_judge = False

        if resume_judge :
            #计算出简历权值
            weight_list[0] = calculate_resume_weight(baseinfo["content"],**java_weight)
            count_download = input_valid_resume(count_download,download_max,*weight_list,**baseinfo)                                            
        else:
            print "resume is not matched",weight_list[0]
        browser.close()
        browser.switch_to_window(main_win_handle)
    else:
        #保密简历不做处理
        print "this is a secret resume"
    count_i+=1
    count_i = page_turning(count_i)

browser.quit()
print "task end~"
exit()








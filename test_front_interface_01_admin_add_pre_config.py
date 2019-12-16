# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
import config

# import seleniumfiles
browser = webdriver.Chrome()


##==========================================登录平台==============================================================
def test_login():
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('admin')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


##=========================================创建行业===================================
def test_hy():
    browser.get(config.remotehost + '/#/page/organization/industry')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div[1]/div[2]/'
                                         'button[1]/span')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    hyname = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/form/div[1]/div/div[1]/input')
    hyname.send_keys('测试行业')
    time.sleep(2)  # 输入行业名
    pic = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/form/div[2]/div/div/label/input')
    pic.send_keys(os.path.abspath('pic1.png'))
    time.sleep(2)  # 输入行业logo
    ve = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(2)  # 点击确定
    assert 0 == 0


##=========================================创建攻击队伍=========================================
def test_attackteam():
    browser.get(config.remotehost + '/#/page/organization/attack')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div/div[1]'
                                         '/div[2]/button[1]/span')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    gjdwname = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div['
        '1]/div/div[1]/input')
    gjdwname.send_keys('测试攻击队伍')
    time.sleep(1)  # 输入攻击队伍名称
    address = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div[2'
        ']/div/div[1]/input')
    address.send_keys('湖北武汉')
    time.sleep(1)  # 输入地址
    jingdu = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div[3'
        ']/div/div/input')
    jingdu.send_keys('74.1233')
    time.sleep(1)  # 输入经度
    weidu = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div[4'
        ']/div/div[1]/input')
    weidu.send_keys('15.13')
    time.sleep(1)  # 输入纬度
    dwxz = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div[5]/'
        'div/div/div[1]/input')
    dwxz.click()
    time.sleep(1)  # 点击队伍性质
    xzdwxz = browser.find_element_by_xpath('/html/body/div[9]/div/div/ul/li[1]')
    xzdwxz.click()
    time.sleep(1)  # 选中队伍性质
    dwlogo = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[2]/form/div[6]'
        '/div/div/label/input')
    dwlogo.send_keys(os.path.abspath('pic1.png'))
    time.sleep(1)  # 添加队伍logo
    ve = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div[3]/div/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================创建防守队伍=====================================
def test_victimteam():
    browser.get(config.remotehost + '/#/page/organization/defense')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div/div[1]/d'
                                         'iv[2]/button[1]/span')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    fsdwname = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    fsdwname.send_keys('测试防守队伍')
    time.sleep(1)  # 输入防守队伍名称
    address = browser.find_element_by_xpath(
        '/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/div[1]/div[1]/input')
    address.click()
    time.sleep(1)  # 点击地址下拉框
    province = browser.find_element_by_xpath(
        '/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/span/ul/li[1]')
    province.click()
    time.sleep(1)  # 选择省
    city = browser.find_element_by_xpath(
        '/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/div[2]/div/span/span/ul/li[1]')
    city.click()
    time.sleep(1)  # 选择市
    jd = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    jd.send_keys('74.1233')
    time.sleep(1)  # 输入经度
    wd = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    wd.send_keys('15.13')
    time.sleep(1)  # 输入纬度
    hy = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[6]/div/div/div[1]/input')
    hy.click()
    time.sleep(1)  # 点击行业
    hy = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li/span')
    hy.click()
    time.sleep(1)  # 选中行业
    dwxz = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[7]/div/d'
                                         'iv/div[1]/input')
    dwxz.click()
    time.sleep(1)  # 点击队伍性质
    dwxz = browser.find_element_by_xpath('/html/body/div[11]/div/div/ul/li[1]')
    dwxz.click()
    time.sleep(1)  # 选中队伍性质
    dwlogo = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[8]/div/di'
                                           'v/label/input')
    dwlogo.send_keys(os.path.abspath('pic1.png'))
    time.sleep(1)  # 添加队伍logo
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================创建攻击用户===================================
def test_attackuser():
    browser.get(config.remotehost + '/#/page/user')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div[1'
                                         ']/div[2]/button[1]/span')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_attacker')
    time.sleep(1)  # 输入用户名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/input')
    yhm.send_keys('攻击方')
    time.sleep(1)  # 输入姓名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[3]/div/div[1]/input')
    yhm.send_keys('18888888888')
    time.sleep(1)  # 输入手机号
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入初始密码
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入确认密码
    juese = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/di'
                                          'v[6]/div/div/div[1]/input')
    juese.click()
    time.sleep(1)  # 点击角色下拉框
    xzjs = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li[2]/span')
    xzjs.click()
    time.sleep(1)  # 选择攻击方
    bddw = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[7]/'
                                         'div/div[1]/div[1]/input')
    bddw.click()
    time.sleep(1)  # 选择绑定队伍
    csdw = browser.find_element_by_xpath('/html/body/div[11]/div/div/ul/li/span')
    csdw.click()
    time.sleep(1)  # 选择测试攻击队伍
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================创建防守用户=====================================
def test_victimuser():
    browser.get(config.remotehost + '/#/page/user')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/div['
                                         '1]/div[2]/button[1]/span')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_victim')
    time.sleep(1)  # 输入用户名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/input')
    yhm.send_keys('防守方')
    time.sleep(1)  # 输入姓名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[3]/div/div[1]/input')
    yhm.send_keys('18888888888')
    time.sleep(1)  # 输入手机号
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入初始密码
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入确认密码
    juese = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form'
                                          '/div[6]/div/div/div[1]/input')
    juese.click()
    time.sleep(1)  # 点击角色下拉框
    xzjs = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li[3]/span')
    xzjs.click()
    time.sleep(1)  # 选择攻击方
    bddw = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[7]/d'
                                         'iv/div[1]/div[1]/input')
    bddw.click()
    time.sleep(1)  # 选择绑定队伍
    csdw = browser.find_element_by_xpath('/html/body/div[11]/div/div/ul/li/span')
    csdw.click()
    time.sleep(1)  # 选择测试防守队伍
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================创建专家=========================================
def test_expert():
    browser.get(config.remotehost + '/#/page/user')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/di'
                                         'v/div[1]/div[2]/button[1]')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_expert')
    time.sleep(1)  # 输入用户名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/input')
    yhm.send_keys('专家')
    time.sleep(1)  # 输入姓名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[3]/div/div[1]/input')
    yhm.send_keys('18888888888')
    time.sleep(1)  # 输入手机号
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入初始密码
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入确认密码
    juese = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form'
                                          '/div[6]/div/div/div[1]/input')
    juese.click()
    time.sleep(1)  # 点击角色下拉框
    xzjs = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li[4]')
    xzjs.click()
    time.sleep(1)  # 选择专家
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================创建裁判========================================
def test_judge1():
    browser.get(config.remotehost + '/#/page/user')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/ma'
                                         'in/div/div[1]/div[2]/button[1]')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_judge1')
    time.sleep(1)  # 输入用户名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/input')
    yhm.send_keys('裁判')
    time.sleep(1)  # 输入姓名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[3]/div/div[1]/input')
    yhm.send_keys('18888888888')
    time.sleep(1)  # 输入手机号
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入初始密码
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入确认密码
    juese = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2'
                                          ']/form/div[6]/div/div/div[1]/input')
    juese.click()
    time.sleep(1)  # 点击角色下拉框
    xzjs = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li[5]')
    xzjs.click()
    time.sleep(1)  # 选择裁判
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


def test_judge2():
    browser.get(config.remotehost + '/#/page/user')
    time.sleep(1)
    addb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main'
                                         '/div/div[1]/div[2]/button[1]')
    addb.click()
    time.sleep(1)  # 点击添加按钮
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_judge2')
    time.sleep(1)  # 输入用户名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[2]/div/div[1]/input')
    yhm.send_keys('裁判')
    time.sleep(1)  # 输入姓名
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[3]/div/div[1]/input')
    yhm.send_keys('18888888888')
    time.sleep(1)  # 输入手机号
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[4]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入初始密码
    yhm = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[2]/form/div[5]/div/div[1]/input')
    yhm.send_keys('admin123')
    time.sleep(1)  # 输入确认密码
    juese = browser.find_element_by_xpath('/html/body/div[9]/div/div/div'
                                          '[2]/form/div[6]/div/div/div[1]/input')
    juese.click()
    time.sleep(1)  # 点击角色下拉框
    xzjs = browser.find_element_by_xpath('/html/body/div[10]/div/div/ul/li[5]')
    xzjs.click()
    time.sleep(1)  # 选择裁判
    ve = browser.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0


##=========================================获取IP=========================================
def test_getip():
    browser.get(config.remotehost + "/#/page/resource/ips")
    time.sleep(1)
    ipnum = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[1]/div[2]/form/div/div/div/input')
    ipnum.send_keys(3)
    time.sleep(1)
    getbutton = browser.find_element_by_xpath('//*[@id="app"]/section/section'
                                              '/main/div/div[1]/div[2]/button[1]/span')
    getbutton.click()
    time.sleep(1)
    sure = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/div/button[1]/span')
    sure.click()
    time.sleep(1)
    assert 0 == 0


##=========================================创建攻击队伍资源================================
def test_giveoutip():
    browser.get(config.remotehost + '/#/page/resource/attack')
    time.sleep(1)
    fp = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div[2]/div[1]/div[3]/'
        'table/tbody/tr/td[6]/div/button[1]/span')
    fp.click()
    time.sleep(1)
    first = browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[2]/form/div[2]/div/div/div[1]/div/div[2]/label[1]/span[1]/span')
    first.click()
    time.sleep(1)
    two = browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[2]/form/div[2]/div/div/div[1]/div/div[2]/label[2]/span[1]/span')
    two.click()
    time.sleep(1)
    three = browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[2]/form/div[2]/div/div/div[1]/div/div[2]/label[3]/span[1]/span')
    three.click()
    time.sleep(1)
    jt = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/for'
                                       'm/div[2]/div/div/div[2]/button[2]/span/i')
    jt.click()
    time.sleep(3)
    qdbt = browser.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div/button[1]/span')
    qdbt.click()
    time.sleep(1)
    assert 0 == 0


##=========================================设置基础设置=====================================
def test_setbasic():
    browser.get(config.remotehost + '/#/page/plat/systemSetting')
    time.sleep(1)
    sl = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/di'
        'v[1]/div/div/div/div/form/div[4]/div/div/input')
    ActionChains(browser).double_click(sl).perform()
    sl.send_keys(2)
    time.sleep(1)
    veri = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/di'
        'v/div/div/div/div/button[1]/span')
    veri.click()
    time.sleep(1)
    veri2 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]/span')
    veri2.click()
    time.sleep(1)
    assert 0 == 0


##=========================================高级演习设置=====================================
def test_butt():
    browser.get(config.remotehost + '/#/page/plat/systemSetting')
    time.sleep(1)
    by = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div/div/div/div[1]/div/'
        'div/div/div[1]/div[3]/div')
    by.click()
    time.sleep(1)
    ve = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[2]/div[2]/div/div/'
        'div/div/form/div[2]/div/div/span/span[2]')
    ve.click()
    time.sleep(1)
    ve2 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[2]/div[2]/div/'
        'div/div/div/div/button[1]/span')
    ve2.click()
    time.sleep(1)
    ve3 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]/span')
    ve3.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()

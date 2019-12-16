# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


# 用户登陆
def test_login():
    browser.get(config.remotehost + '/#/login')
    time.sleep(1)
    yhm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[1]/div/div[1]/input')
    yhm.send_keys('cs_expert')  # 用户名
    time.sleep(1)
    mm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[2]/div/div[1]/input')
    mm.send_keys('Admin123')  # 密码
    time.sleep(1)
    yzm = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[3]/div/div[1]/input')
    yzm.send_keys('xxx')  # 验证码
    time.sleep(1)
    dl = browser.find_element_by_xpath('//*[@id="app"]/div/div/form/div[4]/div/button')
    dl.click()
    time.sleep(1)
    assert 0 == 0


# 攻击方评审(通过)
def test_psgj():
    # 攻击方评审：得分，风险等级，评审意见
    browser.get(config.remotehost + '/#/page/score/attack')
    time.sleep(3)
    ck1 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/'
        'table/tbody/tr[1]/td[11]/div/button[1]')
    ck1.click()  # 点击查看
    time.sleep(5)
    psgjcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/p/button')
    psgjcj.click()  # 点击评审成绩
    time.sleep(1)
    tg = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/'
        'div[2]/form/div[1]/div/div/label[1]')
    tg.click()  # 点击通过
    time.sleep(1)
    nwqx = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div'
        '[2]/form/div[2]/div/div/label[1]')
    nwqx.click()  # 获得内网权限
    time.sleep(1)
    df = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/'
        'form/div[3]/div/div[1]/input')
    df.send_keys(524)  # 得分
    time.sleep(1)
    fxdj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/'
        'form/div[6]/div/div[1]/input')
    fxdj.send_keys(5)  # 风险等级
    time.sleep(1)
    psyj2 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/for'
        'm/div[7]/div/div[1]/textarea')
    psyj2.send_keys('comments')  # 评审意见
    time.sleep(1)
    qd2 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[3]/div/button[1]')
    qd2.click()
    time.sleep(1)
    assert 0 == 0


# 对防守方成绩评审(驳回)
def test_pscj():
    browser.get(config.remotehost + '/#/page/score/defense')
    time.sleep(3)
    ck = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/table/'
        'tbody/tr[1]/td[11]/div/button[1]')
    ck.click()  # 点击查看
    time.sleep(5)
    psfscj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/p/button')
    psfscj.click()  # 点击评审成绩
    time.sleep(1)
    bh = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div'
        '[2]/form/div[1]/div/div/label[2]')
    bh.click()  # 点击驳回
    time.sleep(1)
    psyj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/'
        'form/div[2]/div/div[1]/textarea')
    psyj.send_keys('comments')  # 评审意见
    time.sleep(1)
    qd = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[3]/div/button[1]')
    qd.click()
    time.sleep(1)
    fhlb = browser.find_element_by_xpath('/html/body/div[1]/section/section/main/div/di'
                                         'v[2]/div[1]/div[1]/button')
    fhlb.click()  # 点击返回列表
    time.sleep(1)
    assert 0 == 0
    browser.close()

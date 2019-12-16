# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


# 攻击方用户登录系统
def test_login():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_judge2')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('Admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_gjdf():
    browser.get(config.remotehost + '/#/page/score/attack')
    time.sleep(5)
    look1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[1]/div[3]/div[1]/div[3]/table/t'
        'body/tr[1]/td[12]/div/button/span')
    look1.click()
    time.sleep(3)  # 查看成绩
    pscj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/p/button/span')
    pscj.click()
    time.sleep(1)  # 点评审该成绩
    tgcj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div'
        '[2]/form/div[1]/div/div/label[1]/span[1]/span')
    tgcj.click()
    time.sleep(1)  # 点击通过按钮
    grant = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div['
        '2]/form/div[2]/div/div/label[1]/span[1]/span')
    grant.click()
    time.sleep(1)  # 点击获得内网权限
    score = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/'
        'form/div[3]/div/div[1]/input')
    score.send_keys(5200)
    time.sleep(1)  # 输入得分
    fxdj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/for'
        'm/div[6]/div/div[1]/input')
    fxdj.send_keys(9)
    time.sleep(1)  # 输入风险等级
    psyj = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/for'
        'm/div[7]/div/div[1]/textarea')
    psyj.send_keys('no comment')
    time.sleep(1)  # 输入评论意见
    ve = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[3]/di'
        'v/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    back = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[1]/button/span/span')
    back.click()
    time.sleep(1)  # 返回列表
    assert 0 == 0


def test_fsdf2():
    browser.get(config.remotehost + '/#/page/score/defense')
    time.sleep(5)
    look1 = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[1]/div[3]/div[1]/div[3]/table/tbod'
        'y/tr/td[12]/div/button/span')
    look1.click()
    time.sleep(3)  # 点击查看
    ps = browser.find_element_by_xpath(
        '//html/body/div[1]/section/section/main/div/div[2]/div[1]/div[3]/div[1]/p/button/span')
    ps.click()
    time.sleep(1)  # 点击评审该成绩
    tg = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/form/'
        'div[1]/div/div/label[2]/span[1]/span')
    tg.click()
    time.sleep(1)  # 点击驳回
    comm = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[2]/f'
        'orm/div[2]/div/div[1]/textarea')
    comm.send_keys('comments')
    time.sleep(1)  # 输入评审意见
    ve = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[2]/div[1]/div[6]/div/div/div[3'
        ']/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    assert 0 == 0
    browser.close()

# -*- coding: utf-8 -*-
import time
import os
import datetime
from getImages import crawl_oinbag


def refresh_to_run(peak_flag, k):
    old = ""
    j = 0
    print("获取可用的IP代理...")
    os.system("python3 getImages/fetch_free_proxies.py")
    while True:
        if not peak_flag:
            k = 15*k
        print("开始轮询...")
        new, flag = crawl_oinbag.refresh(old)
        old = new  # 不管有没有更新都要重新赋值
        if flag:
            print("有图片更新，开始爬虫程序...")
            os.system("scrapy crawl oinbag")
            print("爬取完毕，等待%d秒开始下次轮询..." % k)
        else:
            print("没有图片更新，等待%d秒下次轮询..." % k)
        time.sleep(k)
        j = j + k
        if j >= 3600:
            # 每小时更新一次IP代理列表
            print("更新IP代理")
            os.system("python3 getImages/fetch_free_proxies.py")
            j = 0
        print(k)


def time_to_run(peak_flag, k):
    j = 0
    # 获取可用的IP代理，保存在proxy.txt中
    print("获取可用的IP代理...")
    # os.system("python3 getImages/fetch_free_proxies.py")
    while True:
        if peak_flag:
            i = k
            j = j + i
        else:
            i = 7200
            j = i
        os.system("scrapy crawl oinbag")
        print("waiting......当前更新频率为%s秒" % i)
        time.sleep(i)
        if j >= 3600:
            # 每小时更新一次IP代理列表
            os.system("python3 getImages/fetch_free_proxies.py")
            j = 0


def peak_hour():
    """判断时间段"""
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    hour = time.strip().split(' ')[1].split(':')[0]
    # print(int(hour))
    if int(hour) < 8:
        return False
    else:
        return True


if __name__ == '__main__':
    slot = 120   # 设置轮询频率
    peak = peak_hour()
    # time_to_run(night_flag, slot)
    refresh_to_run(peak, slot)

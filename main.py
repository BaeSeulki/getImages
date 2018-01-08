# -*- coding: utf-8 -*-
import time
import os
import datetime


def run(flag, k):
    j = 0
    # 获取可用的IP代理，保存在proxy.txt中
    print("获取可用的IP代理...")
    os.system("python3 getImages/fetch_free_proxies.py")
    while True:
        if flag:
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


def night():
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    hour = time.strip().split(' ')[1].split(':')[0]
    # print(int(hour))
    if int(hour) < 8:
        return False
    else:
        return True


if __name__ == '__main__':
    k = 90   # 设置更新频率s
    a = night()
    run(a, k)

# -*- coding: utf-8 -*-
import time
import os
import datetime


def run(flag):
    j = 0
    # 获取可用的IP代理，保存在proxy.txt中
    os.system("python3 getImages/fetch_free_proxies.py")
    while True:
        # 每90秒执行一次爬虫
        if flag:
            i = 90
            j = j + i
        else:
            i = 3600
            j = i
        os.system("scrapy crawl oinbag")
        time.sleep(i)
        print("waiting......")
        if j == 3600:
            # 每小时更新一次IP代理列表
            os.system("python3 getImages/fetch_free_proxies.py")
            j = 0


def night():
    now = datetime.datetime.now()
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    hour = time.strip().split(' ')[1].split(':')[0]
    # print(int(hour))
    if int(hour) < 7:
        return False
    else:
        return True


if __name__ == '__main__':
    a = night()
    run(a)

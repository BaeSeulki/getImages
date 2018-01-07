# -*- coding: utf-8 -*-
import time
import os

j = 0
# 获取可用的IP代理，保存在proxy.txt中
os.system("python3 getImages/fetch_free_proxies.py")
while True:
    # 每90秒执行一次爬虫
    i = 90
    j = j + i
    os.system("scrapy crawl oinbag")
    time.sleep(i)
    print("waiting......")
    if j == 3600:
        # 每小时更新一次IP代理列表
        os.system("python3 getImages/fetch_free_proxies.py")
        j = 0

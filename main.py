# -*- coding: utf-8 -*-
import time
import os

j = 0
while True:
    i = 90
    j = j + i
    os.system("scrapy crawl oinbag")
    time.sleep(i)
    print("waiting......")
    if j == 3600:
        os.system("python3 getImages/fetch_free_proxies.py")
        j = 0

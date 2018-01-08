# -*- coding: utf-8 -*-
import urllib
from urllib import request
from bs4 import BeautifulSoup


def get_html(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1")
    html = urllib.request.urlopen(request)
    return html.read().decode('utf-8')


def get_soup(url):
    soup = BeautifulSoup(get_html(url), "lxml")
    return soup


def refresh(old_content):
    """判断是否有更新"""
    flag = False
    url = "http://www.oinbag.com/"
    # content = get_html(url)
    # print(content)
    soup = get_soup(url)
    # print(soup.prettify())
    # 查找第一个
    new_content = soup.find("li", attrs={"class": "event-img-file"}).a["href"]
    # print(new_content)
    if new_content != old_content:
        old_content = new_content
        flag = True
    return old_content, flag


if __name__ == '__main__':
    content, f = refresh("")
    print(refresh(content))

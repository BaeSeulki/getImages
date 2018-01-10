# getImages
## 从oinbag.com获取车牌标注图像
1. 图像下载，用标签命名
2. 反爬措施，IP代理和用户代理，禁用cookies，禁用robot协议
3. 定时检测更新，当有更新时执行爬虫程序

## 环境依赖：
python3.6  
scrapy1.5    
requests 2.18.4   
pillow 5.0.0  
twisted 17.90  
bs4 (BeautifulSoup) 0.01       


## 说明：  
pipelines.py 中设置保存图像的文件夹地址save_path  
main.py 中设置爬取间隔，默认为0-8点1800s一次，8点-24点120s一次。  

## shell执行命令：  
`python3 main.py`    



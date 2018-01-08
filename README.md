# getImages
##从oinbag.com获取车牌标注图像
1. 图像下载，用标签命名
2. 反爬措施，IP代理和用户代理，禁用cookies，禁用robot协议
3. 定时爬取无历史的实时更新网站

##环境依赖：
python3.6/ scrapy1.5/ requests  

##说明：  
pipelines.py 中设置保存图像的文件夹地址save_path  
main.py 中设置爬取间隔，默认为0-8点2小时一次，8点-24点90s一次。  

## shell执行命令：  
`python3 main.py`    



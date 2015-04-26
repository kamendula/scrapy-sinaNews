import requests,re,json

from scrapy.spider import BaseSpider
from bs4 import BeautifulSoup
from sinaNews.items import SinanewsItem

class newsSpider(BaseSpider):
    name = 'SportsNews'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = []

    def __init__(self):
        pages=1
        for page in range(pages):
            news_list = 'http://roll.sports.sina.com.cn/api/\
news_list.php?tag=2&cat_1=premierleague&&k=&show_num=60&page='+str(page+1)
            #print news_list
            info = requests.get(news_list).content.decode('gbk')
            data = re.match('var jsonData = (.*);',info).group(1)
            jsondata = json.loads(data)
            
            for news in jsondata['list']:
                #print news['title']
                #print news['url']
                self.start_urls.append(news['url'])

    def parse(self, response):
        news = BeautifulSoup(response.body)
        newsItem = SinanewsItem()
        newsItem['title'] = news.find(id='artibodyTitle').get_text()
        #newsItem['url'] = response.url
        t = news.find_all(id='artibody')
        s=''
        for p in t[0].find_all("p"):
            s = s + p.get_text()+'\n'
        newsItem['content'] = s
        newsItem['pic'] = news.find('div', class_='img_wrapper').img['src']
        return newsItem
        

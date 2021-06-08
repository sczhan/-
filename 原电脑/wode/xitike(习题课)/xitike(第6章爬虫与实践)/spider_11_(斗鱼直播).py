"""
任务:
爬取斗鱼直播内容
https://www.douyu.com/directory/all

思路:
1. 利用selenium得到页面内容
2. 利用xpath或者bs等在页面中进行信息提取

"""
from bs4 import BeautifulSoup
from selenium import webdriver


class Douyu():

    # 初始化方法
    "爬取斗鱼网页直播和再看直播人数"
    def start(self):
        self.url = "https://www.douyu.com/directory/all"
        self.dirver = webdriver.Chrome()

    def douyu(self):
        self.dirver.get(self.url)
        while True:
            soup = BeautifulSoup(self.dirver.page_source, "xml")
            # print(soup)
            # 返回当前页面所有的放标题列表和人数
            fenlei = soup.find_all("span", {'class': 'DyListCover-zone'})
            name = soup.find_all("h3", {"class": 'DyListCover-intro'})
            renshu = soup.find_all("span", {'class': 'DyListCover-hot is-template'})

            for names, renshus, fenleis in zip(name, renshu, fenlei):
                print("现在直播: {0},\n人数是: {1},\n直播类型是:  {2}\n".format(names.get_text(), renshus.get_text(), fenleis.get_text()))
            break

    def quit(self):
        self.dirver.quit()


if __name__ == "__main__":
    douyu = Douyu()
    douyu.start()
    douyu.douyu()
    douyu.quit()

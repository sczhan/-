
import re
import time
from urllib import request

# value = input("请输入：")

# def getMd5(value):
#     md5 = hashlib.md5()
#     md5.update(bytes(value, encoding="utf-8"))
#     key = md5.hexdigest()
#     return key

value = input("")
key = str(bytes(value, encoding="utf-8")).replace("\\x", "%").replace("b'", "").replace("'", "").upper()
# print(type(key), key)

def lianjie(key):
    url = "http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx?callback=jQuery18301" \
          "9982303452915473_1608796013779&m=0&key={}&_=1608796014008".format(key)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
    }

    rsp = request.Request(url, headers=headers)
    rep = request.urlopen(rsp)
    html = rep.read().decode()
    # print(html)
    counts = re.findall(r'"FundListTotalCount":\d*,', html)
    count = str(counts[0]).replace(",", "").split(":")[1]
    if count == 0:
        pass
    else:
        url = "http://fundsuggest.eastmoney.com/FundSearch/api/FundSearchPageAPI.ashx?" \
              "callback=jQuery18308281986363928_{0}&m=1&key={1}&pageindex=0&pagesize={2}&_={3}"\
            .format(int(time.time()*1000), key, count, int((time.time()-10000)*1000))
        rsp = request.Request(url, headers=headers)
        rep = request.urlopen(rsp)
        html = rep.read().decode()

    names = re.findall(r'"_id":.*?,"STOCKMARKET":""', html)
    for name in names:
        code = re.findall(r'"CODE":"\d{6}', name)[0].split('"')[3]
        jjname = re.findall(r'"NAME":".*?"', name)[0].split('"')[3]
        # url = "http://fund.eastmoney.com/{}.html".format(code)
        url = "http://fundgz.1234567.com.cn/js/{}.js?rt={}".format(code, int(time.time() * 100))
        # # print(code, jjname, url)1.05
        page(url, jjname)


def page(url, name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        # "Cookie":"AUTH_FUND.EASTMONEY.COM_GSJZ=AUTH*TTJJ*TOKEN; em_hq_fls=js; qgqp_b_id=fdd7c34fbeb0f6860c4e083b5a6dec60; em-quote-version=topspeed; searchbar_code=008282_008887_320007_00237112_001552_161726_161024_008641_001629_008903; HAList=a-sz-000768-%u4E2D%u822A%u897F%u98DE%2Ca-sz-000596-%u53E4%u4E95%u8D21%u9152%2Cd-hk-00268%2Ca-sz-002371-%u5317%u65B9%u534E%u521B%2Ca-sz-300750-%u5B81%u5FB7%u65F6%u4EE3%2Ca-sz-002636-%u91D1%u5B89%u56FD%u7EAA; EMFUND1=12-23%2014%3A08%3A42@%23%24%u94F6%u534E%u65B0%u80FD%u6E90%u65B0%u6750%u6599A@%23%24005037; EMFUND2=12-23%2014%3A32%3A58@%23%24%u5BCC%u5B89%u8FBE%u65B0%u5174%u6210%u957F%u6DF7%u5408@%23%24000755; EMFUND3=12-23%2015%3A46%3A11@%23%24%u5E7F%u53D1%u79D1%u6280%u5148%u950B%u6DF7%u5408@%23%24008903; EMFUND4=12-23%2015%3A46%3A37@%23%24%u9E4F%u534E%u7A7A%u5929%u519B%u5DE5%u6307%u6570%28LOF%29A@%23%24160643; EMFUND5=12-24%2014%3A20%3A22@%23%24%u524D%u6D77%u5F00%u6E90%u4E2D%u822A%u519B%u5DE5@%23%24164402; EMFUND6=12-24%2015%3A01%3A34@%23%24%u5BCC%u56FD%u519B%u5DE5%u4E3B%u9898%u6DF7%u5408@%23%24005609; EMFUND7=12-24%2014%3A21%3A42@%23%24%u62DB%u5546%u4E2D%u8BC1%u7164%u70AD%u7B49%u6743%u6307%u6570%u5206%u7EA7@%23%24161724; EMFUND8=12-24%2016%3A51%3A39@%23%24%u7533%u4E07%u83F1%u4FE1%u4E2D%u8BC1%u519B%u5DE5%u6307%u6570%u5206%u7EA7@%23%24163115; _adsame_fullscreen_18503=1; st_si=58908840308038; st_asi=delete; ASP.NET_SessionId=nfolud15y04x4d5b1qhj1cog; EMFUND0=12-25%2010%3A30%3A48@%23%24%u5929%u5F18%u4E2D%u8BC1%u8BA1%u7B97%u673AETF%u8054%u63A5A@%23%24001629; EMFUND9=12-25 10:58:49@#$%u5BCC%u56FD%u4E2D%u8BC1%u519B%u5DE5%u6307%u6570%u5206%u7EA7@%23%24161024; st_pvi=01767901850915; st_sp=2020-10-19%2011%3A20%3A51; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=4; st_psi=20201225105849190-0-1596718674",
        # "If-Modified-Since": "Fri, 25 Dec 2020 03:02:54 GMT",
        # "If-None-Match": "5fe5565e-25f63"
    }
    rsp = request.Request(url, headers=headers)
    rep = request.urlopen(rsp)
    html = rep.read().decode()
    # print(html)
    guzhi = re.findall(r'"gszzl":".*?,"', html)
    code = guzhi[0].split('"')
    print(name, code[3] + '%')



if __name__ == "__main__":
    lianjie(key)
    # page(url)
    # print(getMd5(value))



    # pass
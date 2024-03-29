import requests
import re
import json


# 文件写入方法
def file_data(title, address, avgprice, avgscore, comment):
    data = {
        '店铺名称': title,
        '店铺地址': address,
        '平均消费价格': avgprice,
        '店铺评分': avgscore,
        '评价人数': comment
    }


    with open('美团美食.txt', 'a', encoding='utf-8')as fb:
        fb.write(json.dumps(data, ensure_ascii=False) + '\n')
        # ensure_ascii=False必须加因为json.dumps方法不关闭转码会导致出现乱码情况


def start():
    for w in range(0, 1792, 32):
        # 页码根据实际情况x32即可，我这里是设置50页为上限，为了避免设置页码过高或者数据过少情况，定义最大上限为1600-也就是50页，使用try-except来检测时候异常，异常跳过该页，一般作为无数据跳过该页处理
        try:
            # 注意uuid后面参数空余将uuid后xxx替换为自己的uuid参数
            # url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/70?uuid=2495cbb274184833b2d3.1621248470.1.0.0&userid=63721705&limit=32&offset=' + str(w) + '&cateId=-1&q=%E8%B6%B3%E6%B5%B4'
            url = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/70?uuid=2495cbb274184833b2d3.1621248470.1.0.0&userid=63721705&limit=32&offset=' + str(
                w) + '&cateId=-1&q=%E8%B6%B3%E6%B5%B4&token=SLvGTYPgBmv6cX6r8vhHtI5nWtMAAAAAhw0AAL5p_RIJu1wGFQW2jPZS0mBIFxjg2h44NUeIZq3fEBGw6hminGyRKXNQv_rUdiPCnw'
            # headers的数据可以在F12开发者工具下面的requests_headers中查看，需要实现选择如下headers信息
            # 必要情况 请求频繁 建议增加cookie参数在headers内
            headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'Host': 'apimobile.meituan.com',
                'Origin': 'https://chs.meituan.com',
                'Referer': 'https://chs.meituan.com/s/%E8%B6%B3%E6%B5%B4/'
            }
            response = requests.get(url, headers=headers)
            # 正则获取当前响应内容中的数据，因json方法无法针对店铺特有的title键值进行获取没所以采用正则
            titles = re.findall('","title":"(.*?)","address":"', response.text)
            addresses = re.findall(',"address":"(.*?)",', response.text)
            avgprices = re.findall(',"avgprice":(.*?),', response.text)
            avgscores = re.findall(',"avgscore":(.*?),', response.text)
            comments = re.findall(',"comments":(.*?),', response.text)
            # 输出当前返回数据的长度 是否为32
            print(len(titles), len(addresses), len(avgprices), len(avgscores), len(comments))
            for o in range(len(titles)):
                # 循环遍历每一个值 写入文件中
                title = titles[o]
                address = addresses[o]
                avgprice = avgprices[o]
                avgscore = avgscores[o]
                comment = comments[o]
                # 写入本地文件
                file_data(title, address, avgprice, avgscore, comment)
        finally:
            pass


if __name__ == '__main__':
    start()

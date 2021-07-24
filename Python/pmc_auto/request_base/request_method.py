import requests

class RequestMethod:
    """ 定义请求类型 """

    def __init__(self):

        """初始化参数"""
        self.base_url = cf.get('URL', 'base_url')
        self.data = {}
        self.files = {}
        self.mySchedule = sched.scheduler(time.time, time.sleep)

    def get(self, url, params):
        """
        定义get方法请求
        :return:
        """
        test_url = self.base_url + ":" + port_20224 + url
        try:
            return requests.get(url=test_url, params=params, timeout=60)
        except TimeoutError:
            return print('%s get request timeout!' % url)

    def post_act(self, url, params):
        """
        定义post方法请求
        :return:
        """
        try:
            headers = {'content-type': 'application/json;charset=UTF-8'}
            return requests.post(url=url, data=params.encode(), timeout=60, headers=headers)
        except TimeoutError:
            return print('%s post request timeout!' % url)

    def post(self, url, params,headers):
        """
        定义post方法请求
        :return:
        """
        try:
            return requests.post(url=url, data=params.encode(), timeout=60, headers=headers)
        except TimeoutError:
            return print('%s post request timeout!' % url)
    def put(self, url, params):
        """
        定义post方法请求
        :return:
        """
        try:
            headers = {'content-type': 'application/json;charset=UTF-8'}
            return requests.put(url=url, data=params.encode(), timeout=60, headers=headers)
        except TimeoutError:
            return print('%s post request timeout!' % url)

    def post_with_file(self, url, params, fp):
        """
        定义post方法请求
        :return:
        """
        test_url = self.base_url + url
        file = {
            'head_img': open(fp, 'rb')
        }
        try:
            return requests.post(url=test_url, data=params.encode(), files=file, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % url)


if __name__ == '__main__':
    request = RequestMethod()
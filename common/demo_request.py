import requests
import jsonpath
from fire import Fire

host = 'http://127.0.0.1:8888'
session = requests.session()


# def get():
#     url = host + '/api/Any'
#     params = {
#
#     }
#     resp = requests.get(url, params=params)
#     status_code = resp.status_code
#     print('响应状态码:{}'.format(status_code))
#     # text = resp.text
#     # print('响应内容:{}'.format(text))
#     json = resp.json()
#     print('响应内容:{}'.format(json))
#     resp_header = resp.headers
#     print('响应内容:{}'.format(resp_header))


def login():
    # global token
    # url = host + '/api/loginFrom51PM'
    # # headers = {'Content-Type': 'application/json;charset=UTF-8'}
    # data = {
    #     'username': '16621236193', 'password': '166212361937331'
    # }
    # resp = session.request(url=url, method='post', data=data)
    # # status_code = resp.status_code
    # # print('响应状态码：{}'.format(status_code))
    # # text = resp.text
    # # print('响应内容:{}'.format(text))
    # resp_json = resp.json()
    # token = jsonpath.jsonpath(resp_json, '$.data')[0]
    # print('响应内容:{}'.format(resp_json))
    # # resp_headers = resp.headers
    # # print('响应内容：{}'.format(resp_headers))

    url = 'http://127.0.0.1:8888/api/loginFrom51PM'
    json = {
        "username": "16621236193",
        "password": "166212361937331"
    }
    login_res = requests.post(url, json=json)
    # 从响应结果中获取token值
    token = login_res.json()["token"]
    print("token:", token)


if __name__ == '__main__':
    # get()
    # login()
    Fire(login)

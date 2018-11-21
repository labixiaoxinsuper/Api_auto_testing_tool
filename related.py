#coding=utf-8
import json
import requests
from method import Fmethod


class Frelated:
    def related_func(self, table, i, data_path, cookies_path, open_sheet, copy_data):
        # 先执行related的case，得到结果res1为dict
        row_data = table.row_values(i)  # 假如执行第六个case，相关联的是4，那么先执行4.i=6,rel=4.（无论第4个case是否yes）
        rel = int(row_data[7])   # 得到相关联的caseid，例如等于4
        row_data_rel = table.row_values(rel)   # 得到rel=4的行，以及其相关信息
        method = row_data_rel[4]
        url = row_data_rel[2]
        headers = row_data_rel[6]
        headers = headers.encode('utf-8')
        headers = json.loads(headers)

        # 打开data.json得到data
        d = str(rel)
        with open(data_path, 'r') as data_o:
            data_o = data_o.read()
            data = json.loads(data_o)
            data_num = 'data' + d
            data = data[data_num]

        # 打开cookies。json得到cookies
        with open(cookies_path, 'r') as cookies:
            cookies = cookies.read()
            cookies = json.loads(cookies)
            cookies_num = 'cookies' + d
            cookies = cookies[cookies_num]
        global res1
        if method == 'post':
            res = requests.post(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        elif method == 'get':
            res = requests.get(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        elif method == 'put':
            res = requests.put(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        elif method == 'delete':
            res = requests.delete(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        elif method == 'head':
            res = requests.delete(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        elif method == 'options':
            res = requests.delete(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            res1 = json.loads(res.content)
        else:
            pass
        # 将4得出的结果传入，然后更新headers 或者data,cookies.
        value_info = row_data[8]
        value_info = str(value_info)
        get_value_info = res1[value_info]
        location_info = row_data[9]
        key_value = row_data[10]

        method = row_data[4]
        url = row_data[2]
        info_1 = row_data[12]
        info_2 = row_data[13]
        d = str(i)

        if location_info == 'headers':
            with open(data_path, 'r') as data_o:
                data_o = data_o.read()
                data = json.loads(data_o)
                data_num = 'data' + d
                data = data[data_num]
            headers = row_data[6]
            headers = headers.encode('utf-8')
            headers = json.loads(headers)
            headers[key_value] = get_value_info
            with open(cookies_path, 'r') as cookies:
                cookies = cookies.read()
                cookies = json.loads(cookies)
                cookies_num = 'cookies' + d
                cookies = cookies[cookies_num]
            run = Fmethod()
            run.method_func(url, headers, data, cookies, info_1, info_2, open_sheet, copy_data, i, method)  # 执行method_func

        elif location_info == 'data':
            headers = row_data[6]
            headers = headers.encode('utf-8')
            headers = json.loads(headers)
            with open(data_path, 'r') as data_o:
                data_o = data_o.read()
                data = json.loads(data_o)
                data_num = 'data' + d
                data = data[data_num]
            data[key_value] = get_value_info
            with open(cookies_path, 'r') as cookies:
                cookies = cookies.read()
                cookies = json.loads(cookies)
                cookies_num = 'cookies' + d
                cookies = cookies[cookies_num]
            run = Fmethod()
            run.method_func(url, headers, data, cookies, info_1, info_2, open_sheet, copy_data, i, method)   # 执行method_func

        elif location_info == 'cookies':
            headers = row_data[6]
            headers = headers.encode('utf-8')
            headers = json.loads(headers)
            with open(cookies_path, 'r') as cookies:
                cookies = cookies.read()
                cookies = json.loads(cookies)
                cookies_num = 'cookies' + d
                cookies = cookies[cookies_num]
            with open(data_path, 'r') as data_o:
                data_o = data_o.read()
                data = json.loads(data_o)
                data_num = 'data' + d
                data = data[data_num]
            run = Fmethod()
            run.method_func(url, headers, data, cookies, info_1, info_2, open_sheet, copy_data, i, method)  # 执行method_func
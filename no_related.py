#coding=utf-8
import json
from method import Fmethod

class Fno_related:
    def no_related_func(self, table, i, data_path, cookies_path, open_sheet, copy_data):
        row_data = table.row_values(i)   # 获取第i行的数据
        # 请求参数定义
        method = row_data[4]
        url = row_data[2]
        info_1 = row_data[12]
        info_2 = row_data[13]

        # 从case.xls中获取headers
        headers = row_data[6]             # 初步得到的headers为unicode的类型，转换为dict
        headers = headers.encode('utf-8')
        headers = json.loads(headers)

        # 从data.json中获取data
        d = str(i)      #  把i的int转换为str
        with open(data_path, 'r') as data_o:
            data_o = data_o.read()
            data = json.loads(data_o)
            data_num = 'data' + d
            data = data[data_num]

        # 从cookies.json中获取cookies
        with open(cookies_path, 'r') as cookies:
            cookies = cookies.read()
            cookies = json.loads(cookies)
            cookies_num = 'cookies' + d
            cookies = cookies[cookies_num]

        run = Fmethod()
        run.method_func(url, headers, data, cookies, info_1, info_2, open_sheet, copy_data, i, method)


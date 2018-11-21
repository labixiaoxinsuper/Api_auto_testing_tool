#coding=utf-8
import requests
import json


class Fmethod:
    def method_func(self, url, headers, data, cookies, info_1, info_2, open_sheet, copy_data, i, method):
        if method == 'post':
            res = requests.post(url=url, headers=headers, data=json.dumps(data),  cookies=cookies, verify=False)
            if res.status_code == 200:   # 先判断状态码，不是200，在case.xls的实际结果列写入状态码。
                res1 = json.loads(res.content)
                res2 = res.content  # excel表不支持传入dict的格式，所以改成str的格式。
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')

                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed", res1

            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        elif method == 'get':
            res = requests.get(url=url, headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            if res.status_code == 200:
                res1 = json.loads(res.content)
                res2 = res.content
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed",res1
            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        elif method == 'put':
            res = requests.put(url=url,  headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            if res.status_code == 200:
                res1 = json.loads(res.content)
                res2 = res.content
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed", res1
            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        elif method == 'delete':
            res = requests.delete(url=url,  headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            if res.status_code == 200:
                res1 = json.loads(res)
                res2 = res.content
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed", res1
            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        elif method == 'head':
            res = requests.delete(url,  headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            if res.status_code == 200:
                res1 = json.loads(res.content)
                res2 = res.content
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed", res1
            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        elif method == 'options':
            res = requests.delete(url,  headers=headers, data=json.dumps(data), cookies=cookies, verify=False)
            if res.status_code == 200:
                res1 = res.json()
                res2 = res.content
                if res1[info_1] == info_2:
                    open_sheet.write(i, 14, 'pass')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "pass", res1
                else:
                    open_sheet.write(i, 14, 'failed')
                    open_sheet.write(i, 15, res2)
                    copy_data.save('case.xls')
                    print "failed", res1
            else:
                open_sheet.write(i, 14, res.status_code)
                copy_data.save('case.xls')
                print res.status_code
        else:
            print "sorry, the method is not supported."







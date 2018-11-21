#coding=utf-8
import xlrd
from xlutils.copy import copy


def definations_func(excel_path, sheet_input, data_path, cookies_path):
    if excel_path: # 定义excel_path
        excel_path=excel_path
    else:
        excel_path = "case.xls"

    if sheet_input:  # 定义sheet_input
        sheet_input=sheet_input
    else:
        sheet_input = "Sheet1"
    excel = xlrd.open_workbook(excel_path,formatting_info=True)   # 注意添加参数formatting_info=True，得以保存之前数据的格式。并且必须为xls的格式，否则不执行！
    table = excel.sheet_by_name(sheet_input)      # 打开名字为sheet1的sheet
    total_num=len(table.col_values(2))-1   #return "the total case number in case.xlsx is: ",total. it depends on url
    for_num=total_num+1  # range右面的限定值

    if data_path:    # 定义data_path
        data_path=data_path
    else:
        data_path="data.json"

    if cookies_path:    # 定义cookies_path
        cookies_path=cookies_path
    else:
        cookies_path="cookies.json"

    copy_data = copy(excel)       # excel写入
    open_sheet = copy_data.get_sheet(sheet_input)  # 打开sheet1

    return table,open_sheet,copy_data,for_num,excel_path,data_path,cookies_path
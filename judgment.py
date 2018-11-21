#coding=utf-8
from no_related import Fno_related
from related import Frelated


def judgment_func(for_num, table, data_path, cookies_path, open_sheet, copy_data):
    for i in range(1, for_num):  # 请求
        if table.col_values(3)[i] == 'yes' and not table.col_values(7)[i]:  # 在run等于yes的时候加上case.xls中H列 所依赖的测试用例rel 中为空
            run = Fno_related()
            run.no_related_func(table, i, data_path, cookies_path, open_sheet, copy_data)    # 即没有依赖
        elif table.col_values(3)[i] == 'yes' and table.col_values(7)[i]:    # 在run等于yes的时候加上case.xls中H列 所依赖的测试用例rel 中有值
            run = Frelated()
            run.related_func(table, i, data_path, cookies_path, open_sheet, copy_data)   # 有数据依赖
        else:
            pass
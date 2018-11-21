#coding=utf-8
from definations import definations_func
from judgment import judgment_func
from statistic import statistic_func
from sendemail import sendemail_func

excel_path = raw_input("Please input your excel file path: ")
sheet_input = raw_input("Please input your sheet file path: ")
data_path = raw_input("Please input your data file path: ")
cookies_path = raw_input("Please input your cookies file path: ")

# 带有*，表示必须要用户手动输入，不可以直接回车，选择默认值。
smtp_server = raw_input("*Please input your smtp server*: ")
send_user = raw_input("*Please input the address of the message sent*: ")
password = raw_input("*Please input the email password*: ")
receive_user_list = raw_input("*Please input the address of the message receive and seperate them with comma*: ")
subject = raw_input("Please input your subject of email: ")



# 获得参数
table, open_sheet, copy_data, for_num, excel_path, data_path, cookies_path = definations_func(excel_path,sheet_input,data_path,cookies_path)
# 判断是否存在数据依赖，并根据请求方式，得到response来判断是否满足预期值
judgment_func(for_num, table, data_path, cookies_path, open_sheet, copy_data)
# 统计数据
run_num, pass_num, failed_num, pass_rate, failed_rate = statistic_func(for_num, table)
# 发送邮件
sendemail_func(smtp_server, send_user, password, receive_user_list, subject, excel_path,run_num, pass_num, failed_num, pass_rate, failed_rate)











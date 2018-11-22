#coding:utf-8
import smtplib      # 发送邮件
from email.mime.multipart import MIMEMultipart  # 带附件
from email.mime.text import MIMEText   # 构建邮件


def sendemail_func(smtp_server, send_user, password, receive_user_list, subject, excel_path, run_num, pass_num, failed_num, pass_rate, failed_rate):
    if smtp_server:
        smtp_server = smtp_server
    else:                      # 如果不输入，则按照默认值来
        smtp_server = "smtp.163.com"
    if send_user:
        send_user = send_user
    else:                       # 如果不输入，则按照默认值来
        send_user = "17709816196@163.com"
    if password:
        password = password
    else:                        # 如果不输入，则按照默认值来
        password = "xxxxxxxx"
    if receive_user_list:
        receive_user_list = receive_user_list.split(",")             # ！以逗号为分隔符，并隔开，并自动变为list的形式
        #receive_user_list = ["17709816196@163.com","1052398277@qq.com"]
    else:                         # 如果不输入，则按照默认值来
        receive_user_list = ["17709816196@163.com"]
    if subject:
        subject = subject
    else:                         # 如果不输入，则按照默认值来
        subject = "api testing report"

    message=MIMEMultipart()     # 邮件

    message['Subject'] = subject
    message['From'] = send_user
    message['To'] = ', '.join(receive_user_list)   # 对字典进行连接之后变成了字符串  list=['1','2','3','4','5']  print(''.join(list))  结果：12345  此处逗号或者分号都是可以的
    content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s, 通过率为%s, 失败率为%s" % (run_num, pass_num, failed_num, pass_rate, failed_rate)

    message.attach(MIMEText(content,'plain','utf-8'))   # 加附件

    att = MIMEText(open(excel_path,'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="case.xls"'

    message.attach(att)
    server = smtplib.SMTP()
    server.connect(smtp_server,25)
    server.login(send_user,password)
    server.sendmail(send_user,receive_user_list,message.as_string())
    server.quit()








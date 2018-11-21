#coding=utf-8
def statistic_func(for_num,table):
    pass_num = 0
    for m in range(1,for_num):
        if table.col_values(3)[m] == 'yes' and table.col_values(14)[m] == 'pass':  # 得到pass的个数
            pass_num = pass_num + 1
        else:
            continue
    run_num = 0
    for l in range (1,for_num):
        if table.col_values(3)[l] == 'yes':  # 得到总的run为yes的个数
            run_num = run_num + 1
        else:
            continue

    failed_num = run_num - pass_num    # 因为failed的状态可能是failed也可能是除了200的状态码，所以采用此减法
    pass_num_1 = float(pass_num)
    failed_num_1 = float(failed_num)
    pass_rate = "%.2f%%" % (pass_num_1 / run_num * 100)
    failed_rate = "%.2f%%" % (failed_num_1 / run_num * 100)

    return run_num, pass_num, failed_num, pass_rate, failed_rate


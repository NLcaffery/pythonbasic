from stus_manager.stus_operate import StusOperate


def run():
    print('=============欢迎登录码同学学员管理系统================')
    # 和控制台做交互，需要设计控制台上的动作和业务方法的对应关系
    # print('请输入你的操作,1(新增)/2(修改)/3(查询)/4(删除)/5(计算平均分):')
    # 我们发现这样写的话，每次执行都只能做一个动作就结束了
    # 但是我们希望的运行系统后，他会做各种各样的业务，除非他主动结束，否则系统应该一直在运行
    while True:
        op = int(input('请输入你的操作,1(新增)/2(修改)/3(查询)/4(删除)/5(计算平均分)/6(退出):'))
        if op==1:
            print('新增学员')
            # 由于新增学员的方法有个不定长关键字参数，不好确定要来几个input
            # 干脆我们让他在输入时直接输入一个json格式的字符串
            # {"no":"1","name":"张三","phone":"18729399607","wx":"wx001","qq":"qq001","score":0}
            stu_str = input('请输入学员信息(必须有编号和姓名):')
            # 把json格式的字符串变成python里的字典
            stu_dict = eval(stu_str)
            # **stu_dict 可以把你的字典变成no=1,name=张三,phone=18729399607，
            print(StusOperate.add_stu(**stu_dict))
        elif op==2:
            print('修改学员')
            # 参考新增设计
            change_info = input('请输入要修改的信息(必须有编号):')
            change_info = eval(change_info)
            print(StusOperate.change_stu(**change_info))
        elif op==3:
            print('查询学员')
            no = input('请输入要查询的学员编号:')
            print(StusOperate.select_stu(no))
        elif op==4:
            print('删除学员')
            no = input('请输入删除的学员编号:')
            print(StusOperate.delete_stu(no))
        elif op==5:
            print(StusOperate.avg_score())
            print('计算平均分')
        elif op==6:
            print('退出成功')
            break
        else:
            print('输入的操作不支持')
if __name__ == '__main__':
    run()

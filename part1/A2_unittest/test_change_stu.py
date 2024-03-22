
import unittest

# 专门修改学员
import ddt

from stus_manager.stus_operate import StusOperate


@ddt.ddt
class TestChangeStu(unittest.TestCase):


    # 类级别的前置和后置，在当前类下都只会执行一次，不管你有多少条用例
    # 对于修改学员来说，我们大部分的场景都有一个前提条件就是用户已存在

    # 所以在该类下所有用例开始执行前先准备数据，这叫做前置处理，并且还是一个类级别的前置处理
    @classmethod
    def setUpClass(cls) -> None:#固定的名字，准备数据，前置
        print('当前类下所有用例开始执行前，先执行我')
        #建造用例，调用学员增加方法--》前置处理
        StusOperate.add_stu(no='200',name='沙陌')

    # 通常有可能在测试完成后，我们需要去清除自己的临时数据
    # 在所有用例执行完之后去做，这叫做后置处理，并且还是一个类级别的后置处理
    @classmethod
    def tearDownClass(cls) -> None:#固定名称
        print('当前类下所有用例执行完成后，才执行我')
        StusOperate.delete_stu(no='200')

    # 但是有的场景可能需要在每条用例执行开始前后去执行
    # 这叫做 方法级别的前置及后置
    def setUp(self) -> None:
        print('用例开始执行啦')
    def tearDown(self) -> None:
        print('用例执行结束啦')

    # 把多组数据采用列表套列表的形式进行存储
    test_data = [
        ['修改用户姓名',{"no":"200","name":"张三三"},'修改成功'],
        ['修改phone', {"no": "200", "phone": "18729399607"}, '修改成功'],
        ['修改wx', {"no": "200", "wx": "wx001"}, '修改成功'],
        ['修改qq', {"no": "200", "qq": "qq001"}, '修改成功'],
        ['修改score', {"no": "200", "score": 80}, '修改成功'],
        ['全部修改', {"no": "200","name": "张三四","phone": "18729399608","wx": "wx002","qq": "qq002","score": 81}, '修改成功']

    ]

    @ddt.data(*test_data)
    def test_change_info(self,data):
        # ['修改用户姓名', {'no': '200', 'name': '张三三'}, '修改成功']
        print(data)
        change_info = data[1] # change_info是个字典，代表修改学员的入参
        expect_msg = data[2]
        res = StusOperate.change_stu(**change_info)
        assert res == expect_msg
        # pass

    # # 修改用户姓名
    # def test_001_change_name(self):
    #     res = StusOperate.change_stu(no='200',name='张三三')
    #     assert res == '修改成功'
    # # 修改phone
    # def test_002_change_phone(self):
    #     res = StusOperate.change_stu(no='200',phone='18729399607')
    #     assert res == '修改成功'
    # # 修改wx
    # def test_003_change_wx(self):
    #     res = StusOperate.change_stu(no='200',wx='wx001')
    #     assert res == '修改成功'
    # # 修改qq
    # def test_004_change_qq(self):
    #     res = StusOperate.change_stu(no='200',qq='qq001')
    #     assert res == '修改成功'
    # # 修改score
    # def test_005_change_score(self):
    #     res = StusOperate.change_stu(no='200',score=80)
    #     assert res == '修改成功'
    #
    # # 一次性全部修改
    # def test_006_change_all(self):
    #     res = StusOperate.change_stu(no='200',name='张三四',phone='18729399608',wx='wx002',qq='qq002',score=90)
    #     assert res == '修改成功'




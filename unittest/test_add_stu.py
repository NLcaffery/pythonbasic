import unittest

from stus_manager.stus_operate import StusOperate


class TestAddStu(unittest.TestCase):#继承unittest.TestCase
    # # 只填写必填项，添加成功
    def test_001_add_stu_require(self):
        # 所谓的测试其实就是调用，并且判断结果
        res = StusOperate.add_stu(no='1',name='张三')
        # 针对结果做判断，这个过程叫做断言
        assert res == '添加成功'

    # 所有非必填都填，添加成功
    def test_002_add_stu_not_require(self):
        # 所谓的测试其实就是调用，并且判断结果
        res = StusOperate.add_stu(no='2',name='张三',phone='18729399607',wx='wx001',qq='qq001',score=80)
        # 针对结果做判断，这个过程叫做断言
        assert res == '添加成功'

    # 学员编号已存在，添加失败
    def test_003_add_stu_no_already(self):
        # 所谓的测试其实就是调用，并且判断结果
        no = '1'
        res = StusOperate.add_stu(no=no,name='张三')
        # 针对结果做判断，这个过程叫做断言
        assert res == f'{no}已存在'

import unittest

from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    # 这个文件中实现测试用例的组织和执行，以及测试报告的生成
    # 组织测试用例，通过测试套件
    # suite = unittest.TestSuite() # 创建一个测试集合对象
    # 单独加一个类或者多个类其实都不太方便
    # suite.addTest(TestAddStu('test_001_add_stu_require')) # 单独添加某个类下的某个用例

    # 按照指定目录，指定文件规则去加载
    suite = unittest.defaultTestLoader.discover('.','test_*.py')#.同一目录，规则test_*,*号表示任意的

    # 执行器
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # 生成html报告，可视化的
    with open('testreport.html',mode='wb') as f:
        HTMLTestRunner(f,title='学员系统测试报告',description='这是描述').run(suite)


from stu_mage.students import Student


class StusOperate:
    stus_dict = {}
     #定义一个类属性
     #｛“编号1”：“1”，学院对象1｝（k, V）

     #**
     # 类方法主要操作类相关的变量，而不是具体的实例对象。
     # 在类方法中，通常使用特殊装饰器@classmethod来标识它是一个类方法。
     # 类方法在调用时，不需要传递类的实例作为参数，而是传递类本身的名称。
     # 类方法的第一参数通常命名为cls，代表类本身。

    @classmethod
         ##
         # 不确定将来要往函数中传入多少个参数，即可使用可变参数（即不定长参数），用*args,**kwargs表示。
         # *args称之为Non-keyword Variable Arguments，无关键字参数；非键值对
         # **kwargs称之为keyword Variable Arguments，有关键字参数；键值对。
         # #

         #增
    def add_stu(cls,no,name,**kwargs):
        if no not in cls.stus_dict:
            cls.stus_dict[no] = Student(no,name,**kwargs)
        else:
             return f'{no}已存在'

        #删除
    @classmethod
    def delete_stu(cls,no):
        if no in cls.stus_dict:
        #删除操作
            del cls.stus_dict[no]
        else:
            return f'{no}不存在'

        # 修改学员
        # 要告诉给这个函数修改的学员是谁？no
        # 还得告诉这个函数要修改学员的什么信息？name=李四，phone=1662636,wx=wx001
        # 好像不太能够确定到底要改啥，而且他要改的必然是这种键值对数据，所以我们可以用**kwargs
    @classmethod
    def change_stu(cls, no, **kwargs):
        """
        修改学员
        :param no:
        :param kwargs:
        :return:
        """
        # 判断编号是否存在，不存在则添加
        if no in cls.stus_dict:
            stu = cls.stus_dict[no]  # 得到学员对象
            # 根据传进来的kwargs来判断要改啥
            # kwargs={"name":"李四","phone":"6236633","qq":"qq888"}
            if "name" in kwargs:
                stu.set_name(kwargs['name'])
            if "phone" in kwargs:
                stu.set_phone(kwargs['phone'])
            if "wx" in kwargs:
                stu.set_wx(kwargs['wx'])
            if "qq" in kwargs:
                stu.set_qq(kwargs['qq'])
            return '修改成功'
        else:
            return f'{no}不存在'

    # 查询学员
    @classmethod
    def select_stu(cls, no):
        # 判断编号是否存在，不存在则添加
        if no in cls.stus_dict:
            stu = cls.stus_dict[no]
            return str(stu)  # 2,李四,18727272,wx001,
        else:
            return f'{no}不存在'

    # 增加一个全班平均分的计算业务

if __name__ == '__main__':
    StusOperate.add_stu(no='1', name='张三', phone="18723773", wx='wx001')
    StusOperate.add_stu(no='2', name='李四', phone="18723774", wx='wx002')
    StusOperate.add_stu(no='3', name='王五', phone="18723775", wx='wx003')
    StusOperate.add_stu(no='4', name='赵六', phone="18723776", wx='wx004')
    print(StusOperate.stus_dict)
    print(StusOperate.select_stu('3'))
    print(StusOperate.change_stu('3', name='赵六六', qq='qq001'))
    print(StusOperate.select_stu('3'))
    print(StusOperate.delete_stu('3'))
    print(StusOperate.select_stu('3'))

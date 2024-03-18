class Student:
    def __init__(self,no,name,phone='',wx='',qq=''):
        self.no = no
        self.name = name
        self.phone = phone
        self.wx = wx
        self.qq = qq

    def __str__(self):
        return f'{self.no},{self.name},{self.phone},{self.wx},{self.qq}'
    #f''字符串格式

    def get_no(self):
        return self.no
    def set_no(self,no):
        self.no = no

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name

    def get_wx(self):
        return self.wx
    def set_wx(self,wx):
        self.wx = wx

    def get_qq(self):
        return self.qq
    def set_qq(self,qq):
        self.qq = qq

if __name__ == '__main__':

    stu1 = Student('1','张三')
    print(stu1)#<__main__.Student object at 0x0000026CAC298508>
    #返回的是学员内存地址
    #使用__str__ 返回字符串格式

    print(stu1.get_name())
    stu1.set_name("李四")
    print(stu1.get_name())
class BaseTest:
    def __init__(self):
        self.test_attr = "hello world"
        print("创建实例成功")
    
    def get_test(self):
        return self.test_attr
    
    def calc_add(self,first_value, second_value):
        return first_value+second_value


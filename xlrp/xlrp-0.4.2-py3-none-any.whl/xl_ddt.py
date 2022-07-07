from functools import wraps


FUNC_NAME = []          # 放置了xl_data的函数
FUNC_PARAM = []         # 用户放入的参数
USE_FUNC = []           # 构造后的字典列表，key为方法名，value为参数

# 装饰器运行顺序，会从上到下执行，也就是先执行xl_ddt，但是并不会执行到wrapper，而是会先执行xl_data的所有，因而可以现在下面的装饰器中对数据进行添加操作
def xl_ddt(cls):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        cls_instance = cls(*args, **kwargs)                 # 对传入的类进行实例化操作
        func_index = 1
        for func, params in zip(FUNC_NAME, FUNC_PARAM):     # 组合FUNC_NAME和参数，合并成USE_FUNC
            if hasattr(cls_instance, func.__name__) is True:
                for param in params:
                    # 构建新的用例名，通过setattr将其放入，并将其赋值成一个函数
                    setattr(cls_instance, f'{func.__name__}_{func_index}', eval(f'cls_instance.{func.__name__}'))
                    USE_FUNC.append({f'{func.__name__}_{func_index}': param})
                    func_index += 1
        return cls_instance
    return wrapper

def xl_data(param_list):
    FUNC_PARAM.append(param_list)       # 将参数添加到FUNC_PARAM参数列表中

    def wrapper(func):
        FUNC_NAME.append(func)          # 将每个函数名称添加到FUNC_NAME中

        @wraps(func)
        def decorator(*args, **kwargs):
            return func(*args, **kwargs)
        return decorator
    return wrapper

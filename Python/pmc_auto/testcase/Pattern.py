#单例模式
# def singleton(cls):
#     instances = {}
#
#     def getinstance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return getinstance
#
# @singleton
# class my_cls(object):
#     pass

class MTC(object):
    STATIC_MEMBER = "STATIC MEMBER of MTC"

    def __new__(cls, *args, **kwargs):
        print("this is MTC __new__ func")
        print (cls, args, kwargs)
        cls.NEW_STATIC_MEMBER = 'NEW STATIC MEMBER of MTC'
        cls.test_func = lambda self, x = 'args': x
        return super(MTC, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("this is MTC __init__ func")
        print(self, args, kwargs)

init_val = (1,2,3,4)
instance = MTC(*init_val, my_key = 'my_value')
print(instance.NEW_STATIC_MEMBER)
print(instance.test_func('This func added in __new__ func!'))
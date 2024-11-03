import inspect


class MyClass:
    def __init__(self):
        self.attribute1 = "Hello"

    def method1(self):
        pass


def introspection_info(obj):
    obj_info = {'type': type(obj).__name__}
    if hasattr(obj, "__dict__"):
        obj_info['attributes'] = obj.__dict__
    obj_info['methods'] = dir(obj)
    obj_info['module'] = inspect.getmodule(obj)
    return obj_info


number_info = introspection_info(42)
print(number_info)

my_object = MyClass()
object_info = introspection_info(my_object)
print(object_info)

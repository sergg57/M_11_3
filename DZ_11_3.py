import inspect
from pprint import pprint

def introspection_info(obj):
    obj_type = type(obj)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_module = obj.__class__.__module__
    obj_in_module = inspect.getmodule(obj)
    if obj_module == 'builtins':
        builtins = True
        #pprint(dir(obj_module))
    else:
        builtins = False

    info = {
        'type': obj_type.__name__,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module,
        'obj_in_module': obj_in_module,
        'builtins': builtins
    }
    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)
list_info = introspection_info([1,2,3,4,5,6,7,8,9])
print(list_info)

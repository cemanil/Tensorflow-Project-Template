

def import_by_name(module_name, class_name):
    module = __import__(module_name)
    my_class = getattr(module, class_name)
    instance = my_class()

    return instance

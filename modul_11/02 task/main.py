from pprint import pprint


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)


create_cart = Cart()


def introspection_info(obj):
    dictionary = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': obj.__module__,
        'class': obj.__class__.__name__,
        'instance': obj,
        'class_attributes': [attr for attr in dir(obj.__class__) if not callable(getattr(obj.__class__, attr))]
    }
    return dictionary

pprint(introspection_info(create_cart))
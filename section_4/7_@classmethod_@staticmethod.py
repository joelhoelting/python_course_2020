class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_object = Foo()
my_object.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello, I hate arguments")


bar_obj = Bar()
bar_obj.hi()

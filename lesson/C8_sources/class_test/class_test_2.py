class MyClass():
    """Another simple class example"""
    def __init__(self, value):
        self.value = value

    def show_value(self):
        print("value = ", self.value) 

a = MyClass(5)
b = MyClass('test')

print(a.value)
print(b.value)

a.show_value()
b.show_value()

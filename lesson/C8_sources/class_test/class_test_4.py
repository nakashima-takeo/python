class MyClass():
    """Another simple class example"""
    instances_count = 0

    def __init__(self, value):
        self.value = value
        MyClass.instances_count += 1

    # Define some functions
    def show_value(self):
        print("value = ", self.value) 

    def show_count(self):
        print("count = ", MyClass.instances_count) 

    def show_all(self):
        self.show_value()
        self.show_count()

# Create an instance 
a = MyClass(5)
a.show_all()
# Create another instance
b = MyClass('test')
b.show_all()

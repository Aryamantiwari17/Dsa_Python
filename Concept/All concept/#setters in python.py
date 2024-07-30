#setters in python
"""self.value is a standard public attribute.
self._value is a conventionally private attribute. By convention, 
a single leading underscore indicates that the attribute or 
method is intended for internal use within the class or module.
"""
class MyClass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")


    @property

    def ten_value(self):
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new_valu):
        self._value=new_valu/10
        return 10* self._value
    


obj=MyClass(10)
print(obj._value)
obj.ten_value=67
print(obj.ten_value)

obj.show()
class base:
    def __init__(self):
        print("BASE INIT")
    def set_name(self,name):
        self.name = name
        print("Base set name")

class sub(base):
    def __init__(self):
        super().__init__()
        print("SUB INIT")
    def set_name(self,name,age):
        super().set_name(name)
        print("Sub set name")
        print(self.name)


x = sub()
x.set_name("Ashik",19)
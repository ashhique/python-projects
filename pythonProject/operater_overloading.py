class operation:
    def set_name(self,name):
        self.name = name

    def __add__(self, other):
        name = self.name+" "+other.name
        return name

first_name = operation()
last_name = operation()

first_name.set_name("Ashik")
last_name.set_name("mon")

full_name = first_name + last_name
print(full_name)
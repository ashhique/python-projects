class first:
    def display(self):
        print("First")

class second:
    def display(self):
        print("second")

class third(second,first):
    def display_third(self):
        print("third")

x = third()
x.display()
x.display_third()
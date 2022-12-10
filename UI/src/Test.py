class Class:
    def __init__(self):
        self.funcs = {
            1: self.f1,
            2: self.f2
        }

    def f1(self):
        print("Hi")

    def f2(self):
        print("Hello")


c = Class()
c.funcs[1]()



class py:

    def __init__(self):
        print("called automatically")

    a=10
    def hi(self):
        self.b=self.a*self.a
        print(self.b)

    def sai(self,a,b):
        print(a+b)


c= py()


c.hi()

print(c.sai(2,3))

           



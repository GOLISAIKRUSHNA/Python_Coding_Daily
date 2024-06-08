




class sai:
    def __init__(self):
        print("automatic constructor")
        self.__name=""

    def setname(self,n):
        self.__name=n

    def getname(self):
        return self.__name
    

o=sai()
o.setname('goli')
s=o.getname()
print(s)
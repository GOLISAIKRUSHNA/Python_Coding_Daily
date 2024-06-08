

# class a:
#     def displayA(self):
#         print("From class A")

# class b(a):
#     def displayB(self):
#         print("From class B")


# o=b()
# o.displayA()
# o.displayB()





# ******************************************************************************************



# class a:
#     def displayA(self):
#         print("From class A")

# class b(a):
#     def displayB(self):
#         print("From class B")
# class c(b):
#     def displayC(self):
#         print("From class C")
        

# o=c()
# o.displayA()
# o.displayB()
# o.displayC()







# *********************************************************************************************





class a:
    def displayA(self):
        print("From class A")

class b:
    def displayB(self):
        print("From class B")
class c(a,b):
    def displayC(self):
        print("From class C")
        

o=c()
o.displayA()
o.displayB()
o.displayC()
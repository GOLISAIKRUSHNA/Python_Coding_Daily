class Test:
    print("class object variable")
    def __init__(self):
        self.a=5
        self.b=10

t1=Test()
t2=Test()

print("this is from t1 instance object variable")
print(t1.a,t1.b)
print("this is from t2 instance object variable")
print(t2.a,t2.b)
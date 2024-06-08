


class hi:

    def over(self):
        print("overriding in first func")


class b(hi):
    def over(self):
        super().over()
        print("overriding in second func")


o=b()
o.over()

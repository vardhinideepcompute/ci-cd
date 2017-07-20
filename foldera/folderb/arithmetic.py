class Arith:
    
    def add(self, a, b):
        c = a + b
        return c

    def mul(self, c):
        return c * 5

x = Arith()
print x.mul(x.add(1, 9))

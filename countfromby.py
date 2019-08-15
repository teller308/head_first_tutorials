class CountFromBy:

    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
    
    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return(str(self.val))


q = CountFromBy(100, 10)
q.increase()
print(q.val)
j = CountFromBy(10, 1)
print(j)
print(type(j))
print(id(j))
print(hex(id(j)))
h = CountFromBy()
print(h)
h.increase()
print(h)
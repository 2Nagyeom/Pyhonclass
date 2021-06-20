class Counter:
    def __init__(self, val=0):
        self.count = val
    def increment(self):
        self.count += 1

a = Counter(100)
a.increment()
print("카운터의 값=",a.count)


b = Counter()
b.increment()
print("카운터의 값=",b.count)
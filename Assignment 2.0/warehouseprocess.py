class Warehouse:
    def __init__(self):
        self.dict = {}
    def process (self, tup) :
        if tup[1] in self.dict :
            if tup[0]=='ship':
                self.dict[tup[1]]=self.dict[tup[1]]-tup[2]
            if tup[0] == 'receive':
                self.dict[tup[1]] = self.dict[tup[1]] + tup[2]
        if tup[1] not in self.dict:
            if tup[0] == 'receive':
                self.dict[tup[1]] = tup[2]
    def lookup (self, a):
        if a not in self.dict:
            return 0
        if a in self.dict:
            return self.dict[a]

w = Warehouse()
w.process(('receive', 'a', 10))

print(w.lookup('a'))  # prints 3



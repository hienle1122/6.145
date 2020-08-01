class Matrix ():
    def __init__(self,list):
        self.l=list
    def size(self):
        return (len(self.l), len(self.l[0]))
    def get(self,a,b):
        return (self.l[a][b])
    def set(self, a, b, val):
        self.l[a][b]=val
    def row(self,a):
        return self.l[a]
    def col(self,a):
        return [self.l[n][a] for n in range(len(self.l))]
    def transpose(self):
        l2 = [[row[i] for row in self.l] for i in range(len(self.l[0]))]
        return Matrix(l2)

    def add(self, other):
        if isinstance(other, Matrix) and self.size() == other.size():
            added = [[self.l[i][j] + other.l[i][j] for j in range(len(self.l[0]))] for i in
                     range(len(self.l))]
            return Matrix(added)
        if isinstance(other, Matrix) and self.size() != other.size():
            return None
        if isinstance(other, int):
            added = [[self.l[i][j] + other for j in range(len(self.l[0]))] for i in
                     range(len(self.l))]
            return Matrix(added)
    def sub(self, other):
        if isinstance(other, Matrix) and self.size() == other.size():
            added = [[self.l[i][j] - other.l[i][j] for j in range(len(self.l[0]))] for i in
                     range(len(self.l))]
            return Matrix(added)
        if isinstance(other, Matrix) and self.size() != other.size():
            return None
        if isinstance(other, int):
            added = [[self.l[i][j] - other for j in range(len(self.l[0]))] for i in
                     range(len(self.l))]
            return Matrix(added)

    def mul(self, other):
        if isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            c = [[0 for j in range(len(other.l[0]))] for i in range(len(self.l))]
            for i in range(len(self.l)):
                for j in range(len(other.l[0])):
                    for k in range(len(other.l)):
                        c[i][j] += self.l[i][k] * other.l[k][j]
            return Matrix(c)
        elif isinstance(other, Matrix):
            return None
        elif isinstance(other, int) or isinstance(other, float):
            mul = [[self.l[i][j] * other for j in range(len(self.l[0]))] for i in range(len(self.l))]
            return Matrix(mul)
        else:
            return None


    def __add__(self, other):
        return self.add(other)
    def __sub__(self, other):
        return self.sub(other)
    def __mul__(self, other):
        return self.mul(other)
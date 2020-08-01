
class Rational:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def computeGCD(self):
        x = self.x
        y = self.y
        while (y):
            x, y = y, x % y
        return x

    def get_numerator(self):
        return int(self.x)

    def get_denominator(self):
        return int(self.y)

    def to_float(self):
        return float(self.x / self.y)

    def reciprocal(self):
        return Rational(self.get_denominator(), self.get_numerator())

    def reduce(self):
        gcd = self.computeGCD()
        reducedRat = Rational(int(self.x / gcd), int(self.y / gcd))
        return reducedRat

    def __add__(self, other):
        if isinstance(other, Rational):
            denom= self.y * other.y
            numer=self.x * other.y + self.y * other.x
            add3 = Rational(numer,denom)
            return add3
        if isinstance(other, float):
            return self.x/self.y+ other
        if isinstance(other, int):
            numer=other*self.y+self.x
            denom=self.y
            add3 = Rational(numer, denom)
            return add3
        else:
            return None
    def __mul__(self, other):
        if isinstance(other, Rational):
            num=self.x * other.x
            denom= self.y * other.y
            add3 = Rational(num, denom)
            return add3
        if isinstance(other, float):
            return self.x / self.y * other
        if isinstance(other, int):
            numer = other * self.x
            denom = self.y
            add3 = Rational(numer, denom)
            return add3
        else:
            return None
    def __truediv__(self, other):
        if isinstance(other, Rational):
            num=self.x * other.y
            denom= self.y * other.x
            add3 = Rational(num, denom)
            return add3
        if isinstance(other, float):
            return self.x / (self.y * other)
        if isinstance(other, int):
            numer = self.x
            denom = self.y*other
            add3 = Rational(numer, denom)
            return add3
        else:
            return None
    def __sub__(self, other):
        if isinstance(other, Rational):
            denom = self.y * other.y
            numer = self.x * other.y - self.y * other.x
            add3 = Rational(numer, denom)
            return add3
        if isinstance(other, float):
            return self.x / self.y - other
        if isinstance(other, int):
            numer =self.x-other * self.y
            denom = self.y
            add3 = Rational(numer, denom)
            return add3
        else:
            return None



res = (Rational(40, 24) + Rational(10, 20)) * 86 - Rational(24,21) / 76
res2 = res.reduce()
ans = (res.get_numerator(), res.get_denominator(), res2.get_numerator(), res2.get_denominator(), res2.to_float())
print (ans)
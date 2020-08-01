out = []
def hailstone_sequence(a_0):
    out.append(a_0)
    if a_0 == 1:
        return out
    elif a_0 % 2 == 0:
        f = a_0/2
    elif a_0 % 2 == 1:
        f = 3 * a_0 + 1
    a_0 = f
    return hailstone_sequence(a_0)

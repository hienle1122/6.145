def approx_integral(f, lo, hi, num_regions):
    delta_x = (hi - lo) / num_regions
    outer = delta_x / 2
    inner = 0
    # outer and inner refer to the way that the trapezoid rule is written with some elements
    # inside of parentheses and others outside of parentheses
    for i in range(num_regions + 1):
        if i == 0 or i == num_regions:
            inner += f(lo + (i * delta_x))
        else:
            inner += 2 * f(lo + (i * delta_x))
    return outer * inner

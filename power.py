def power(base, exponent) :
    ret = 1
    for i in range(exponent) :
        ret *= base
    return ret
    
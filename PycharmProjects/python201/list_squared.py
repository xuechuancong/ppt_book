from math import sqrt
def get_div(x):
    s = []
    for i in range(1,x):
        if x%i == 0:
            # print i, x/i
            s.append(i)
            s.append(x/i)
    h = sum(i**2 for i in set(s))
    return sqrt(h)

def list_squared(m, n):
    p = []
    for i in range(m,n):
        if i == 1:
            p.append([1,1])
            continue
        s = get_div(i)
        if float(s).is_integer():
            print s,i
            p.append([i,s**2])
    return p

list_squared(1,300)
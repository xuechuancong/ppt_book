from math import sqrt
def get_div(x):
    s = []
    for i in range(1,x):
        if x%i == 0:
            # print i, x/i
            s.append(i)
            s.append(x/i)
    return set(s)

# if __name__ == '__main__':
#     get_div(42)
#     print sum(i**2 for i in get_div(42))



def list_squared(m, n):
    p = []
    for i in range(m,n):
        if i == 1:
            p.append([1,1])
            continue
        s = sum(a**2 for a in get_div(i))
        if float(sqrt(s)).is_integer():
            print s,i
            p.append([i,s])
    return p

if __name__ == '__main__':
    list_squared(1,300)






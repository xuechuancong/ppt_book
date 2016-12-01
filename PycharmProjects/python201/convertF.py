
#
# def scm(array):
#     # le = len(array)
#     a_max = max(array)
#     while True:
#         for i in array:
#             if a_max % i == 0:
#                 lcm = a_max
#                 print lcm
#             else:
#                 break
#         a_max += 1
#     return lcm



# if __name__ == '__main__':
#     scm([2,3,4])





#
# def convertFracts(lst):
#     le = len(lst)
#     lis_max = amax(lst)
#     while True:
#         if (lis_max%lst[i][0] == 0 and lis_max%lst[i][1] == 0 for
#                 i in range(le)):
#             print lis_max
#             break
#         else:
#             lis_max += 1

def cal(x,y):
    while y != 0:
        r = y
        y = x%y
        x = r
    print y, x
    return x



if __name__ == '__main__':
    print cal(25,5)
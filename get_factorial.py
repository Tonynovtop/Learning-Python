# 递归运算
# 实现递归的原理，以及递归过程中各变量的值还是有待研究
def get_factorial(n):
    if n == 1:
        return 1
    # print("n的值：%d" %n)
    # result = n * get_factorial(n-1)
    # print("result的值：%d" %result)
    # return result
    return n * get_factorial(n-1)
    
print(get_factorial(4))

def get_factorial1(n):
    ret = i = 1
    while i<=n:
        ret = ret * i
        i = i + 1
    return ret

print(get_factorial1(6))


# 斐波那契级数，是另一个递归的案例
def fabnacc(n):
    # if n == 1:
    #     return 1
    # elif n == 2:
    if n in [1,2]:
        return 1
    return fabnacc(n-1) + fabnacc(n-2)

# print(fabnacc(8))
fabnacc_list = []
for x in range(1,9):
    fabnacc_list.append(fabnacc(x))
print(','.join(str(x) for x in fabnacc_list))

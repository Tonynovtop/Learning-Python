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

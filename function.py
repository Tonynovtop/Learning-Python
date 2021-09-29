from functools import reduce
def plus(a):
    return a+1

d = [1,2,3,4]
r = map(plus,d)
# for x in r:
    # print(x,end=',') # ','隔开，但是结尾会留有','
print(",".join(str(x) for x in r))

# 方法一
def add_op(x,y):
    return x + y

def get_sum(x):
    ret = 0
    for item in x:
        ret = add_op(ret,item)
    print(ret)

d = [2,3,4,5,6]
get_sum(d)

# 方法二，但是由于python3在全局名字空间里移除了，现在放置在functools模块下，因此必须在开头
# 添加from functools import reduce
def add_op1(x,y):
    return x + y

def get_sum1(x):
    ret = reduce(add_op1,x)
    print(ret)

e = [2,3,4,5,6]
get_sum1(e)
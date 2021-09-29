# 函数参数的几种形式：位置参数、把位置参数作为元组（print）、
# 部分实参作为元组、元组和列表作为参数、关键字参数
# 把实参当作字典、调用时使用字典
def get_sum(*a): # a表示的是一个元组
    print("Type of 1: %s" % type(a))
    ret = 0
    for x in a:
        print("x = ",x)
        ret = ret + x
    print("sum = ",ret)

get_sum(1,2,3,4)

def get_sum1(k,*a):
    ret = 0
    for x in a:
        print("x = ",x)
        ret = ret + x
    ret = k * ret
    print("sum = ",ret)

get_sum1(2,4,5,7,6)

def get_list(a,b,c):
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
d = [2,3,4]
get_list(*d)

def get_diff(sub_from,sub_val):
    ret = sub_from - sub_val
    print("%d - %d = %d" % (sub_from,sub_val,ret))

get_diff(120,12)
get_diff(sub_from=56,sub_val=10)

def demo_dict(**d):
    print("type of d is %s" % type(d))
    for k,v in d.items():
        print("%s => %s" % (k,v))

demo_dict(key1 = 1)
demo_dict(key1 = 1,key2 = 2,key3 = 3)

def func_demo(a,b,c):
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)

d = {"a":10,"b":20,"c":30}
func_demo(**d)
e = {"c":30,"a":10,"b":20}
func_demo(**e)
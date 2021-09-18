import sys

def cal_sqrt_with_newton(start,end,target,stop): #获取用户参数
    while True:
        mid = (start + end) / 2.0
        if abs((mid * mid) - target) < stop: # 如果精度达到要求
            return mid # 返回中间值
        else:
            if (mid * mid) > target: # 否则继续二分法
                end = mid
            else:
                start = mid

def py_sqrt(v):
    if v > 1.0: # 如果值大于1，那么在1和v之间
        return cal_sqrt_with_newton(1.0,v,v,1.0e-6)
    else: # 如果值小于1，那么在v和1之间
        return cal_sqrt_with_newton(v,1.0,v,1.0e-6)

def test(v): # 测试计算结果
    ret = py_sqrt(v)
    print("sqrt(%s) = %s" % (v,ret)) # 显示计算结果

if __name__ == '__main__':
    input = float(sys.argv[1]) # 执行该脚本，并在第二个位置输入参数，如：python cal_sqrt_with_newton.py 2.0
    # input = 5.8 # 另一种方式：直接指定参数传入
    test(input)
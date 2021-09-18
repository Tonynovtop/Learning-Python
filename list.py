import random # 引入伪随机数模块
def find_missing_number(list): # 查找丢失的数
    for candidate in range(1,101):
        if candidate not in list: # 如果1-100中有数不在结果中，即为丢失的数
            return candidate
    return None

def test():
    list_a = list(range(1,101)) # 注意：这里必须加list进行强制转换，不然输出的为range对象
    random.shuffle(list_a) # 打乱顺序
    drop_val = list_a.pop(49) #丢掉一个数
    print("The Dropped item is %d" % drop_val)
    ret = find_missing_number(list_a) # 查找丢失的数
    print("Answer: %d" % ret)

if __name__ == '__main__': # 如果脚本运行而不是import，那么执行测试代码
    test()
# 合并结果
# 两个文件的统计已经在各自的机器上完成了，
# 并且结果以字典的方式保存，现在需要合并这两个结果字典，得到一个完整的统计结果
# 两个文件的结果字典如下：
# {
#     "a":10,
#     "b":21,
#     ...
#     "z":18
# }
import random
import string
def generate_2_dict(): # 产生两个字典
    a = dict()
    b = dict()
    for x in string.ascii_lowercase: # 从a-z的字符串中得到字典的键
        temp_num = random.randint(0,10)
        if temp_num > 0:
            a[x] = temp_num
        temp_num1 = random.randint(0,10)
        if temp_num1 > 0:
            b[x] = temp_num1
    return (a,b)

def merge_dict(a,b): # 合并两个结果字典
    ret = dict()
    for x in string.ascii_lowercase:
        val1 = a.get(x,0)
        val2 = b.get(x,0)
        merge_val = val1 + val2
        if merge_val > 0:
            ret[x] = merge_val
    return ret

dict_a,dict_b = generate_2_dict() # 生成输入的两个字典
print("第一个字典的值：%s" % dict_a)
print("第二个字典的值：%s" % dict_b)
merged_dict = merge_dict(dict_a,dict_b) # 合并输入字典
print("合并后的字典：%s" % merged_dict) # 显示合并后的字典的内容,得到的结果是乱序的！！！怎么解决？
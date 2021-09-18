# 给定一个列表，将重复出现的元素删除
# 将列表转换为集合，在将集合转换为列表即可
input_list = [1,2,1,23,42,33,5]
output_list = list(set(input_list))
print(output_list)

# 对列表进行排序
print("排序后的列表：")
print(sorted(output_list))

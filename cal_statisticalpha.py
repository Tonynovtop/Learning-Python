input_str = """The First-ever Open-water Beluga Sanctuary will Welcome to
Adorable Whales in June,Adorable beluga whales are a pupular attraction to aquariums
around the world,but like many other wild animals,they also risk losing their habitats
due to human intervention such as population growth,new buildings along the coastline,
fishing,and other problems that sea creatures face."""
def calc_statistic(input_str): # 计算英文字母出现的频率
    result = [0] * 26 # 构建结果列表。26个0组成的列表
    for c in input_str: # 对于字符串中的每个字符
        if c.isalpha(): # 判断是否为字母
            c = c.lower() # 统一转换为小写
            index = ord(c) - ord('a') # 计算出其相对a的位置
            result[index] = result[index] + 1 # 将出现次数加1
    for ele in range(0,26): # 
        c = chr(ord('a') + ele)
        print("[%s] 出现的次数为 %d" % (c,result[ele]))

calc_statistic(input_str)

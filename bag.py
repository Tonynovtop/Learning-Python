# 待解决的问题：输出selection_decision所有的元素，格式为一行4个，依次排列。
goods_list = [1,3,6,8]
def resolve_bag(bag_volume,goods_list): # 传入背包容量、物品清单
    biggest_valid_vol = 0 # 最大有效空间
    biggest_valid_selection = [] # 最大有效选择
    goods_num = len(goods_list) # 物品数量
    candidate_num = 1 << goods_num # 可选的数量,即所有可能出现的情况总数，2**goods_num
    for candidate in range(candidate_num): # 循环每种情况
        selection_decision = [] # 是否选择该物品
        for x in range(goods_num): # 对于每一个物品
            if (candidate & 1) == 1: # 对于1-15
                selection_decision.append(True)
            else: # 对于0
                selection_decision.append(False)
            candidate = candidate >> 1 # 除以2是什么鬼？
        current_vol  = 0 # 当前容量为0
        for x in range(goods_num): # 对于每一个物品
            if selection_decision[x] == True: # 如果选择了该物品
                current_vol = current_vol + goods_list[x] # 此时的容量
        if current_vol <= bag_volume and current_vol > biggest_valid_vol: # 如果容量在背包空间范围内，同时比前一次有效容量大，则将这一次容量作为最大有效容量
            biggest_valid_vol = current_vol # 此时当前的容量作为最大有效空间
            biggest_valid_selection = selection_decision # 选择列表作为最大有效选择
    result = [goods_list[x] for x in range(goods_num) if biggest_valid_selection[x] == True] # 语句中结合循环、条件、列表取值，运用比较灵活
    print(result)

resolve_bag(10,goods_list)
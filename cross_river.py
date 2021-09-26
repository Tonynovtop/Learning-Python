# 有虎、豹、狼三对母子靠一只小船过河，已知：
# 虎、豹、狼母亲和小虎会驾船
# 大动物在一起不会互相伤害，小动物在一起也不会互相伤害，但如果小动物离开了母亲而有其他大动物在，
# 则小动物会受到伤害。
# 不论大小，小船每次只能载两只动物。
# encoding: utf-8
import copy
gstate = [] # 记录所有的状态
def init_state(): # 初始化状态
    # 键是虎、豹、狼母亲
    # 值是是否已经过河
    state = {
        'tiger_mother': False,
        'panther_mother': False,
        'wolf_mother': False,
        'tiger_kid': False,
        'panther_kid': False,
        'wolf_kid': False,
        'boat': False
    }
    gstate.append(state)

def is_state_safe(state): # 判断某种状态是否安全，即不能有动物被吃掉
    # 如果小虎不安全
    if (state['tiger_mother'] != state['tiger_kid']) and ((state['tiger_kid'] == state['panther_mother']) or (state['tiger_kid'] == state['wolf_mother'])):
        return False
    # 如果小豹不安全
    if (state['panther_mother'] != state['panther_kid']) and ((state['panther_kid'] == state['tiger_mother']) or (state['panther_kid'] == state['wolf_mother'])):
        return False
    # 如果小狼不安全
    if (state['wolf_mother'] != state['wolf_kid']) and ((state['wolf_kid'] == state['tiger_mother']) or (state['wolf_kid'] == state['panther_mother'])):
        return False
    return True # 都很安全，返回True

def print_state(state):
    ret_str = ""
    if not state['tiger_mother']:
        ret_str = ret_str + ' tm'
    if not state['panther_mother']:
        ret_str = ret_str + ' pm'
    if not state['wolf_mother']:
        ret_str = ret_str + ' wm'
    if not state['tiger_kid']:
        ret_str = ret_str + ' tk'
    if not state['panther_kid']:
        ret_str = ret_str + ' pk'
    if not state['wolf_kid']:
        ret_str = ret_str + ' wk'
    if not state['boat']:
        ret_str = ret_str + ' boat'
    ret_str = ret_str + ' <-> '
    if  state['tiger_mother']:
        ret_str = ret_str + ' tm'
    if  state['panther_mother']:
        ret_str = ret_str + ' pm'
    if  state['wolf_mother']:
        ret_str = ret_str + ' wm'
    if  state['tiger_kid']:
        ret_str = ret_str + ' tk'
    if  state['panther_kid']:
        ret_str = ret_str + ' pk'
    if  state['wolf_kid']:
        ret_str = ret_str + ' wk'
    if  state['boat']:
        ret_str = ret_str + ' boat'
    print(ret_str)

def print_steps(): # 显示状态转换过程
    for state in gstate:
        print_state(state)
    print("")

def is_done(): # 判断游戏是否结束
    last_state = gstate[-1]
    if last_state['tiger_mother'] == True and \
        last_state['panther_mother'] == True and \
        last_state['wolf_mother'] == True and \
        last_state['tiger_kid'] == True and \
        last_state['panther_kid'] == True and \
        last_state['wolf_kid'] == True:
        return True
    return False

def equal_state(state1,state2):
    if state1['tiger_mother'] == state2['tiger_mother'] and \
        state1['panther_mother'] == state2['panther_mother'] and \
        state1['wolf_mother'] == state2['wolf_mother'] and \
        state1['tiger_kid'] == state2['tiger_kid'] and \
        state1['panther_kid'] == state2['panther_kid'] and \
        state1['wolf_kid'] == state2['wolf_kid'] and \
        state1['boat'] == state2['boat']:
        return True
    return False

def search_state(state):
    for old_state in gstate:
        if equal_state(old_state,state):
            return True
    return False

def cross_river(first,second):
    if len(gstate) <= 0:
        print("List empty")
        return False
    last_state = gstate[-1]
    if first is None and second is None: # 没有指定任何动物过河
        return False
    if (first is not None) and (last_state['boat'] != last_state[first]): # 船和动物不在一起，没法过河
        return False
    if (second is not None) and (last_state['boat'] != last_state[second]):# 船和动物不在一起，没法过河
        return False
    if (first not in ['tiger_mother','panther_mother','wolf_mother','tiger_kid']) and \
        (second not in ['tiger_mother','panther_mother','wolf_mother','tiger_kid']): # 没有会划船的动物，没法过河
        return False
    new_state = copy.copy(last_state)
    if first is not None:
        new_state[first] = not new_state[first]
    if second is not None:
        new_state[second] = not new_state[second]
    new_state['boat'] = not new_state['boat']
    if is_state_safe(new_state) and search_state(new_state) == False:
        gstate.append(new_state)
        return True
    return False

def try_next_step():
    moved = False
    if is_done():
        return True
    for candidate in ['tiger_mother','panther_mother','wolf_mother','tiger_kid','panther_kid','wolf_kid']:
        ret = cross_river(candidate,None)
        if ret:
            if is_done():
                return True
            else:
                try_next_step()
        else:
            pass
    for candidate1 in ['tiger_mother','panther_mother','wolf_mother','tiger_kid','panther_kid','wolf_kid']:
        for candidate2 in ['tiger_mother','panther_mother','wolf_mother','tiger_kid','panther_kid','wolf_kid']:
            if candidate != candidate2:
                ret = cross_river(candidate1,candidate2)
                if ret:
                    if is_done():
                        return True
                    else:
                        try_next_step()
                else:
                    pass
    if len(gstate) == 0:
        print("pop empty list")
    else:
        gstate.pop()

init_state()
try_next_step()
if is_done():
    print_steps()
else:
    print("No answer to this question")
# 输出结果：(存在问题，第三行)
# tm pm wm tk pk wk boat <-> 
# tm pm wm pk wk <->  tk boat
# tm pm wm pk wk boat <->  tk
# pm wm pk wk <->  tm tk boat
# pm wm pk wk boat <->  tm tk
# pk wk <->  tm pm wm tk boat
# tk pk wk boat <->  tm pm wm
# wk <->  tm pm wm tk pk boat
# wm wk boat <->  tm pm tk pk
# wm wk <->  tm pm tk pk boat
# tm pm wm wk boat <->  tk pk
# tm pm wm wk <->  tk pk boat
# tm pm wm tk wk boat <->  pk
# tm wm tk wk <->  pm pk boat
# tm wm tk wk boat <->  pm pk
# tk wk <->  tm pm wm pk boat
# tk wk boat <->  tm pm wm pk
# <->  tm pm wm tk pk wk boat
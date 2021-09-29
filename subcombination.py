def sub_combination(left,right):
    if len(left) > 0:
        for item in left:
            new_right = right + [item]
            new_left = [x for x in left if x != item]
            sub_combination(new_left,new_right)
    else: # else不可以省略，省略后子循环每循环一次都会执行以下语句一次。Q:什么时候可以省略，什么时候不可以省略呢？
        print(right)
    # print(right)
if __name__ == "__main__":
    sub_combination(['tom','jack','jerry','cook'],[])
import random
def find_missing_number(list):
    expected_sum = (1 + 100) * 100 / 2
    real_sum = sum(list)
    return (expected_sum - real_sum)
def test():
    list_b = list(range(1,101))
    random.shuffle(list_b)
    drop_val = list_b.pop(46)
    print("The Droped item is %d" % drop_val)
    print("Answer: %d" % find_missing_number(list_b))

if __name__ == '__main__':
    test()
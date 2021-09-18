# 逻辑判断程序化

def A_lies(who_takes_money):
    """
    如果who_takes_money拿了钱，A说谎了吗？
    """
    # 如果A拿了钱，那么她没有说谎
    if who_takes_money.find("A") != -1:
        return False
    # 否则A说谎
    else:
        return True

def B_lies(who_takes_money):
    """
    如果who_takes_money拿了钱，B说谎了吗？
    """
    # 如果A拿了钱，B没有拿钱，那么B没有说谎
    if (who_takes_money.find("A") != -1) and (who_takes_money.find("B") == -1):
        return False
    else:
        return True

def C_lies(who_takes_money):
    """
    如果who_takes_money拿了钱，C说谎了吗？
    """
    # 如果B或C拿了钱，那么C说谎了
    if (who_takes_money.find("B") != -1) or (who_takes_money.find("C") != -1):
        return True
    else:
        return False

for money_taker in ['A','B','C','AB','AC','BC','ABC']:
    lier_number = 0
    if A_lies(money_taker):
        lier_number = lier_number + 1
    if B_lies(money_taker):
        lier_number = lier_number + 1
    if C_lies(money_taker):
        lier_number = lier_number + 1
    if lier_number == 1:
        print("[%s] 拿了钱" % money_taker)
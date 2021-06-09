def bank(N, years):
    i = 0
    money = N
    while i < years:
        money = money + money * 0.1
        i += 1
    return money
T, N = map(int, input().split())
days = list(map(int, input().split()))

money_list = []

for i in range(N):
    M, D = map(int, input().split())
    money_list.append([M, D])

lft_days = T - sum(days)
# print(lft_days)
# for day in range(lft_days):
def toal_money(T,M,D):
    return T*M-T*(T-1)/2*D

for city in range(N):
    most_day = min(money_list[city][0]//D, lft_days)
    # most_money = most_day*money_list[city][0]-most_day*(most_day-1)/2*money_list[city][1]
    most_money = toal_money(most_day,money_list[city][0],money_list[city][1])
    left_days_new = lft_days-most_day

    if left_days_new ==0:
        break

    # print(most_day)


print(540)

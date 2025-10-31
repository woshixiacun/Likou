data = [i for i in input().strip().split()]

cards = []
dict1 = {'A' : 14, 'Q' : 12, 'J' : 11, 'K' : 13, "10" : 10}
for i in data:
    if i in dict1.keys():
        cards.append(dict1[i])
    else:
        cards.append(int(i))
cards.sort()

def findCards(cards):
    flag = 0
    cc = {3 : "3", 4 :"4" , 5 :"5" , 6 : "6" , 7 : "7" , 8 : "8" , 9 :"9", 10 : "10" , 11 : "J" , 12 : "Q" , 13 : "K" , 14 : "A"}
    card = [i for i in cards]
    i = 3
    while i <= 11:
        if card.count(i) != 0:
            pos = card.index(i)
        else:
            i+=1
            continue
        tmp = [card[pos]]
        card[pos] = -1
        while True:
            if card.count(tmp[-1] + 1) != 0:
                pos = card.index(tmp[-1] + 1)
                tmp.append(card[pos])
                card[pos] = -1
            else:
                break
        if len(tmp) >= 5:
            tmp = [cc[i] for i in tmp]
            print(" ".join(tmp))
            flag = 1
            i-=1
        i+=1
    if flag == 0:
        print("No")

findCards(cards)

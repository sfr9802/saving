import random

card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cal = ["+", "-", "/"]


p1_cash = 10000
p2_cash = 10000

p1_jjam = []
p2_jjam = []


turn_1_p1 = random(card)
print("P1의 숫자카드뽑기" + turn_1_p1)
turn_1_p2 = random(card)
print("P2의 숫자카드뽑기" + turn_1_p2)
    

# 1차
p1_bet = int(input("자본금 10% 이상 베팅 요망"))
if p1_bet < p1_cash/10 :
    p2_bet = int(input("베팅금액이 10% 미만임"))
else :
    print("P1 베팅완료")
    p2_cash = p2_cash-p1_bet

p2_bet = int(input("자본금 10% 이상 베팅 요망"))
if p2_bet < p2_cash/10 :
    p2_bet = int(input("베팅금액이 10% 미만임"))
else :
    print("P1 베팅완료")
    p2_cash = p2_cash-p2_bet


if turn_1_p1 == 7 :
    print("P1의 승리")

elif turn_1_p1 == turn_1_p2 :
    turn_1_p2 = random(card)
    if turn_1_p2 == 7 :
        print("P2의 승리")
else :
    if turn_1_p1 < turn_1_p2 :
        p2_cash2 = p2_cash + p1_bet + p2_bet
    else :
        p1_cash = p1_cash + p1_bet + p2_bet
    










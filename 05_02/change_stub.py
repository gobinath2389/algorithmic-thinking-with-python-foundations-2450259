# 1p 2p 5p 10p 20p 50p 1 
def make_change(target_amount):
    denomination = []
    while target_amount>0:
        if target_amount > 100:
            remainder = target_amount%100
            quotient = target_amount//100
            denomination.append(f'£{quotient}')
            target_amount = remainder
        elif target_amount > 50:
            remainder = target_amount%50
            quotient = target_amount//50
            denomination.append(f'{50*quotient}p')
            target_amount = remainder
        elif target_amount > 20:
            remainder = target_amount%20
            quotient = target_amount//20
            denomination.append(f'{20*quotient}p')
            target_amount = remainder
        elif target_amount > 10:
            remainder = target_amount%10
            quotient = target_amount//10
            denomination.append(f'{10*quotient}p')
            target_amount = remainder
        elif target_amount > 5:
            remainder = target_amount%5
            quotient = target_amount//5
            denomination.append(f'{5*quotient}p')
            target_amount = remainder
        elif target_amount > 2:
            remainder = target_amount%2
            quotient = target_amount//2
            denomination.append(f'{2*quotient}p')
            target_amount = remainder
        else :
            remainder = target_amount%1
            quotient = target_amount//1
            denomination.append(f'{quotient}p')
            target_amount = remainder
    return denomination

print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p

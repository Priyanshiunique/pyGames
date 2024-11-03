
import random as r
while True:
    print('='*90)
    print('*************************ROLLING THE DICE********************************')
    print('='*90)
    num=r.randint(1,6)
    if num==6:
        print('hey you got ....',num,'congratulations')
    elif num==1:
        print('well tried ..but you got ',num)
    else:
        print('you  got :',num)
    
    ch=input('roll again?(Y/N)')
    if ch in 'Nn':
        break
print('thanks for playing!!!!!!!!!!!!!!!!!!!!!!!!!!!')
          

# coding: utf-8
import random
roll_dict()
def roll_dict(num=3,p=None):
    print('<<< Roll The Dict!!! >>>')
    if p is None:
        p = []
    while num > 0 :
        p1 = random.randrange(1,7)
        p.append(p1)
        num = num - 1 
    return p
    
        
roll_result(sum(roll_dict()))
def roll_result(total):
    isbig = 11 <= total <= 18
    issmall = 3 <= total <= 10
    if isbig:
        return 'Big is ' + str(total)
    elif issmall:
        return 'small is ' + str(total)
        
roll_result(sum(roll_dict()))

position=int(input('enter the position'))
i=1
index=1
while True:
    if i%3!=0 and i%10!=3:
        index+=1
    if index>position:
        print('the number at that position',i)
        break
    i+=1
# given index=position-1
#1,2,4,5,7,8,10,11....
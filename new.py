a=int(input('enter amount '))
if (a>25000):
    print('category is gold')
    discount=a*(20/100)
    amount=a-discount
elif (10000<a<25000):
    print('category id silver')  
    discount=a*(10/100)
    amount=a-discount
else:
    print('category is bronze')   
    discount=a*(5/100) 
    amount=a-discount
print(f'amount is{a} and dicount is {discount} and final amount is {amount}')    
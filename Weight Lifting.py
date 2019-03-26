weight=int(input('Please enter the weight'))

if weight in range (50,60):
    print (f'Batch one and weight is {weight}')
elif weight in range (61,70):
    print (f'Batch two and weight is {weight}')
elif weight in range (71,80):
    print (f'Batch three and weight is {weight}')
else: print ('BETTER LUCK NEXT TIME')
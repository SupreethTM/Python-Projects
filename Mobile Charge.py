
battery = int(input('Battery status'))

if battery <=10:
    print('connect charger')
    charger=int(input('charger connected is 1 if not 0 = '))
    if charger==1:
        print ('charging||||||||')
    else:print ('Battery about to drain and power off.....!')
elif battery in range (11,90):
    print (f'the battery value{battery}%')
else:print('charge is 100%')
    

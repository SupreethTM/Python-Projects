traffic_violation = 0

while traffic_violation < 3:
    traffic_update = int (input('traffic status 0 or 1'))
    if traffic_update == 1:
        traffic_violation +=1
    else :
        print (f'you left with few chance {traffic_violation} ')
print ('traffic violation has been exited Licence has been cancled ')
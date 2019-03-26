import datetime
cap_alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sam_alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
spe = ['!','@','#','$','%','^','&','*']
t = [0,0,0,0]
new = input ('enter the password ')
new1 = list (new)
D= datetime.datetime.now()
if (len(new1)) > 7:
    for test in new1:
        if test in cap_alp:
            t[0]=1
        elif test in sam_alp:
            t[1]=1
        elif test in num:
            t[2]=1
        elif test in spe:
            t[3]=1
        else :
            pass
else:
    print ('The length is less than 8 Please try again ')

if (0 not in t) and ((len(new1)) > 7):
    print (f'The password has been changed :{new} Time :{D}')
else:
    print ('The entered value is not meeting requriment ')